import streamlit as st
import streamlit.components.v1 as components
import os

# -----------------------------------------------------------------------------
# 1. 페이지 설정 및 Advanced CSS 스타일링
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="BAIS - Baseball AI Select",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 구글 폰트 임포트 및 커스텀 CSS
st.markdown("""
<style>
    /* 폰트 임포트 (로고용: Bebas Neue, 본문용: Noto Sans KR) */
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Noto+Sans+KR:wght@300;400;700&display=swap');

    /* 1. Streamlit 기본 구조 초기화 */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    .stApp {
        background-color: #141414; /* 넷플릭스 다크 배경 */
        margin-top: -60px; /* 상단 빈 공간 제거 */
    }
    
    /* 본문 컨테이너 여백 재설정 (여백 확보의 핵심) */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 5rem !important;
        padding-left: 4rem !important;
        padding-right: 4rem !important;
        max-width: 100%;
    }

    /* 2. 텍스트 스타일링 */
    body, p, div, span {
        font-family: 'Noto Sans KR', sans-serif;
        color: #e5e5e5;
    }
    h1, h2, h3, h4, h5 {
        font-family: 'Noto Sans KR', sans-serif;
        color: #ffffff !important;
        font-weight: 700;
    }

    /* 3. 고정 헤더 스타일 */
    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 80px;
        background: linear-gradient(to bottom, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%); /* 투명 그라데이션 */
        background-color: #141414; /* 스크롤 시 배경 */
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 60px; /* 헤더 좌우 여백 */
        border-bottom: 1px solid #333;
    }
    
    .logo-text {
        font-family: 'Bebas Neue', sans-serif; /* 임팩트 있는 폰트 */
        font-size: 42px;
        color: #E50914;
        letter-spacing: 2px;
        cursor: pointer;
        padding-top: 10px;
    }

    /* 4. 메인 컨텐츠 래퍼 (여백 관리) */
    .main-wrapper {
        margin-top: 100px; /* 헤더 높이만큼 띄우기 */
        padding: 0 80px; /* 전체 좌우 여백 (넓게) */
    }

    /* 5. 서비스 소개 배너 (Hero Banner) */
    .intro-banner {
        margin-top: 20px;
        position: relative;
        /* 배경 이미지 추가 (야구장 느낌) + 어두운 오버레이 */
        background: 
            linear-gradient(90deg, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.7) 50%, rgba(0,0,0,0.4) 100%),
            url('https://images.unsplash.com/photo-1508344928928-7165b67de128?q=80&w=1920&auto=format&fit=crop');
        background-size: cover;
        background-position: center center;
        
        /* 세로 여백 대폭 확대 */
        padding: 120px 60px; 
        border-radius: 16px;
        margin-bottom: 60px;
        
        /* 테두리 및 그림자 */
        border: 1px solid #333;
        box-shadow: 0 20px 50px rgba(0,0,0,0.7);
        overflow: hidden;
    }
    
    /* AI 뱃지 스타일 */
    .ai-badge {
        display: inline-block;
        background-color: #E50914;
        color: white;
        padding: 6px 14px;
        border-radius: 4px;
        font-size: 14px;
        font-weight: 900;
        letter-spacing: 1px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(229, 9, 20, 0.4);
    }

    .intro-title {
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 52px; /* 폰트 크기 확대 */
        font-weight: 900;
        margin-bottom: 40px;
        color: white;
        line-height: 1.2;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }
    
    .intro-desc {
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 20px;
        color: #e0e0e0;
        line-height: 1.6;
        max-width: 700px; /* 텍스트가 너무 퍼지지 않게 제한 */
        text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    }
    
    /* 강조 텍스트 */
    .highlight-text {
        color: #E50914;
        font-weight: bold;
    }

    /* 6. 영상 섹션 제목 스타일 */
    .section-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
        margin-top: 40px;
        border-left: 4px solid #E50914;
        padding-left: 15px;
    }

    /* 7. 버튼 스타일 커스텀 */
    .stButton > button {
        background-color: #E50914;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 1.5rem;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #ff1f2b;
        transform: scale(1.05);
        box-shadow: 0 0 15px rgba(229, 9, 20, 0.5);
    }
    
    /* 8. 채팅창 스타일 */
    .chat-container {
        background-color: #1f1f1f;
        border-radius: 12px;
        padding: 20px;
        height: 650px;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
        border: 1px solid #333;
    }
    .chat-bubble-ai {
        background-color: #E50914;
        color: white;
        padding: 15px;
        border-radius: 15px 15px 15px 2px;
        margin-bottom: 15px;
        font-size: 15px;
        line-height: 1.5;
        max-width: 90%;
    }
    .chat-bubble-caster {
        background-color: #333;
        color: #ddd;
        padding: 12px 15px;
        border-radius: 15px 15px 2px 15px;
        margin-bottom: 15px;
        font-size: 14px;
        align-self: flex-end;
        max-width: 80%;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. 데이터 관리 (videos 폴더 내 파일 자동 매핑)
# -----------------------------------------------------------------------------

video_data = [
    {
        "id": 1,
        "title": "2025 KBO 리그 6/10 하이라이트",
        "desc": "한화 vs 키움",
        "video_path": "videos/마지막.mp4"
    },
    {
        "id": 2,
        "title": "2025 NAVER K-BASEBALL SERIES 1차전 하이라이트",
        "desc": "대한민국 vs 체코",
        "video_path": "videos/2025 NAVER K-BASEBALL SERIES 1차전 대한민국 vs 체코.mp4"
    },
    {
        "id": 3,
        "title": "2025 NAVER K-BASEBALL SERIES 2차전 하이라이트",
        "desc": "대한민국 vs 체코",
        "video_path": "videos/2025 NAVER K-BASEBALL SERIES 2차전 대한민국 vs 체코.mp4"
    },
    {
        "id": 4,
        "title": "2023 WBC 조별리그 최종전 하이라이트",
        "desc": "대한민국 vs 중국",
        "video_path": "videos/2023 WBC 조별리그 최종전 대한민국 vs 중국.mp4"
    }
]

# -----------------------------------------------------------------------------
# [로직 추가] URL 파라미터 감지 및 상태 업데이트
# -----------------------------------------------------------------------------
query_params = st.query_params

# 1. 페이지 이동 처리
if "page" in query_params:
    st.session_state.page = query_params["page"]

if "page" in query_params and query_params["page"] == "main":
    st.session_state.page = "main"

# 2. 비디오 선택 처리 (?view=ID)
if "view" in query_params:
    try:
        view_id = int(query_params["view"])
        # ID에 해당하는 비디오 찾기
        selected = next((item for item in video_data if item["id"] == view_id), None)
        if selected:
            st.session_state.selected_video = selected
    except:
        pass # ID가 숫자가 아니거나 에러나면 무시

# 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'main'
if 'selected_video' not in st.session_state:
    st.session_state.selected_video = video_data[0]

# -----------------------------------------------------------------------------
# 3. 공통 컴포넌트
# -----------------------------------------------------------------------------
def render_header():
    st.markdown("""
        <div class="fixed-header">
            <div class="logo-text">BAIS</div>
            <div style="display: flex; align-items: center; gap: 20px;">
                <span style="color: #ddd; font-size: 14px;">홈</span>
                <span style="color: #ddd; font-size: 14px;">KBO</span>
                <span style="color: #ddd; font-size: 14px;">TEAM KOREA</span>
                <div style="width: 35px; height: 35px; background-color: #333; border-radius: 4px; display: flex; justify-content: center; align-items: center; font-weight: bold;">U</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. 메인 화면 (Main Page)
# -----------------------------------------------------------------------------
def render_main_page():
    render_header()
    
    st.markdown('<div class="main-wrapper">', unsafe_allow_html=True)
    
    # [A] 서비스 소개
    st.markdown("""
        <div class="intro-banner">
            <div class="ai-badge">NEXT-GEN ANALYTICS</div>
            <div class="intro-title">
                야구의 흐름을 꿰뚫다,<br>
                <span style="color: #E50914;">BAIS</span> 실시간 AI 해설
            </div>
            <div class="intro-desc">
                단순한 중계는 끝났습니다. 투수의 심리부터 감독의 전술까지.<br>
                지금껏 경험하지 못한 고품격 야구 콘텐츠를 만나보세요.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # [B] 오늘의 추천 영상
    st.markdown('<div class="section-title">🔥추천 하이라이트</div>', unsafe_allow_html=True)
    
    main_video = video_data[0]
    
    col1, col2 = st.columns([1.8, 1.2])
    
    with col1:
        if os.path.exists(main_video['video_path']):
            st.video(main_video['video_path'])
        else:
            st.info(f"⚠️ 영상을 찾을 수 없습니다. ({main_video['video_path']}) 폴더를 확인해주세요.")
            
    with col2:
        st.markdown(f"### {main_video['title']}")
        st.markdown(f"<p style='font-size: 18px; color: #aaa;'>{main_video['desc']}</p>", unsafe_allow_html=True)
        st.markdown("""
            <div style='background-color: #262626; padding: 20px; border-radius: 8px; margin-bottom: 20px; border: 1px solid #333;'>
                <div style='display:flex; align-items:center; gap: 15px; color: #aaa; font-size: 14px; margin-bottom: 15px;'>
                    <span>2025</span>
                    <span style='border: 1px solid #888; padding: 0 4px; font-size: 11px;'>FHD</span>
                    <span>2분 39초</span>
                    <span>AI 해설 Ver.</span>
                </div>
                <p style='color: #e5e5e5; font-size: 15px; line-height: 1.5; margin:0;'>
                    팽팽한 긴장감 속, 승패를 가른 단 한 번의 기회!<br>
                    양 팀 에이스의 자존심을 건 투구와 그라운드를 뜨겁게 달군 슈퍼 플레이까지,<br>
                    6월 10일 경기의 숨 막히는 하이라이트를 생생하게 확인하세요.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        video_url = f"?page=player&view={main_video['id']}"
        st.markdown(f"""
            <a href="{video_url}" target="_self" class="custom-btn" style="display:block; width:100%;">▶ 재생하기</a>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # [C] 추천 리스트
    render_video_list_section()

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# [공통함수] 비디오 리스트 렌더링 (메인 & 플레이어 하단용)
# -----------------------------------------------------------------------------
def render_video_list_section():
    st.markdown('<div class="section-title">📺 지금 뜨는 콘텐츠</div>', unsafe_allow_html=True)
    
    # 버튼 스타일 정의
    st.markdown("""
    <style>
        .custom-btn {
            display: inline-block;
            background-color: #E50914;
            color: white !important;
            padding: 0.5rem 1.5rem;
            border-radius: 4px;
            text-decoration: none;
            font-weight: bold;
            font-size: 16px;
            transition: all 0.3s ease;
            text-align: center;
            border: none;
            cursor: pointer;
        }
        .custom-btn:hover {
            background-color: #ff1f2b;
            transform: scale(1.05);
            box-shadow: 0 0 15px rgba(229, 9, 20, 0.5);
        }
        /* a 태그 기본 스타일 제거 */
        a.custom-btn:visited, a.custom-btn:active, a.custom-btn:link {
            color: white !important;
            text-decoration: none !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    grid_cols = st.columns(3)
    for i, video in enumerate(video_data[1:]):
        col_idx = i % 3
        with grid_cols[col_idx]:
            st.markdown("<div style='margin-bottom: 30px;'>", unsafe_allow_html=True)
            if os.path.exists(video['video_path']):
                st.video(video['video_path'])
            else:
                st.image("https://via.placeholder.com/600x340/141414/FFFFFF/?text=Video+File+Missing", use_column_width=True)
            
            st.markdown(f"<div style='font-weight: bold; font-size: 18px; margin-top: 10px;'>{video['title']}</div>", unsafe_allow_html=True)
            st.caption(video['desc'])
            
            video_url = f"?page=player&view={video['id']}"
            st.markdown(f"""
                <a href="{video_url}" target="_self" class="custom-btn">지금 시청</a>
            """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. 플레이어 화면 (Player Page) - 데이터 기반 채팅 렌더링
# -----------------------------------------------------------------------------
def render_player_page():
    components.html(
        """
            <script>
                window.scrollTo(0, 0);
                window.parent.scrollTo(0, 0);
            </script>
        """, 
        height=0
    )

    render_header()
    video = st.session_state.selected_video
    
    # 말풍선 스타일 CSS (개별 적용을 위해 인라인 클래스 정의)
    st.markdown("""
    <style>
        /* AI 메시지 스타일 */
        .ai-msg {
            background-color: #222;
            color: white;
            padding: 15px;
            border-radius: 15px 15px 15px 2px;
            margin-bottom: 10px;
            font-size: 15px;
            line-height: 1.5;
            border: 1px solid #333;
        }
        /* 캐스터 메시지 스타일 */
        .caster-msg {
            background-color: transparent;
            color: #aaa;
            padding: 5px 10px;
            margin-bottom: 10px;
            font-size: 14px;
            text-align: right;
        }
        /* 메시지 내 이름 스타일 */
        .msg-name-ai {
            font-size: 12px;
            color: #E50914;
            margin-bottom: 5px;
            font-weight: bold;
        }
        .msg-name-caster {
            font-size: 11px;
            color: #666;
            margin-bottom: 2px;
        }
        /* Streamlit 컨테이너 테두리 제거 (선택사항) */
        [data-testid="stVerticalBlockBorderWrapper"] > div {
            border: none !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # --------------------------------------------------
    # [데이터] 채팅 메시지 리스트 (나중에 모델 연동 시 이 리스트만 업데이트하면 됨)
    # --------------------------------------------------
    chat_messages = [
        {
            "role": "caster",
            "text": "채은성 5번타자, 초구를 당겼고 이 타구 3, 유간을 뺐습니다. 플로리얼 달립니다. 홈까지, 홈까지 미끄러져 들어옵니다. 채은성의 적시타. 스코어 2 대 0"
        },
        {
            "role": "ai",
            "text": "예, 채은성 선수가 지금, 어… 정말 본인이 해야, 해야 할 역할을 정확하게 해냈습니다. 초구부터 방망이를, 어… 짧게 가져가면서, 강하게 당겨서 3, 유간을 깨는 그런 타, 타구를 만들어냈거든요. 저도 LA에 있을 때 보면, 어… 5번 타자는 항상 이런 상황에서 “나는 찬스 메이커다”라는 책임이, 책임감이 있어야 했어요. 클린업 뒤를 받쳐주면서도, 득점권에서 어… 확실하게 한 점, 두 점을 만들어주는 역할인데, 지금 채은, 채은성 선수가 딱 그런 모습, 예… 보여주고 있습니다."
        },
        {
            "role": "caster",
            "text": "3구를 밀었습니다. 이 타구는 우중간을 겨낭했습니다. 적시타가 되면서 한 점을 더 벌어들이고있는 한화이글스. 노시환의 적시타."
        },
        {
            "role": "ai",
            "text": "예, 지금 노시환 선수가, 어… 정말 팀 배팅을 보여주고 있습니다. 3구째 공을, 어… 밀어, 밀어치는 모습이었는데요, 힘으로만 잡아당기려는 게 아니라, 상, 상황에 맞게 우중간 방향으로 공을 보내는, 예… 이런 타격이 팀 타선을 더 단단하게 만들어 줍니다. 제가 메이저리그에 있을 때도, 어… 이렇게 점수를 한 번에 몰아서 내기보다는, 지금 한화처럼 한 점, 또 한 점, 예… 차곡차곡 쌓아가는 공격이 상대 투수에게는 더 힘들었.., 어... 부담이 됐거든요."
        },
        {
            "role": "caster",
            "text": "송성문의 타구. 오른쪽 떴습니다. 우익수 움직임 느려지고, 담장을 넘습니다. 송성문 3경기 연속 홈런."
        },
        {
            "role": "ai",
            "text": "예, 지금 타구가 그냥 밀려 나간 게 아니라, 어… 끝까지 방망이가 공을 따라가면서, 오른쪽 담장을 넘기는 그런 스윙이었어요. 우익수가 처음에는 따라, 따라가다가, 어… 점점 발이 느려지는 장면이 나오잖아요, 그게 타구의 힘, 힘과 각도가, 예… 얼마나 좋았는지를 보여주는 모습... 장면입니다. 송성문 선수, 어… 결과적으로 3경기 연속 홈런인데요, 타이밍, 스윙 궤적, 그리고 자신감까지, 예… 전부 올라와 있다는 모습... 장면입니다."
        },
        {
            "role": "caster",
            "text": "오늘 두차례 출루. 노시환 4번타자. 변화구. 스윙 삼진. 원아웃."
        },
        {
            "role": "ai",
            "text": "예, 지금 이 타석에서는 노시환 선수가, 어… 완전히 속었습니다. 앞선 타석들에서 계속 로케이션을 직, 직구, 슬라이더 위주의 승부를 보다가, 어… 전혀 보여주지 않았던 커브가 갑자기 스트라이크 존으로 들어오니까, 머리로는 스윙을 멈추고 싶은데, 그… 몸은 이미 나가 있는 그런 장면이었어요. 제가 메이저리그에 있을 때도, 어… 타, 타자들이 잘 맞고 있을 때일수록 일부러 이렇게 한 번은 완전히 다른 구종을 섞어 줍니다 “오늘은 이 공 안 쓰네?” 하다가, 결정적인 카운트에서 딱 한 번 꺼내는 커브에, 예… 타자들이 많이 속아요."
        },
    ]

    # 여백 래퍼
    st.markdown('<div class="main-wrapper">', unsafe_allow_html=True)

    # 레이아웃
    p_col1, p_col2 = st.columns([2.3, 1])

    # [왼쪽] 영상 및 상세 정보
    with p_col1:
        if os.path.exists(video['video_path']):
            st.video(video['video_path'], autoplay=True)
        else:
            st.markdown(
                f"""
                <div style="width:100%; height:450px; background-color:#000; display:flex; justify-content:center; align-items:center; border-radius:12px;">
                    <p style='color:white;'>🚫 영상 파일을 찾을 수 없습니다.<br>({video['video_path']})</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
        st.markdown(
            f"""
            <div style="margin-top: 15px;">
                <h3 style="font-size: 24px; font-weight: bold; margin-bottom: 10px; color: white;">{video['title']}</h3>
                <div style="display: flex; align-items: center; justify-content: space-between; color: #aaa; font-size: 14px; margin-bottom: 15px; border-bottom: 1px solid #333; padding-bottom: 15px;">
                    <div style="display: flex; gap: 15px;">
                        <span style="display: flex; align-items: center;">👤 BAIS Official</span>
                        <span>•</span>
                        <span>{video['desc']}</span>
                    </div>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )

    # [오른쪽] 실시간 채팅창 (반복문 렌더링 방식)
    with p_col2:
        # 헤더
        st.markdown(
            """
            <div style="display: flex; justify-content: flex-end; margin-bottom: 10px; padding-right: 10px;">
                <span style="background-color: rgba(229, 9, 20, 0.1); color: #E50914; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; display: flex; align-items: center; gap: 5px;">
                    <span style="width: 8px; height: 8px; background-color: #E50914; border-radius: 50%;"></span> LIVE
                </span>

            </div>
            """, 
            unsafe_allow_html=True
        )
        
        with st.container(height=600, border=False):
            for msg in chat_messages:
                if msg["role"] == "ai":
                    # AI 메시지 DIV
                    st.markdown(f"""
                        <div class="ai-msg">
                            <div class="msg-name-ai">🎙️ BAIS 해설</div>
                            {msg['text']}
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    # 캐스터 메시지 DIV
                    st.markdown(f"""
                        <div class="caster-msg">
                            <div class="msg-name-caster">👤 캐스터</div>
                            {msg['text']}
                        </div>
                    """, unsafe_allow_html=True)

    st.markdown("---")
    
    # [하단] 추천 리스트
    render_video_list_section()

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. 앱 실행 라우터
# -----------------------------------------------------------------------------
if st.session_state.page == 'main':
    render_main_page()
else:
    render_player_page()