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
   <div align="center"><a href="https://www.mysql.com/" target="_blank"> <img src="data:image/png;base64,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" alt="mysql" width="40" height="40"/> </a></div>
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

## Deploy

```bash
zappa init
```

```bash
zappa deploy
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
