### 안녕하세요, 3조 백엔드-DB 팀입니다.

앞으로 진행될 프로젝트 병합 과정에서의 문제를 관리하고자 스프레드시트 파일을 만들어 공유드립니다.

3조 백엔드 팀에게 질문하실 내용을 [여기](https://docs.google.com/spreadsheets/d/18vAw3wEnwzzxgxT8H-mUfDs_zQrDpR-gX497ZFPqaRw/edit?gid=833081153#gid=833081153)에 작성해주시면 감사하겠습니다.

ERD ver 0.2를 카카오톡 채팅방에 배포하기 전까지 이슈가 해결된 ERD, SQL 쿼리는 [이 페이지](https://pretty-icebreaker-f34.notion.site/ERD-ver-0-2-79bc33afd7f24980ba2b1b7ee7db4d1a) 에서 실시간으로 확인할 수 있습니다. 감사합니다.

---

### 진행 내역

진행이 되는 대로 계속하여 업데이트 중입니다.

[완료]

- DB & 서버단
    - DB ERD ver 0.2 배포전
    - MariaDB 데이터베이스, 테이블 생성 및 더미데이터 추가하여 구동 완료
    - MariaDB와 Django 연동 완료, 어드민화면에서 데이터 불러오기까지 완료
    - 로그인 구현 완료

- 클라이언트단
    - ~tkinter, backend 파일간 연결 코드 작성 완료~
    - ~jetson backend와 DB 연결 완료~
    - ~DB SELECT, INSERT 쿼리 작성 완료~
    - 로그인 구현 테스트 완료

[진행중]

- 클라이언트단
    - tkinter와 클라이언트단 backend 파일 연결 중 (tkinter 내 변수 파악 중)

- 서버단
    - 클라이언트 POST DB에 입력 구현 중