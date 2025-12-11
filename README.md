# SKN17-FINAL-3Team
> 주제 : 인공지능 인플루언서 <br>
> 프로젝트 기간: 25.10.28 - 25.12.18
<br>

#  팀 소개

### 팀명: ⚾TEAM BASIS⚾

### 팀원 소개
<table>
  <tbody>
    <tr>
      <td align="center" width="16%"><b>김민균</b></td>
      <td align="center" width="16%"><b>김준협</b></td>
      <td align="center" width="16%"><b>박민정</b></td>
      <td align="center" width="16%"><b>이민영</b></td>
      <td align="center" width="16%"><b>정의중</b></td>
      <td align="center" width="16%"><b>조세희</b></td>
    </tr>
    <tr>
      <td align="center">
        <img width="140" alt="Image" src="https://github.com/user-attachments/assets/7b43b853-addd-4bb1-a7b3-26e695742f31" />
      </td>
      <td align="center">
        <img width="140" alt="Image" src="https://github.com/user-attachments/assets/7e191d94-7885-4c5c-8239-2681f5781c81" />
      </td>
      <td align="center">
        <img width="140" alt="Image" src="https://github.com/user-attachments/assets/f991d5d3-20d6-4939-9273-cc7772ea6233" />
      </td>
      <td align="center">
        <img width="140" alt="Image" src="https://github.com/user-attachments/assets/d574f00a-b6a8-4e92-aadb-d4c6c8d69d36" />
      </td>
      <td align="center">
        <img width="140" alt="Image" src="https://github.com/user-attachments/assets/4c6208e1-ce36-4495-8f32-b23abc83e002" />
      </td>
      <td align="center">
        <img width="140" alt="Image" src="https://github.com/user-attachments/assets/257e214f-7842-476f-b910-c48b9fadacc4" />
      </td>
    </tr>
    <tr>
      <td align="center"><a href="https://github.com/alswhitetiger">@alswhitetiger</a></td>
      <td align="center"><a href="https://github.com/use08168">@use08168</a></td>
      <td align="center"><a href="https://github.com/minjeon">@minjeon</a></td>
      <td align="center"><a href="https://github.com/mylee99125">@mylee99125</a></td>
      <td align="center"><a href="https://github.com/uii42">@uii42</a></td>
      <td align="center"><a href="https://github.com/SEHEE-8546">@SEHEE-8546</a></td>
    </tr>
  </tbody>
</table>

<br>

