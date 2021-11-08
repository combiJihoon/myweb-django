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
   <div align="center"><a href="https://aws.amazon.com/ko/s3/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Amazon-S3-Logo.svg/640px-Amazon-S3-Logo.svg.png" alt="S3" width="40" height="40"/> </a></div>
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
   <div align="center"><a href="https://aws.amazon.com/ko/rds/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/AWS_Simple_Icons_Database_Amazon_RDS_DB_Instance_Standby.svg/640px-AWS_Simple_Icons_Database_Amazon_RDS_DB_Instance_Standby.svg.png" alt="rds" width="40" height="40"/> </a></div>
  </td>
  <td>
   <div align="center"><a href="https://www.mysql.com/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Database-mysql.svg/640px-Database-mysql.svg.png" alt="mysql" width="40" height="40"/> </a></div>
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
