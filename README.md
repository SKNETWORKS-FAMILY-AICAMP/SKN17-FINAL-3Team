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
    <br>
      <td align=center><b>김민균</b></td>
      <td align=center><b>김준협</b></td>
      <td align=center><b>박민정</b></td>
      <td align=center><b>이민영</b></td>
      <td align=center><b>정의중</b></td>
      <td align=center><b>조세희</b></td>
    </tr>
    <tr>
      <td align="center">
          <img alt="Image" src="https://github.com/user-attachments/assets/6388e59a-e07b-4bf0-add1-b02155c4823a" width="200px;" alt="김민균"/>
      <td align="center">
          <img alt="Image" src="https://github.com/user-attachments/assets/4cac2da3-8cbe-41d0-b380-cfe1a1d36792" width="200px;" alt="김준협"/>
      </td>
      <td align="center">
        <img alt="Image" src="https://github.com/user-attachments/assets/4aa26058-5332-480d-83e0-16ae9d5afa44" width="200px;"alt="박민정" />
      </td>
      <td align="center">
        <img alt="Image" src="https://github.com/user-attachments/assets/c04c8959-5265-4bd4-9c7c-782f0d63d147" width="200px;" alt="이민영"/>
      </td>
       <td align="center">
        <img alt="Image" src="https://github.com/user-attachments/assets/568d6707-31a3-4095-b6bd-8b7fab0b1d36" width="200px;" alt="정의중"/>
      </td>
      <td align="center">
        <img alt="Image" src="https://github.com/user-attachments/assets/568d6707-31a3-4095-b6bd-8b7fab0b1d36" width="200px;" alt="조세희"/>
      </td>
      </tr>
    <tr>
      <td><a href="https://github.com/alswhitetiger"><div align=center>김민균</div></a></td>
      <td><a href="https://github.com/use08168"><div align=center>김준협</div></a></td>
      <td><a href="https://github.com/minjeon"><div align=center>박민정</div></a></td>
      <td><a href="https://github.com/mylee99125"><div align=center>이민영</div></a></td>
      <td><a href="https://github.com/uii42"><div align=center>정의중</div></a></td>
      <td><a href="https://github.com/SEHEE-8546"><div align=center>조세희</div></a></td>
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
- [7. AI-설계](#7-ai-설계)
- [8. 결론](#8-결론)
- [9. 향후 계획 및 보완점](#9-향후-계획-및-보완점)
- [10. 회고](#10-회고)
 

<br>
<br>

# 1. 프로젝트 개요

### 프로젝트 명
**⚾B<span style="color:red;">AI</span>S⚾**
> BASEBALL AI SELECT 

**“편파 해설 없이, 야구를 더 쉽게”**

**BAIS** 은 편파 중계 없는 AI 해설위원과 야구 초보자들을 위해 어려운 야구 용어, 복잡한 야구 규칙을 좀 더 쉽게 풀어서 설명해주는 해설을 제공합니다. 

 <br>
 
## 프로젝트 배경
<table>  
  <tbody>
   <tr>
      <td> <img alt="Image" src="https://github.com/user-attachments/assets/e880d887-75e4-4579-a0dd-f093c8384af7"> </td>
      <td> <img alt="Image" src="https://github.com/user-attachments/assets/12a3fd04-3e0c-4982-a7d3-2118d1676ead"> </td>
    </tr>
  </tbody>
</table>  


**1. 프로 야구 입문 장벽**
- 프로 야구에 관심이 있지만 어려운 야구 용어와 복잡한 야구 규칙으로 입문 어렵
- 설문 조사 결과, 야구 입문 장벽의 이유로 **어려운 용어**와 **복잡한 규칙**이 제일 큰 비중을 차지
- 해설위원에게 바라는 점으로 **초보자들도 이해하기 쉽게 풀어서 설명해줬으면 좋겠다**는 답변 다수 


<br>

<table>  
  <tbody>
   <tr>
      <td> <img alt="Image" src="https://github.com/user-attachments/assets/e880d887-75e4-4579-a0dd-f093c8384af7"> </td>
      <td> <img alt="Image" src="https://github.com/user-attachments/assets/12a3fd04-3e0c-4982-a7d3-2118d1676ead"> </td>
    </tr>
  </tbody>
</table>  


**2. 해설위원의 역할**
- 해설위원의 역할은 경기 이해도와 몰입도를 높이는데 효과적
- 팬 맞춤 해설에 대한 욕구 증가
- 하지만, 수준 떨어지는 해설에 대한 불만 끊임없이 야기
- 설문조사 결과, 해설위원에게 바라는 점으로 **해설위원의 편파 중계에 대한 불만** 다수 존재 

<br>

## 프로젝트 필요성
<table>  
  <tbody>
   <tr>
      <td> <img alt="Image" src="https://github.com/user-attachments/assets/b975715c-e7d0-4217-b708-6df43a59093a" width="500px;" /> </td>
    </tr>
  </tbody>
</table>  

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

### WBS
![image](https://github.com/user-attachments/assets/5c2b0f10-e901-4541-9090-600982fafccd)

<details>
 <summary>WBS 바로가기</summary>

 [WBS 바로가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-FINAL-3Team/blob/main/01_docs/WBS.pdf)

</details>

<br>

### 프로젝트 기획서 
![image](https://github.com/user-attachments/assets/5c2b0f10-e901-4541-9090-600982fafccd)

<details>
 <summary>프로젝트 기획서 바로가기</summary>

 [프로젝트 기획서 바로가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-FINAL-3Team/blob/main/01_docs/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EA%B8%B0%ED%9A%8D%EC%84%9C.pdf)

</details>

<br>

### 요구사항 정의서 
![image](https://github.com/user-attachments/assets/5c2b0f10-e901-4541-9090-600982fafccd)

<details>
 <summary>요구사항 정의서 바로가기</summary>

 [요구사항 바로가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-FINAL-3Team/blob/main/01_docs/WBS.pdf)

</details>

<br>
<br>

# 3. 기술 스택

| 카테고리 | 기술 스택 |
|----------|-------------------------------------------|
| **사용 언어** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white) |
| **프레임워크** | ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white) |
| **LLM / VLM** | ![KAKAOCORP/kanana-1.5-8b-instruct](https://img.shields.io/badge/kakaocorp/kanana--1.5--8b--instruct-2505-FFB000?style=for-the-badge&logo=HuggingFace&logoColor=white) ![Qwen](https://img.shields.io/badge/Qwen-005F73?style=for-the-badge&logo=HuggingFace&logoColor=white) |
| **STT** | ![Google Cloud Speech-to-Text](https://img.shields.io/badge/CHIRP%203-4285F4?style=for-the-badge&logo=Google-cloud&logoColor=white) ![TELEPHONY STT](https://img.shields.io/badge/TELEPHONY%20STT-000000?style=for-the-badge&logo=Twilio&logoColor=white) |
| **TTS** | ![Google Cloud Text-to-Speech](https://img.shields.io/badge/Fish%20Audio-DB4437?style=for-the-badge&logo=Google-cloud&logoColor=white) |
| **벡터 데이터베이스** | ![FAISS](https://img.shields.io/badge/FAISS-009688?style=for-the-badge&logo=Facebook&logoColor=white) |
| **임베딩 모델** | ![nlpai-lab/KURE-v1](https://img.shields.io/badge/nlpai--lab%2FKURE--v1-8C9E90?style=for-the-badge&logo=HuggingFace&logoColor=white) |
| **모델 튜닝 / 학습 프레임워크** | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white) ![Transformers](https://img.shields.io/badge/Transformers-FFCC00?style=for-the-badge&logo=HuggingFace&logoColor=black) ![LoRA](https://img.shields.io/badge/LoRA-F76D57?style=for-the-badge&logo=HuggingFace&logoColor=white) |
| **UI / 프론트엔드** | <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> |
| **실행 환경** | ![RunPod](https://img.shields.io/badge/RunPod-FF4500?style=for-the-badge&logo=Render&logoColor=white) ![AWS EC2](https://img.shields.io/badge/AWS%20EC2-FF9900?style=for-the-badge&logo=Amazon%20AWS&logoColor=white) |
| **배포 및 컨테이너** | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white) ![Docker Compose](https://img.shields.io/badge/Docker--Compose-1488C6?style=for-the-badge&logo=Docker&logoColor=white) |
| **DB 및 기타** | ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white) ![Amazon S3](https://img.shields.io/badge/Amazon%20S3-232F3E?style=for-the-badge&logo=amazons3&logoColor=white) ![Amazon RDS](https://img.shields.io/badge/Amazon%20RDS-527FFF?style=for-the-badge&logo=amazonrds&logoColor=white) |
| **형상 관리 / 협업** | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white) ![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=Google%20Drive&logoColor=white) |
| **테스트** | ![Pytest](https://img.shields.io/badge/pytest-ffffff?style=for-the-badge&logo=pytest&logoColor=2f9fe3) |
| **개발환경** | ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white) |


<br>

# 4. 시스템 아키텍처

### 4.1 시스템 아키텍처
![시스템 아키텍처](image.png)
<br>

### 4.2 주요 서비스 플로우


<br>
<br>


# 5. 기능 및 화면 설계


### 5.1 시나리오 설계

[시나리오 설계서 바로가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN17-FINAL-3Team/blob/main/01_docs/WBS.pdf)

<details>
 <summary>회원 정보 관리</summary>
 

</details>

<details>
 <summary>선호 구단 선택</summary>
 

</details>

<details>
 <summary>구독</summary>
 

</details>

<details>
 <summary>영상 시청</summary>


</details>

<br>

### 5.2 화면 설계

[화면설계서 자세히 보러가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-FINAL-2Team/blob/main/docs/9%EA%B8%B0-2%ED%8C%80_%ED%99%94%EB%A9%B4%20%EC%84%A4%EA%B3%84%EC%84%9C.pdf)

<details>
 <summary>화면 설계서</summary>

</details>

<br>
<br>

# 6. 데이터 설계


**[ERD]**
![ERD](image-1.png)


<details>
 <summary>데이터 전처리 결과서 </summary>
 

</details>

[데이터 전처리 결과서 자세히 보러가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-FINAL-2Team/blob/main/docs/9%EA%B8%B0-2%ED%8C%80_%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%A0%84%EC%B2%98%EB%A6%AC-%EA%B2%B0%EA%B3%BC%EC%84%9C.pdf)

<br>
<br>

#  7. AI 설계


<details>
 <summary>모델 테스트 계획 및 결과보고서 </summary> 

### <테스트 정보>
   


<br>
   
### <테스트 결과>


</details>

[모델 테스트 계획 및 결과 보고서 자세히 보러가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-FINAL-2Team/blob/main/docs/9%EA%B8%B0-2%ED%8C%80_%EB%AA%A8%EB%8D%B8%20%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EA%B3%84%ED%9A%8D%20%EB%B0%8F%20%EA%B2%B0%EA%B3%BC%20%EB%B3%B4%EA%B3%A0%EC%84%9C.pdf)


<br>

<details>
 <summary>AI 학습 결과서</summary>
 


</details>

[인공지능 학습 결과서 자세히 보기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-FINAL-2Team/blob/main/docs/9%EA%B8%B0-2%ED%8C%80_%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%ED%95%99%EC%8A%B5%20%EA%B2%B0%EA%B3%BC%EC%84%9C.pdf)

<br>

<details>
 <summary>시스템 테스트 계획 및 결과보고서 </summary> 

### <테스트 정보>



<br>
   
### <테스트 결과>


</details>

[시스템 테스트 계획 및 결과 보고서 자세히 보러가기 (PDF)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-FINAL-2Team/blob/main/docs/9%EA%B8%B0-2%ED%8C%80_%EC%8B%9C%EC%8A%A4%ED%85%9C%20%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EA%B3%84%ED%9A%8D%20%EB%B0%8F%20%EA%B2%B0%EA%B3%BC%EC%84%9C.pdf)

<br>
<br>

#  8. 결론

## 시연 영상

**[메인 플로우]**  
- 회원 가입 > 구독 > 하이라이트 영상 시청 


<br>

**[사용자 영상 업로드]**
- 로그인 > 홈 > 내 영상 시청 > 업로드 > 업로드 영상 시청 <br>
- 사용자 로컬의 MP4 파일을 업로드 해 해설위원을 선택하면 선택한 해설위원이 입혀진 영상 시청 가능 <br>
- 유료 플랜 구독 시에만 가능 (BASIC/PREMIUM)


<br>

<br>

## 결과 및 사용자 피드백
[사용자 테스트 설문 결과]

![image](https://github.com/user-attachments/assets/d937af9d-45cc-429e-9250-340adee14b28)


[평가]

![9기_2팀_최종PPT pptx (10)](https://github.com/user-attachments/assets/79a8810e-f80f-4dec-8af3-648d152ce795)


[기대 효과]

![9기_2팀_최종PPT pptx (11)](https://github.com/user-attachments/assets/5c1836a7-8fd5-43a9-bf0b-ca08b4bdc531)


[확장 가능성]

![9기_2팀_최종PPT pptx (12)](https://github.com/user-attachments/assets/2b924d7e-67c9-4aae-a3d4-a8b1adc40773)



<br>
<br>

# 9. 향후 계획 및 보완점 



# 10. 회고

| 이름 | 회고록 |
|----------|-------------------------------------------|
| **김민균** | 우와 |
| **김준협** | 오 |
| **박민정** | 예 |
| **이민영** | 음 |
| **정의중** | 아 |
| **조세희** | 와우 |