# 목차
- [1. 프로젝트 개요](#1-프로젝트-개요)
- [2. 프로젝트 기획](#2-프로젝트-기획)
- [3. 기술 스택](#3-기술-스택)
- [4. 시스템 아키텍처](#4-시스템-아키텍처)
- [5. 기능 및 화면 설계](#5-기능-및-화면-설계)
- [6. 데이터 설계](#6-데이터-설계)
- [7. AI 설계](#7-ai-설계)
- [8. 결론](#8-결론)
- [9. 개선 및 향후 개발 필요](#9-개선-및-향후-개발-필요)
- [10. 회고](#10-회고)
 

<br>
<br>

# 1. 프로젝트 개요

### 프로젝트 명
**⚾B<span>$\textsf{\color{red}AI}$</span>S⚾**
> BASEBALL AI SELECT 

**“편파 해설 없이, 야구를 더 쉽게”**

**BAIS** 은 편파 중계 없는 AI 해설위원과 야구 초보자들을 위해 어려운 야구 용어, 복잡한 야구 규칙을 좀 더 쉽게 풀어서 설명해주는 해설을 제공합니다. 

 <br>
 
## 프로젝트 배경
<br>

### 1. 프로 야구 입문 장벽
<p align="center">
<img width="730" height="662" alt="Image" src="https://github.com/user-attachments/assets/f69ccfd2-44bd-4e73-bf5d-bfcc30d14f00" /> </p>
[출처 : <a href="https://www.civicnews.com/news/articleView.html?idxno=34373">영어 약자로 된 야구 용어 남발...신규 야구 팬 유입 막는 걸림돌 될 수 있어</a>]


<br>
<br>

- 프로 야구에 관심이 있지만 어려운 야구 용어와 복잡한 야구 규칙으로 입문 어렵

<br>

<table>  
  <tbody>
   <tr>
      <td> <img width="978" height="447" alt="Image" src="https://github.com/user-attachments/assets/e0b93f1e-5c9c-4cd5-b011-e5064b599836" /> </td>
      <td> <img width="1125" height="616" alt="Image" src="https://github.com/user-attachments/assets/7d897f73-84d5-4135-8b20-62aed1143590" /> </td>
    </tr>
  </tbody>
</table>
[출처:2025년 Team BASIS 자체 설문조사(Google Forms, n=65)]


<br>
<br>

- 설문 조사 결과, 야구 입문 장벽의 이유로 **어려운 용어**와 **복잡한 규칙**이 제일 큰 비중을 차지
- 해설위원에게 바라는 점으로 **초보자들도 이해하기 쉽게 풀어서 설명해줬으면 좋겠다**는 답변 다수 


<br>

### 2. 해설위원의 역할

<p align="center">
<img width="660" height="627" alt="Image" src="https://github.com/user-attachments/assets/b6f9a938-bac6-4d97-b61e-e4b64b0ac7dd" /> </p>
[출처 : <a href="https://sports.news.nate.com/view/20250513n02348">영어 수준 떨어지는 야구해설, 언제까지 참고 들어야 하나</a>]


<br>
<br>

- 해설위원의 역할은 경기 이해도와 몰입도를 높이는데 효과적
- 팬 맞춤 해설에 대한 욕구 증가
- 하지만, 수준 떨어지는 해설에 대한 불만 끊임없이 야기

<br>

<img width="947" height="422" alt="Image" src="https://github.com/user-attachments/assets/fa637358-3d14-4887-8cc5-9cce560a0dfd" /> <br>
[출처:2025년 Team BASIS 자체 설문조사(Google Forms, n=65)]
 

<br>

- 설문조사 결과, 해설위원에게 바라는 점으로 **해설위원의 편파 중계에 대한 불만** 다수 존재 

<br>

## 프로젝트 필요성
<table>  
  <tbody>
   <tr>
      <td> <img width="1311" height="625" alt="Image" src="https://github.com/user-attachments/assets/15372a44-43b7-42f4-8801-a20279996feb" /> </td>
    </tr>
  </tbody>
</table>
[출처:2025년 Team BASIS 자체 설문조사(Google Forms, n=65)]


<br>
<br>

- 국내외에 AI 해설과 관련된 서비스 전무
- 설문조사 결과 서비스를 이용할 의향이 약 70%로 과반수 차지

**➡️ 야구 입문자와 오랜 팬들 모두를 위해 필요한 서비스임을 확인**

<br>

## 프로젝트 목표

🔸**대상** : 야구 입문자 및 기존 야구 시청자 <br>
🔸**내용** : 입문자에게는 야구에 대한 룰이나 상식을 상세히 설명을 해주며 기존 시청자에게는 편파 없는 몰입도 높은 해설 서비스 제공 <br> 
🔸**수단** : 웹 서비스 <br>

➡️ 웹 기반 야구 해설 서비스를 통해 야구 입문자에게는 경기 규칙과 기본 용어·상식을 직관적으로 이해할 수 있는 설명 기능을 제공하고, 기존 야구 시청자에게는 다양한 화법과 관전 포인트를 활용한 재미있고 차별화된 캐스터·해설 경험을 제공


<br>

#  2. 프로젝트 기획

## 📆WBS
<img width="1543" height="782" alt="Image" src="https://github.com/user-attachments/assets/e162d2a9-843c-47f0-a249-082c4115d9f5" />

[WBS 바로가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-FINAL-3Team/blob/main/01_docs/1.WBS.pdf)

<br>

## 📁프로젝트 기획서 
<img width="752" height="522" alt="Image" src="https://github.com/user-attachments/assets/f1953d63-886e-4220-8843-13c78abd9510" />
<img width="735" height="502" alt="Image" src="https://github.com/user-attachments/assets/99ca19b5-b7df-4243-b97a-d532c7772663" />
<img width="731" height="490" alt="Image" src="https://github.com/user-attachments/assets/6d226f6c-55cd-4a84-ae1d-0cd3a333fe51" />


[프로젝트 기획서 바로가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-FINAL-3Team/blob/main/01_docs/2.%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EA%B8%B0%ED%9A%8D%EC%84%9C.pdf)

<br>

## 🗂️요구사항 정의서 
<img width="1723" height="658" alt="Image" src="https://github.com/user-attachments/assets/233928a4-362b-4909-8b21-b356848dba69" />
<img width="1723" height="521" alt="Image" src="https://github.com/user-attachments/assets/426a10dd-6582-41cd-94ef-d519070e928b" />

[요구사항 정의서 바로가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-FINAL-3Team/blob/main/01_docs/3.%20%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD%20%EC%A0%95%EC%9D%98%EC%84%9C.pdf)

<br>
<br>

# 3. 기술 스택

### 💻 핵심 개발 및 AI/ML 스택
| 카테고리 | 기술 스택 |
|----------|-------------------------------------------|
| **사용 언어** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white) |
| **웹 프레임워크** | ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white) |
| **LLM / VLM** | ![KAKAOCORP/kanana-1.5-8b-instruct](https://img.shields.io/badge/kakaocorp/kanana--1.5--8b--instruct-2505-FFB000?style=for-the-badge&logo=HuggingFace&logoColor=white) ![Qwen3-VL-4B-Instruct](https://img.shields.io/badge/Qwen%2FQwen3--VL--4B--Instruct-000000?style=for-the-badge&logo=AlibabaCloud&logoColor=white) |
| **음성 인식 및 화자 분리 (STT)** | ![Google Cloud Speech-to-Text](https://img.shields.io/badge/CHIRP%203-4285F4?style=for-the-badge&logo=Google-cloud&logoColor=white) ![TELEPHONY STT](https://img.shields.io/badge/TELEPHONY%20STT-000000?style=for-the-badge&logo=Twilio&logoColor=white) ![Clova Speech](https://img.shields.io/badge/Clova%20Speech-03C75A?style=for-the-badge&logo=Naver&logoColor=white) |
| **음성 합성 (TTS)** | ![Google Cloud Text-to-Speech](https://img.shields.io/badge/Fish%20Audio-DB4437?style=for-the-badge&logo=Google-cloud&logoColor=white) |
| **벡터 데이터베이스** | ![FAISS](https://img.shields.io/badge/FAISS-009688?style=for-the-badge&logo=Facebook&logoColor=white) |
| **임베딩 모델** | ![nlpai-lab/KURE-v1](https://img.shields.io/badge/nlpai--lab%2FKURE--v1-8C9E90?style=for-the-badge&logo=HuggingFace&logoColor=white) |
| **모델 튜닝 / 학습 프레임워크** | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white) ![Transformers](https://img.shields.io/badge/Transformers-FFCC00?style=for-the-badge&logo=HuggingFace&logoColor=black) ![QLoRA](https://img.shields.io/badge/QLoRA-F76D57?style=for-the-badge&logo=HuggingFace&logoColor=white) |

### 🌐 프론트엔드 및 인프라/배포
| 카테고리 | 기술 스택 |
|----------|-------------------------------------------|
| **UI / 프론트엔드** | <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> |
| **실행 환경** | ![RunPod](https://img.shields.io/badge/RunPod-FF4500?style=for-the-badge&logo=Render&logoColor=white) ![AWS EC2](https://img.shields.io/badge/AWS%20EC2-FF9900?style=for-the-badge&logo=Amazon%20AWS&logoColor=white) |
| **배포 및 컨테이너** | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white) ![Docker Compose](https://img.shields.io/badge/Docker--Compose-1488C6?style=for-the-badge&logo=Docker&logoColor=white) |
| **DB / Storage** | ![Amazon RDS](https://img.shields.io/badge/Amazon%20RDS-527FFF?style=for-the-badge&logo=amazonrds&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white) ![Amazon S3](https://img.shields.io/badge/Amazon%20S3-232F3E?style=for-the-badge&logo=amazons3&logoColor=white) |
| **서버** | ![nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) ![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=Gunicorn&logoColor=white) |


### 🤝 협업 및 기타
| 카테고리 | 기술 스택 |
|----------|-------------------------------------------|
| **형상 관리 / 협업** | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white) ![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=Google%20Drive&logoColor=white) |
| **테스트** | ![Pytest](https://img.shields.io/badge/pytest-ffffff?style=for-the-badge&logo=pytest&logoColor=2f9fe3) |
| **개발환경** | ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white) |



<br>

# 4. 시스템 아키텍처

### 4.1 시스템 아키텍처
<img width="962" height="546" alt="Image" src="https://github.com/user-attachments/assets/88ee2ba1-8561-401c-8681-9684f80d160d" />

<br>

### 4.2 주요 서비스 플로우


<br>
<br>


# 5. 기능 및 화면 설계


### 5.1 시나리오 설계

<details>
 <summary>회원 정보 관리</summary>
 <img width="1188" height="706" alt="Image" src="https://github.com/user-attachments/assets/31be7950-d341-421c-800c-42be1580b8b5" />
 <br>
 <img width="1192" height="622" alt="Image" src="https://github.com/user-attachments/assets/9429bb56-583e-4e69-af3c-96fb43a270a3" />
 <br>
 <img width="1192" height="572" alt="Image" src="https://github.com/user-attachments/assets/a89cf5be-74bd-4c0d-b69b-60318aa4e866" />
</details>

<details>
 <summary>선호 구단 선택</summary>
 <img width="1192" height="781" alt="Image" src="https://github.com/user-attachments/assets/aa10371a-db0d-48fe-8d0b-30fd7503b8ee" />
</details>

<details>
 <summary>구독</summary>
 <img width="996" height="777" alt="Image" src="https://github.com/user-attachments/assets/91f6217e-0b73-4e09-bc14-c26525b591bf" />
</details>

<details>
 <summary>영상 시청</summary>
 <img width="992" height="536" alt="Image" src="https://github.com/user-attachments/assets/aa96e0a1-2d2b-4059-a38a-afe1531ff0b5" />
 <br>
 <img width="998" height="457" alt="Image" src="https://github.com/user-attachments/assets/677f9571-d2de-4a7b-99c9-5b96862cdd67" />
</details>

[시나리오 설계서 바로가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-FINAL-3Team/blob/main/01_docs/4.%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4%20%EC%84%A4%EA%B3%84%EC%84%9C.pdf)

<br>

### 5.2 화면 설계

<details>
 <summary>화면 설계서</summary>
 <img width="1320" height="737" alt="Image" src="https://github.com/user-attachments/assets/3ca73a94-0e10-4dbb-b16a-cf464b5ad0bd" />
 <img width="1323" height="741" alt="Image" src="https://github.com/user-attachments/assets/6930c355-c158-450a-ac7f-531c95a3b0c3" />
 <img width="1325" height="745" alt="Image" src="https://github.com/user-attachments/assets/4ef80114-b26c-4584-9aef-6100ae65e3b4" />
 <img width="1317" height="737" alt="Image" src="https://github.com/user-attachments/assets/a68b8234-4b6d-4e62-9d70-c39ce66c2339" />

</details>

[화면설계서 자세히 보러가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-FINAL-3Team/blob/main/01_docs/5.%ED%99%94%EB%A9%B4%EC%84%A4%EA%B3%84%EC%84%9C.pdf)

<br>
<br>

# 6. 데이터 설계


**[ERD]**
<img width="1792" height="868" alt="Image" src="https://github.com/user-attachments/assets/cad13f02-9bd8-4b51-851e-10b0f4a8ffb0" />


<details>
 <summary>데이터 전처리 결과서 </summary>

[RAG 데이터 전처리 결과서 자세히 보러가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-FINAL-3Team/blob/main/01_docs/6.RAG%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A0%84%EC%B2%98%EB%A6%AC%20%EA%B2%B0%EA%B3%BC%EC%84%9C.pdf)

[파인튜닝 데이터 전처리 결과서 자세히 보러가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-FINAL-3Team/blob/main/01_docs/7.%ED%8C%8C%EC%9D%B8%ED%8A%9C%EB%8B%9D%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A0%84%EC%B2%98%EB%A6%AC%20%EA%B2%B0%EA%B3%BC%EC%84%9C.pdf)

</details>

<br>
<br>

#  7. AI 설계


<details>
 <summary>모델 테스트 계획 및 결과</summary> 

### <테스트 정보>
<img width="430" height="780" alt="Image" src="https://github.com/user-attachments/assets/47e99307-9f07-46df-a012-a02730596ca5" />
   
<br>
   
### <테스트 결과>
<img width="433" height="863" alt="Image" src="https://github.com/user-attachments/assets/76d26be9-c2fa-475d-87ed-cd3f47941877" /> <br>
<img width="421" height="921" alt="Image" src="https://github.com/user-attachments/assets/9e717c17-ee2a-4a1e-aede-5cec33690de9" /> <br>
<img width="563" height="310" alt="Image" src="https://github.com/user-attachments/assets/4c0d9924-a394-4565-ad48-3340ce187b4b" />


</details>

[모델 테스트 계획 및 결과 보고서 자세히 보러가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-FINAL-3Team/blob/main/01_docs/8.%EB%AA%A8%EB%8D%B8%20%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EA%B3%84%ED%9A%8D%20%EB%B0%8F%20%EA%B2%B0%EA%B3%BC%20%EB%B3%B4%EA%B3%A0%EC%84%9C.pdf)


<br>

<details>
 <summary>AI 학습 결과</summary>
 <img width="748" height="506" alt="Image" src="https://github.com/user-attachments/assets/339033fb-38fe-4d3a-bada-cd0313642c19" /> <br>
 <img width="742" height="510" alt="Image" src="https://github.com/user-attachments/assets/a43faae5-c68c-4984-af99-68e01a55dc88" /> <br>
 <img width="745" height="506" alt="Image" src="https://github.com/user-attachments/assets/f013556b-616b-45fe-b477-a2c3b86641de" /> <br>
 <img width="355" height="322" alt="Image" src="https://github.com/user-attachments/assets/adb10f76-b2f6-4db3-9c6e-562718bbb34f" />
 
</details>

[인공지능 학습 결과서 자세히 보기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-FINAL-3Team/blob/main/01_docs/9.%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%ED%95%99%EC%8A%B5%20%EA%B2%B0%EA%B3%BC%EC%84%9C.pdf)

<br>

<details>
 <summary>시스템 테스트 계획 및 결과</summary> 

### <테스트 정보>

<br>
   
### <테스트 결과>

</details>

[시스템 테스트 계획 및 결과 보고서 자세히 보러가기 (PDF)]()

<br>
<br>

#  8. 결론

## 시연 영상

**[메인 플로우]**  
- 회원 가입 > 구독 > 하이라이트 영상 선택 > 해설위원 선택 > 영상 시청  


<br>

**[사용자 영상 업로드]**
- 로그인 > 홈 > 내 영상 시청 > 업로드 > 업로드 영상 시청 <br>
- 사용자 로컬의 MP4 파일을 업로드 해 해설위원을 선택하면 선택한 해설위원이 입혀진 영상 시청 가능 <br>
- 유료 플랜 구독 시에만 가능 (BASIC/PREMIUM)


<br>

<br>

## 결과 및 사용자 피드백
**[사용자 테스트 설문 결과]**

![image](https://github.com/user-attachments/assets/d937af9d-45cc-429e-9250-340adee14b28)


**[평가]**

![9기_2팀_최종PPT pptx (10)](https://github.com/user-attachments/assets/79a8810e-f80f-4dec-8af3-648d152ce795)


**[기대 효과]**

![9기_2팀_최종PPT pptx (11)](https://github.com/user-attachments/assets/5c1836a7-8fd5-43a9-bf0b-ca08b4bdc531)


**[확장 가능성]**

![9기_2팀_최종PPT pptx (12)](https://github.com/user-attachments/assets/2b924d7e-67c9-4aae-a3d4-a8b1adc40773)



<br>
<br>

# 9. 개선 및 향후 개발 필요

### 1) 사용자 경험(UX) 고도화
- 사용자의 선호 구단에 맞춘 편파 해설 ON/OFF 기능 제공
  - 팬 성향을 반영한 개인화된 해설 기능
- 사용자가 의견을 공유하고 실시간으로 상호작용할 수 있도록 커뮤니티/댓글 기능 도입
- 다양한 개성과 전문성을 가진 AI 해설 페르소나 추가로 사용자 선택지 확대

### 2) 실시간성과 멀티모달 능력 강화
- 실시간 경기 스트리밍과 연동된 즉시 해설 기능 구현
- 텍스트에 의존하지 않고 영상 기반 모션 인식(ODAR)을 적용하여 경기 상황을 직접 파악하고 해설에 반영하는 멀티모달 시스템 개발
- 여러 사용자가 동시에 영상을 업로드할 때를 대비한 트래픽 관리 및 처리 병렬화 최적화 

### 3) 서비스 확장성 강화
- 야구 외에도 다른 스포츠(축구, 농구, 배구 등)로 확장 가능한 구조 설계
- 현재는 MP4파일만 업로드 가능 → MP4 외의 다양한 영상 포맷 및 주요 플랫폼 URL 지원
- 해외 사용자 확대를 위해 다국어 해설 기능 지원 

### 4) 모델 및 데이터 품질 강화
- 최신 경기 기록/선수 정보를 기반으로 정기적,자동화된 데이터 업데이트 체계 구축
- RAG 및 Fine-tuning 데이터셋을 더 풍부하게 구성
  - 다양한 문맥, 비유, 실전 해설 스타일 포함
- 인간 해설에 가까운 자연스러운 억양, 호흡, 감정 표현

### 5) 서비스 안정성 및 확장성 구축
- 실시간 중계 연동 시 필요한 대규모 트래픽 처리 구조 확립
- 멀티모달 기능을 위한 GPU 리소스 최적화 및 인프라 개선
- AWS S3에 영상 저장 시 영상 압축 후 저장 
  - 사용자가 영상을 시청할 때 영상 압축 해제 및 스트리밍 최적화 

### 6) 결제 및 수익화 시스템 개선
- 카카오페이만 가능한 현재의 결제 수단 → 네이버페이, 카드 결제 등 결제 수단 다양화 
- 유료 버전에 경기 분석 리포츠 제공 등 부가 서비스 확장 



# 10. 회고

| 이름 | 회고록 |
|----------|-------------------------------------------|
| **김민균** | 우와 |
| **김준협** | 오 |
| **박민정** | 예 |
| **이민영** | 음 |
| **정의중** | 아 |
| **조세희** | 와우 |