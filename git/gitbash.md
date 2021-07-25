## Interface

- 서로 다른 두개의 시스템, 장치 사이에서 정보나 신호를 주고받는 경우의 접점이나 경계면

- HDMI선 : High Definition Multimedia Interface 
  - 모니터와 데스크탑을 연결해주는 인터페이스
- 사람과 컴퓨터를 이어주는 접점은  
  - Hardware : 모니터, 키보드, 마우스
  - Softward : GUI == CLI
    - 컴퓨터의 조작 (파일/폴더 생성 & 삭제, 폴더이동, 파일열기 등)
- CLI 배우는 이유 : 명령어의 종류 Unix/Linux vs  windows 두 운영체제는 전혀 다른 존재라서, 명령어가 다른 것도 많다.
  - 다른 컴퓨터(클라우딩 컴퓨터)가 파이썬 파일을 돌려주는데 보통 UNIX/LINUX 운영체제이다.



## Git Bash 

- UINX/LINUX 명령어 -> Git Bash(번역) -> Windows
  - UINX/LINUX 명령어를 Windows에서 실행할 수 있게 번역해주는 것



## CLI명령어들

- 띄어쓰기를 기준으로 명령어를 구분한다
-  git bash창에서 노란색부분 : 내가 위치한 폴더
- prompt($) : 명령어를 받아들일 준비가 되어있다는 기호
  - $ ls : 현재위치한 폴더 내부의 파일/폴더 출력
  - $ ls -a : 현재 위치한 폴더 내부의 모든 파일/폴더 출력(숨김파일까지)
  - $touch filename : filename으로 파일 생성(확장자 표기 필수)
  - 파일을 지정된 응용프로그램으로 실행(더블클릭)
    - $ start filename - windows
      - $ start . : git bash에서 현재 지정되어있는 위치를 열어준다(만약 ~뿐이라면 맨 앞의 계정을 열어준다)
    - $ open filename
  - $ rm filename : 파일 삭제(영구 삭제)
  - $ mkdir dirname : dirname으로 폴더 생성 (make directory)
  - $ cd dirname : 지정한 폴더로 이동
  - $ cd .. : 현재 위치한 폴더의 상위 폴더로 이동
  - $ rm -r dirname : 지정한 폴더 및 파일 삭제
  - $ rm -rf dirname : 지정한 포더 및 파일 강제(force) 삭제

- Root directory(/) : 모든 파일/폴더들의 최상위 폴더(''루트디렉토리로''부터 모든 폴더가 시작된다.)

- Home directory(~) : 사용자(계정)에게 할당된 폴더 ( git bash창에서 노란색부분이 ~ : Home 폴더)
  - Windows : /c/Users/<사용자이름>
  - Mac : /Users/<사용자이름>
- dot(.) : 현재 위치한 폴더를 지칭

- dotdot(..) :  현재 위치한 폴더를 기준으로 상위 폴더를 지칭
  - ..을 계속 사용하게 되면 Root directory에 도달한다.
- Tab키 : 파일/폴더 이름 자동완성 기능

- Ctrl + c : 실행중인 프로세스 취소(cancel)
- Ctrl + l : 터미널 창 정리하기 (clear)

- 키보드 방향 위 아래키 : 이전에 입력한 명령어 기록 탐색



## Git

- version control system 버전 관리 시스템

- Lunus Torvalds (리눅스(라이너스가 만든 유닉스), 깃 만든 분)



## 로컬 저장소 (Local repo)



## 초기화

- git에서 초기화란 일반 폴더를 git이라는 tool을 이용하여 버전관리가 가능할 수 있게 해주는 폴더로 만들어줌
- 초기화 = git init
- bash 창에서 git init된 repository 폴더는 경로 옆에 파란색 글씨가 생긴다



##### * $ git init [폴더를 저장소(Repository)로 만들어줌]

- Directory(폴더) - 기존의 폴더는 아무기능 없음
- Repository(저장소) - 내부의 모든 파일/폴더를 관리
- .git 숨김폴더가 생성 됨



##### * Warning

1.  Home 폴더(~)에서 초기화(git init) 하지 않는다. 
2. repo 안에 repo를 만들지 않는다. (이미 git init한 폴더 안에서는 또 git ini하지 않는다.)



##### * repository 안에 존재하는 3가지 공간

