### 안녕하세요, 3조 백엔드-DB 팀입니다.

앞으로 진행될 프로젝트 병합 과정에서의 문제를 관리하고자 스프레드시트 파일을 만들어 공유드립니다.

3조 백엔드 팀에게 질문하실 내용을 [여기](https://docs.google.com/spreadsheets/d/18vAw3wEnwzzxgxT8H-mUfDs_zQrDpR-gX497ZFPqaRw/edit?gid=833081153#gid=833081153)에 작성해주시면 감사하겠습니다.

ERD ver 0.2를 카카오톡 채팅방에 배포하기 전까지 이슈가 해결된 ERD, SQL 쿼리는 [이 페이지](https://pretty-icebreaker-f34.notion.site/ERD-ver-0-2-79bc33afd7f24980ba2b1b7ee7db4d1a) 에서 실시간으로 확인할 수 있습니다. 감사합니다.

---

### 진행 내역

진행이 되는 대로 계속하여 업데이트 중입니다.

[완료]

-   DB & 서버단

    -   DB ERD ver 0.2 배포전
    -   MariaDB 데이터베이스, 테이블 생성 및 더미데이터 추가하여 구동 완료
    -   MariaDB와 Django 연동 완료, 어드민화면에서 데이터 불러오기까지 완료
    -   로그인 구현 완료
    -   DB 데이터 조회 및 업데이트/추가 구현 완료
    -   API 내 매일 0시 자동실행 함수 구현 완료

-   클라이언트단
    -   UI 데이터 송수신 코드 작성 완료
    -   서버 로그인 구현 완료
    -   서버 데이터 송수신 구현 완료

[진행중]

-   서버단

    -   메일 발송 시스템 구현중

-   클라이언트단
    -   UI 파일 연결중

---

### 환경 구성 (Dependencies)

-   SERVER
    macOS 14.5 (Apple M1)
    python 3.8.19

    | pip package name               | version |
    | ------------------------------ | ------- |
    | Django                         | 4.2.14  |
    | Django-crontab                 | 0.7.1   |
    | Django-restframework           | 3.15.2  |
    | Django-restframework-simplejwt | 5.3.1   |
    | mysqlclient                    | 2.2.4   |
    | python-dotenv                  | 1.0.1   |

    | brew package name | version |
    | ----------------- | ------- |
    | mariadb           | 11.4.2  |
    | mysql             | 8.3.0   |
    | openssl           | 3.3.1   |
    | mysql-client      | 8.3.0   |
    | pkg-config        | 0.29.2  |

-   ClIENT
    Ubuntu 18.04 (Jetson TX2 NX)
    python 3.8.0

    | pip package name | version |
    | ---------------- | ------- |
    | python-dotenv    | 1.0.1   |
    | requests         | 2.32.2  |
