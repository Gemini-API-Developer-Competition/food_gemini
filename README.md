# GEMINI API

## LLM 모델 기반 게시판 글 자동작성 및 사업자정보확인 API

### 1. Flask
- Flask를 활용하여 RESTful API로 생성되었습니다.
- 해당 API는 Firebase에 있는 웹 애플리케이션이 활용할 수 있도록 개발되었습니다.

### 2. Gemini API (Gemini Pro)
- Gemini 모델을 **Fine-Tuning**하여 구현되었습니다.
- 음식점 이름, 간단한 음식 소개, 음식 종류, 전화번호를 입력하면 자동으로 게시판 글이 생성됩니다.
- 예시: 아래와 같이 게시판 글이 생성됩니다.  
  ![게시판 생성 예시](https://github.com/user-attachments/assets/2ec0fe10-464d-4f58-a350-2e979ae3ac39)  
  ![게시판 생성 예시 2](https://github.com/user-attachments/assets/24f14335-290a-40b4-a4a3-34fcd5690712)

### 3. 사업자등록정보 확인 (공공데이터 포털)
- 국세청의 **사업자등록정보 진위확인 및 상태조회 서비스**를 활용하여 사업자번호 입력 시 사업자인지 여부를 확인합니다.
- [공공데이터 포털 API 링크](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15081808)
- 확인 후 회원가입을 진행합니다.  
  ![사업자 확인 예시](https://github.com/user-attachments/assets/52b93c55-ae79-4dc0-b6a7-db6d804af930)

### 4. Firebase 배포
- Firebase Functions를 통해 API가 배포되었습니다.

## Trouble Shooting

- **pip install 오류**  
  `$ pip install google-generativeai` 명령어로 해결하였습니다.

- **데이터 문제**  
  Google AI Studio의 모델을 활용하여 대량의 더미 데이터를 생성하였습니다.

- **jsonl 파일 형식 오류**  
  테스트에서 제공하는 데이터셋과 같이 `message`, `role`, `content`, `role`, `content` 형식으로 변경하여 문제를 해결하였습니다.  
  ![JSONL 파일 형식](https://prod-files-secure.s3.us-west-2.amazonaws.com/b5e4d902-d8f0-45cc-a009-efc4bef6bf3b/29884ec0-d424-47ae-9b29-39e3f424b9b3/Untitled.png)

- **Google SDK 관련 오류**  
  Google SDK를 다운로드한 후 진행하여 에러를 해결하였습니다.

## 향후 계획
- Gemini 모델의 Fine-Tuning 고도화  
  더 많은 데이터와 파라미터 값을 조정하여 모델을 강화할 계획입니다.
- 다양한 모델을 테스트하여 가장 적합한 모델을 선택해 진행할 계획입니다.

## 기타 사항
1. Conda 환경 설정
2. Flask 활용
3. 파인 튜닝 전 진행 날짜: 2024-08-06
4. API Key는 `.gitignore`에 추가
5. 사업자번호 API 완료 날짜: 2024-08-08
6. 파인 튜닝 완료 및 Google SDK 설치 후 진행
7. Input 데이터 형식 예시: ex) 상호명 : 푸짐한 밥상\n음식 : 닭가슴살 샐러드\n소개 : 신선한 채소와 닭가슴살로 만든 건강 샐러드\n전화번호 : 010-1234-5678
8. 용량초과로 인해 push 불가능 zip파일 공유 완료