- 밑의 3가지 과정을 반복하는게 git의 핵심!!
- git 사용자는 스테이지와 저장소를 눈으로 직접 보는것은 아니다.

- 작업공간  Working directory
  - **작업공간**에서 코드 작성 및 수정 
- 스테이지 Staging area
  - 기록될  파일들의 변경사항들을 **스테이지**에 올린다.
- ★★★★★저장소 commits★★★★★
  - 스테이지 위의 변경사항들을 저장 즉,  **commit**(스냅샷)을 한다.

- 비유 CF촬영장
  - 분장실 (분장실은 사진 찍는 곳이 아니다.)

  - 촬영장 (촬영을 한다.)
  - 사진들 (사진들이 나온다.)



 ##### * 커밋(Commit) 남기기 : Versioning

- commit에는 작성자의 서명이 필요

- 매번 서명하기는 힘든 일, 그래서 자동으로 찍히는 도장을 만들어 두는 행동 (보통 컴퓨터당 한번하면 다 찍힘)

  - 서명에 사용할 이름(닉네임) 설정 : 개발에 쓰이는 닉네임

    ```
    $ git config --global user.name <이름>
    ```

  - 서명에 사용할 이메일 설정 : 개발할 때 쓰는 이메일

    ```
    $ git config --global user.email <이메일>
    ```

- 작업공간 -> 스테이지

  ```
  $ git add 파일이름
  ```

  ```
  $ git add . (전체)
  ```

- 스테이지 -> 저장소

  - 각각의 커밋마다 메시지를 반드시 적어야 한다. (내가 이걸 왜 했는지)
  - 최초의 커밋 - root commit(first commit)이라고 남겨지는 경우가 많다.

  ```
  $ git commit -m '메시지 입력'
  ```

- 스테이지 상황 모니터링 (Status & Log)

  - 작업 공간에서 무엇이 변경되었는지, 스테이지에 무엇이 올라왔는지

    ```
    $ git status
    ```

  - 저장소 내부의 commit들을 조회

    ```
    $ git log
    ```

    -  노란색으로 강조된 부분 : 고유ID

    - 메시지는 중복되도 상관없는데, commit ID는 주민등록번호같은 존재

      ```
      $ git log --oneline # 너무길어서 짧게보고싶어!
      ```



## Remote git (원격 저장소) <->로컬 저장소

- 원격저장소 Remote repository (마치 클라우드에 빽업할 파일 올리듯이)

- repository를 백업하는 3대장 Github, Gitlab, BitBucket 
- 원격 저장소는 고유 url이 있다.



##### * 클라우드에 백업

1. 내 컴퓨터의 특정 폴더를 지정
2. 클라우드에 동기화할 폴더를 생성
3. 내 컴퓨터와 클라우드를 연결
4. 파일 업로드 



##### * Remote repo에 백업

1. Local repo 생성 

   ```
   $git init
   ```

2. Remote repo 생성

   - remote repository는 Github, Gitlab에서 프로젝트 생성하는 것

3. Local repo와 Remote repo 연결

   ```
   $ git remote add <name(변수명)> <url> # name이라는 변수에 url을 담겠다
   ```

4. Commit 업로드 (push)

   ```
   $ git push <name(변수명)> <branch>
   ```



##### * 클론받기 /  pull 받기

- Clone 받기 (기존의 remote repository를 받아오는 것)

  - 최초 한 번 프로젝트를 `clone`하여 저장합니다
  - clone 받은 폴더에서 프로젝트를 진행X
  - clone 받은 폴더는 git bash에서 확인하면 init이 이미 되어있는데 push 불가능?
    - push는 주인이 허락해야만 할 수 있다. 

  ```
  $ git clone <url> # url은 깃랩, 깃헙 프로젝트에서 클론 주소가 있다.
  ```

- pull 받기

  - 이 후 새로운 프로젝트가 업데이트 될 때마다 `pull`하여 추가된 데이터를 가져옵니다.

  ```
  $ git pull <name> <branch>
  ```

- init 과 clone은 최초 한번만 하면 되고, 나머지는 반복 & 반복~



## vs code에서 bash 사용

- vs code 여는 방법 (설정 필요)
  - 실행하고자 하는 폴더에서

    ```
    $ code .
    ```

- 터미널 오픈
  - ctrl + `(백틱)

- bash창에서 위에서 봤던 CLI 명령어들 사용가능



## local <-> remote

