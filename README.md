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
   <div align="center"><a href="https://github.com/zappa/Zappa" target="_blank"> <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fgithub.com%2Fzappa%2FZappa&psig=AOvVaw0jhKtgCqnVrJ0vchliF3j2&ust=1636458561216000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCNjZ_KzZiPQCFQAAAAAdAAAAABAD" alt="zappa" width="40" height="40"/> </a></div>
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
   <div align="center"><a href="https://aws.amazon.com/ko/s3/" target="_blank"> <img src="https://www.google.com/search?q=s3&newwindow=1&sxsrf=AOaemvL9H6LXs1AxRERGB_ul3ABbWMHIsw:1636372407718&tbm=isch&source=iu&ictx=1&fir=oEvQYj12aPYkqM%252CLA_od3WTF7CnWM%252C_%253Bljw0ZaqBqOGhOM%252CbX6S1AGK1kQpZM%252C_%253Bi1q2xcI5r5ZRMM%252CgyxNcjgr9S0CWM%252C_%253BSWWhVb-6LYB7CM%252CgyxNcjgr9S0CWM%252C_%253Bg-HART1J4B2f8M%252CXO3Nuv3U9eaYZM%252C_&vet=1&usg=AI4_-kTUVaLaplLOaS9usy_Alj59m_NbeA&sa=X&sqi=2&ved=2ahUKEwjj5dOg2oj0AhWQJDQIHXeNBDYQ_B16BAg1EAE#imgrc=oEvQYj12aPYkqM" alt="S3" width="40" height="40"/> </a></div>
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
   <div align="center"><a href="https://aws.amazon.com/ko/rds/" target="_blank"> <img src="https://www.google.com/search?q=rds&newwindow=1&sxsrf=AOaemvJh_78vlZdwNLCfA38vDjTuHAou7w:1636372505500&tbm=isch&source=iu&ictx=1&fir=cHRUGgp6_PTT4M%252CJw0DIeQnmGpZYM%252C_%253BevI9Nak92T82xM%252C6b_E6_j7A83XYM%252C_%253BaApal0MgFYFlPM%252CFHNoSAJi3MijkM%252C_%253Bevav0zugXy6wqM%252CWU3XHULFys4HWM%252C_%253BOx-W-BngchbHEM%252CVlnFRAT0xapTQM%252C_&vet=1&usg=AI4_-kQCwjFqAdWUnNZbqkSSsyt8h2eQ1w&sa=X&ved=2ahUKEwi6z6PP2oj0AhUsGKYKHdVOBqwQ_B16BAg6EAE#imgrc=cHRUGgp6_PTT4M" alt="rds" width="40" height="40"/> </a></div>
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
