## Django

- Django is a high-level Pyhon WEb Framework that encourages rapid development and clean, pragmatic design
  - Django는 신속한 개발, 깨끗하고 실용적인 설계를 장려하는 높은 수준의 Python WEB 프레임워크
- It takes care of much of the hassle of Web development, so you can focus on Writing your app without needing to reinvent the wheel
  - 이것은 웹 개발의 많은 번거로움을 덜어주기 때문에 당신은 앱 작성에 집중할 수 있습니다

- 빠르고 깨끗한 개발을 지원 
- Web Framework
- 검증된 Python 언어 기반 Web Framework
- 대규모 서비스에도 안정적이며 오랫동안 세계적인 기업들에 의해 사용되고 있다

##### * Web

- 인터넷에 연결된 컴퓨터를 통해 정보를 공유할 수 있는 전 세계적인 정보 공간
- static web page(정적 웹 페이지)
  - 정보가 고정되어 있다
  - 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
  - 서버가 정적 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 없이 클라이언트에게 응답을 보냄
  - 모든 상황에서 모든 사용자에게 동일한 정보를 표시
  - 일반적으로 HTML, CSS, JavaSript로 작성됨
  -  flat page라고 한다

- Dynamic web page (동적 웹 페이지)
  - 웹 페이지에 대한 요청을 받은 경우는 서버는 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄
    - 내가 보내는 특정 키워드에 따라 페이지가 달라진다? 
  - 동적 페이지는 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름
  - 서버 사이드 프로그래밍 언어(python, java, c++ 등)가 사용되며 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐

##### * Framework

- Framework
  - 프로그래밍에서 특정 운영 체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임
  - 재사용할 수 있는 수많은 코드를 프레임워크로 통합함으로써 개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 같이 사용할 수 있도록 도움
  - Framework는 web을 어떻게 만들지 기본 틀이 주어진다.
  - Application Framework라고 함

##### * Web Framework

- Web Framework
  - 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적으로 데이터베이스 연동, 템플릿 형태의 표준, 세션관리, 코드 재사용 등의 기능을 표함
  - 동적인 웹페이지나, 웹 애플리케이션, 웹 서비스 개발 보조용으로 만들어지는  Application Framewokr의 일종

##### * Framework Architecture

- MVC Design Pattern(model-view-controller)
  - model : 데이터, view : 화면의 입력과 출력, controller : 제어
  - 프로그램의 구조, 설계패턴
- 소프트웨어 공학에서 사용되는 디자인 패턴 중 하나
- 사용자 인터페이스로부터 프로그램 로직을 분리하여 애플리케이션의 시각적 요소나 이면에서 실행되는 부분을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있음
- Django는 MTV pattern

##### * MTV Pattern

- Model

  - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)
  - DB를 직접 connection하고 데이터 가져오고 view에 data를 전달

- Template(MVC패턴에서 View)

  - 파일의 구조나 레이아웃을 정의
  - 실제 내용을 보여주는데 사용(presentation)
  - View에서 받은 data를 js/html 등 다양한 형태의 user interface 형태로 만들어서 web browser로 넘겨준다

- View(MVC패턴에서 Controller)

  - HTTP 요청을 수신하고 HTTP응답을 반환
  - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
    - 사용자의 요청을 받는다, Model에서 받은 data를 Template에 전달
  - template에게 응답의 서식 설정을 맡김

  <img src="Django.assets/image-20210831093648156.png" alt="image-20210831093648156" style="zoom:67%;" />

  ![image-20210831094039912](Django.assets/image-20210831094039912.png)



##### * Django Intro

1. django 설치

   ```
   $pip install django

2. 장고 프로젝트 생성

   - 프로젝트 자체를 장고용으로 만들어서 장고 기본 폴더들이 포함된 새로운 폴더가 생성된다

   - 프로젝트를 만들고자 하는 위치에서 실행할 것
   - 프로젝트 이름에는 

   ```
   django-admin startproject firstpjt(프로젝트 이름)
   ```
   - 프로젝트 구조

     

3. django extension 설정

   - 생성된 프로젝트에서 vs code실행 후 확장에서 Django 설치,  Ctrl + Shift + P 눌러서 기본설정 : 설정열기(JSON)을 누른 뒤 setting.json에 아래와 같은 코드 추가

   ```
   //Django
       "files.associations": {
           "**/*.html": "html",
           "**/templates/**/*.html": "django-html",
           "**/templates/**/*": "django-txt",
           "**/requirements{/**,*}.{txt,in}": "pip-requirements"
       },
       "emmet.includeLanguages": {
           "django-html": "html"
       }

4. django 서버 실행

   ```
   python manage.py runserver
   ```

   - 서버 종료 : Ctrl + C



- Project & Application
  - project
  - Application
    - 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담당
    - 하나의 프로젝트는 여러 앱을 가짐
    - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성함





앱을 만들때는 복수형으로 만든다

article X , articles