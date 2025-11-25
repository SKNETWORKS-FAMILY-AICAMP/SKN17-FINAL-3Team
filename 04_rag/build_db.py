import os
import re
import glob
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ==========================================
# [설정] API 키 입력 (새로 발급받은 키 사용)
# ==========================================
os.environ["OPENAI_API_KEY"] = ""

DATA_DIR = "./"
DB_PATH = "./faiss_index"

def parse_match_log_clean(file_path: str):
    """
    제목에서 (날짜) 부분을 아예 제거하고 순수 제목만 추출하여 저장
    """
    print(f"   Processing: {os.path.basename(file_path)}")
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    # '---' 구분자로 경기 분리
    raw_matches = text.split('\n---')
    docs = []

    for match_text in raw_matches:
        match_text = match_text.strip()
        if not match_text:
            continue

        # -------------------------------------------------
        # [핵심 수정] 제목 정제 로직 (날짜 삭제)
        # -------------------------------------------------
        lines = match_text.split('\n')
        clean_title = "Unknown Match"
        
        for line in lines:
            # '#'으로 시작하는 헤더 라인 찾기
            if line.strip().startswith("#"):
                # 1. '#' 제거
                temp_title = line.replace("#", "").strip()
                
                # 2. ( ) 괄호와 그 안의 내용(날짜)을 정규식으로 삭제
                # 예: "2025 한국시리즈 (2025-10-26)" -> "2025 한국시리즈"
                temp_title = re.sub(r"\(.*?\)", "", temp_title)
                
                # 3. 앞뒤 공백 한번 더 제거
                clean_title = temp_title.strip()
                break
        
        # 로그로 확인
        print(f"    >> 제목 추출: '{clean_title}'") 

        metadata = {
            "source": file_path,
            "type": "match_log",
            "match_title": clean_title,
        }

        docs.append(Document(page_content=match_text, metadata=metadata))
        
    return docs

def main():
    all_documents = []
    md_files = glob.glob(os.path.join(DATA_DIR, "*.md"))
    
    print(f"📂 파일 목록: {md_files}")

    if not md_files:
        print("❌ 오류: .md 파일이 없습니다.")
        return

    # 1. 파싱 (Parsing)
    for file_path in md_files:
        filename = os.path.basename(file_path)
        
        # 규정집이 아닌 경우 -> 경기 기록
        if "규정" not in filename and "규칙" not in filename:
            all_documents.extend(parse_match_log_clean(file_path))
        else:
            # 규정집은 통째로
            with open(file_path, 'r', encoding='utf-8') as f:
                all_documents.append(Document(page_content=f.read(), metadata={"match_title": "규정집"}))

    if not all_documents:
        print("❌ 생성된 문서가 없습니다.")
        return

    print(f"📊 총 {len(all_documents)}개의 문서 로드됨.")

    # 2. 청킹 (Chunking)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = text_splitter.split_documents(all_documents)

    # 3. 임베딩 및 저장
    print("🚀 벡터 DB 생성 시작...")
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(split_docs, embeddings)
    vectorstore.save_local(DB_PATH)
    print(f"✅ DB 생성 완료! 경로: {DB_PATH}")

if __name__ == "__main__":
    main()