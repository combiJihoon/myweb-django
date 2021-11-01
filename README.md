# Django를 이용한 게시판 CRUD 백엔드 서버

Django를 백엔드 서버로 하여 만든 게시판으로, CRUD가 가능하며 커스텀 유저도 함께 구현했습니다.
<br>
각 게시글마다 "제목", "내용", "작성자", "작성일", "수정일"이 포함되어 있습니다.
<br>
가입, 로그인시 knox를 이용해 토큰을 부여합니다.
<br>
Django RESTframework를 사용하였으며, 연습용이기 때문에 DB는 SQLite를 사용했습니다.
<br>
Dokerfile이 설정되어 있어 도커를 이용해 컨테이너 생성이 가능합니다.
<br>

# 🔧 Tech Stack

## Infra

<table><tbody>
 <tr>
  <td>
   <div align="center"><a href="https://git-scm.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="60" height="40"/> </a></div>
  </td>
  <td>
   <div align="center"><a href="https://www.docker.com/" target="_blank"> <img src="https://www.docker.com/sites/default/files/d8/2019-07/vertical-logo-monochromatic.png" alt="docker" width="40" height="40"/> </a></div>
  </td>
 </tr>
  <tr>
    <td align = "center">Git</td>
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
   <div align="center"><a href="https://aws.amazon.com/ko/ec2/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/b/b9/AWS_Simple_Icons_Compute_Amazon_EC2_Instances.svg" alt="AWS EC2" width="40" height="40"/> </a></div>
  </td>
   <tr>
    <td align = "center">Python</td>
    <td align = "center">Django</td>
    <td align = "center">Django REST Framework</td>
    <td align = "center">Linux</td>
    <td align = "center">AWS EC2</td>
  </tr>
 </tr>
 </tbody></table>

### Database

<table><tbody>
 <tr>
  <td>
   <div align="center"><a href="https://www.sqlite.org/index.html" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/764px-SQLite370.svg.png" alt="sqlite" width="60" height="40"/> </a></div>
  </td>
 </tr>
  <tr>
    <td align = "center">SQLite</td>
  </tr>
</tbody></table>

<br>

# 🔧 Proejct Setup / and Organization

## Project structure

```
.
├── Dockerfile
├── README.md
├── boards
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── management
│   │   ├── __init__.py
│   │   └── commands
│   │       └── seed_boards.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── myweb
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
└── users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── management
    │   ├── __init__.py
    │   └── commands
    │       └── seed_users.py
    ├── managers.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py

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
