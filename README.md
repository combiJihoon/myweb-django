# Django를 이용한 게시판 CRUD 백엔드 서버

Django를 백엔드 서버로 하여 만든 게시판으로, CRUD가 가능하며 커스텀 유저도 함께 구현했습니다.
<br>
각 게시글마다 "제목", "내용", "작성자", "작성일", "수정일"이 포함되어 있습니다.
<br>
가입, 로그인시 knox를 이용해 토큰을 부여합니다.
<br>
Django RESTframework를 사용하였으며, DB는 MySQL RDS를 사용했습니다.
<br>
zappa를 이용해 deploy를 하여, lamdba와 S3가 사용됩니다.
<br>
추가적으로, Dokerfile이 설정되어 있어 도커를 이용해 컨테이너 생성이 가능합니다.
<br>
<br>

# 🔧 Tech Stack

## Infra

<table><tbody>
 <tr>
  <td>
   <div align="center"><a href="https://git-scm.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="60" height="40"/> </a></div>
  </td>
  <td>
   <div align="center"><a href="https://github.com/zappa/Zappa" target="_blank"> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwCZBA7JFqU1exIFDOX5-Ryt1rKosheBUVnw&usqp=CAU" alt="zappa" width="40" height="40"/> </a></div>
  </td>
  <td>
   <div align="center"><a href="https://www.docker.com/" target="_blank"> <img src="https://www.docker.com/sites/default/files/d8/2019-07/vertical-logo-monochromatic.png" alt="docker" width="40" height="40"/> </a></div>
  </td>
 </tr>
  <tr>
    <td align = "center">Git</td>
    <td align = "center">Zappa</td>
    <td align = "center">Docker</td>
  </tr>
</tbody></table>

## REST API

<table><tbody>
 <tr>
  <td width="75">
   <div align="center"><a href="https://www.python.org/" target="_blank"> <img src="https://www.python.org/static/community_logos/python-powered-h.svg" alt="Python" width="40" height="40"/> </a></div>
  </td>
  <td width="75">
   <div align="center"><a href="https://flask.palletsprojects.com/en/2.0.x/" target="_blank"> <img src="https://media.vlpt.us/images/combi_jihoon/post/a86eb6b0-2dfc-42f9-8c08-db0ff24e9c09/django.png?w=768" alt="Django" width="80" height="40"/> </a></div>
  </td>
  <td width="75">
   <div align="center"><a href="https://flask.palletsprojects.com/en/2.0.x/" target="_blank"> <img src="https://www.django-rest-framework.org/img/logo.png" alt="Django RESTframework" width="80" height="40"/> </a></div>
  </td>
  <td width="75">
   <div align="center"><a href="https://www.linux.org/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg" alt="linux" width="40" height="40"/> </a></div>
  </td>
  <td width="75">
   <div align="center"><a href="https://aws.amazon.com/ko/ec2/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Amazon_Lambda_architecture_logo.png/640px-Amazon_Lambda_architecture_logo.png" alt="AWS Lambda" width="40" height="40"/> </a></div>
  </td>
  <td width="75">
   <div align="center"><a href="https://aws.amazon.com/ko/s3/" target="_blank"> <img src="data:image/png;base64,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" alt="S3" width="40" height="40"/> </a></div>
  </td>
   <tr>
    <td align = "center">Python</td>
    <td align = "center">Django</td>
    <td align = "center">Django REST Framework</td>
    <td align = "center">Linux</td>
    <td align = "center">AWS Lambda</td>
    <td align = "center">S3</td>
  </tr>
 </tr>
 </tbody></table>

### Database

<table><tbody>
 <tr>
  <td>
   <div align="center"><a href="https://aws.amazon.com/ko/rds/" target="_blank"> <img src="data:image/png;base64,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" alt="rds" width="40" height="40"/> </a></div>
  </td>
  <td>
   <div align="center"><a href="https://www.mysql.com/" target="_blank"> <img src="https://ww.namu.la/s/d59b18ca16c075c57c5ebe902e14d46c58e2df1d638605017382993a696c0c8c2313077356a2bd90892fa9e00c704b6832c07c8981482d4d3b88ccb2848da73142a440a665710e13ce579236ead5ce33" alt="mysql" width="40" height="40"/> </a></div>
  </td>
 </tr>
  <tr>
    <td align = "center">RDS</td>
    <td align = "center">MySQL</td>
  </tr>
</tbody></table>

<br>

## ERD

<br>
<img src="https://user-images.githubusercontent.com/74451822/139637665-102ace6c-7356-4464-bdfa-f1e5c610fde3.png" alt="erd" width="600px" />

<br>

# 🔧 Proejct Setup / and Organization

## Project structure

```
.
├── AWSCLIV2.pkg
├── Dockerfile
├── README.md
├── boards
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── management
│   │   ├── __init__.py
│   │   └── commands
│   │       └── seed_boards.py
│   ├── migrations
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── core
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── management
│   │   ├── __init__.py
│   │   └── commands
│   │       └── create_db.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── myweb
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── users
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── management
│   │   ├── __init__.py
│   │   └── commands
│   │       └── seed_users.py
│   ├── managers.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── zappa_settings.json
```

## Install required packages

사용한 패키지들 다운로드

```bash
pip install -r requirements.txt
```

## Build

```bash
# $(pwd) = project root directory
docker build -t yourdockerusername/dockerfilename .
```

## Run

```bash
docker run -dp 8000:8000 yourdockerusername/dockerfilename
```

<br>

# :books: API List

## Boards

#### 1. BoardAPI

인증되지 않은 유저도 게시물을 볼 수 있으며, 글쓰기 기능은 인증된 사용자만 가능합니다.
<br>

- '/board' GET POST

#### 2. BoardDetailAPI

board id를 이용해 접근하며 인증 & 허용된 유저에게만 수정, 삭제 권한을 부여했습니다.
<br>

- '/board/<int:pk>' GET PUT DELETE

## Users

Logout 기능의 경우 knox를 이용하며, 발급된 token을 폐기합니다.

#### 1. ReigstrationAPI

knox를 이용해 가입시 유저 token을 부여합니다.
<br>

- '/users/register' POST

#### 2. LoginAPI

이메일 아이디와 비밀번호로 로그인하며, 로그인시 token이 발급됩니다.

- '/users/login' POST

#### 3. UserAPI

user token으로 인증된 유저의 아이디와 이름을 확인합니다.
<br>

- '/users' GET
