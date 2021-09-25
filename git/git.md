![image-20210716111403139](git.assets/image-20210716111403139.png)

![image-20210716110544509](git.assets/image-20210716110544509.png)

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

# git

> 분산 버전 관리 시스템 (DVCS, Distributed Version Control System)

윈도우 환경에서는 git 설치 및 실행을 위해 git bash를 다운로드 받는다.

## 기본 명령어

- ls (list의 약자) 목록 - 내 현재 목록을 보기위함
- cd (change directory) 폴더를 이동하는 명령어
- mkdir (make directory) 폴더 생성
- touch 비어있는 파일 생성
- rm (remove) 삭제

### 저장소(repository) 생성

```bash
$ git init
```

* `.git` 폴더가 숨김 폴더로 생성되고, git bash에서는 `(master)` 라고 표기 된다.
  * 저장소 생성시 상위 폴더에 `.git` 저장소가 있지 않은지 확인할 필요가 있다.
    * 예) 바탕화면에 실수로 `git init` 에서 `.git` 이 있는 경우

### 기본 버전 관리 흐름

* git은 저장소 내에 모든 파일의 변경사항을 추적함
* 작업을 완료하고 `add` -> `commit` 을 통해 버전을 기록한다.
  * `working directory` 에서 `add` 명령어를 통해 `staging area` 상태(`staged`)로
  * `staged` 상태인 파일들을 모두 `commit` 명령어를 통해 버전 기록

#### `add`

> `working directory` 에서 `add` 명령어를 통해 `staging area` 상태(`staged`)로
>
> 버전으로 기록할 파일을 모으기 위해 사용

```bash
$ git add a.txt    # 특정 파일
$ git add test/    # 특정 폴더
$ git add .        # 현재 디렉토리 (하위 디렉토리 포함)
$ git add git.md markdown.md # 이어서 쓰기
```

#### `commit` 

> `staged` 상태인 파일들을 모두 `commit` 명령어를 통해 **버전 기록**

```bash
$ git commit -m '커밋 메시지'
[master ce0578b] 커밋 메시지
 1 file changed, 1 deletion(-)
 delete mode 100644 a.txt
```

* 커밋 메시지는 현재 버전에 대해 알 수 있도록 작성
* 지금까지 커밋을 확인하기 위해서는 `git log` 명령어 사용

### 상태 확인 

#### `status`

> working directory와 staging area의 상태를 확인할 수 있다. 
>
> 특정 파일이 변경되었는지 (추가/수정/삭제), `staged` 상태인지

```bash
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   b.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        c.txt
```

#### `log`

> 커밋 로그를 확인

```bash
$ git log 
$ git log --oneline # 한줄로 간략히 표기
$ git log -2 # 최근 n개의 로그만 확인
$ git log --oneline -2 # 한줄로 최근 n개만
```



## 깃헙 프로젝트

1. open source 프로젝트 - Tensor flow
2. 개발자의 이력서 && 경험 1일 1commit - 잔디밭 쌓기

git 은 github과 다르다.

비유 하자면 마치 핸드폰의 사진첩 갤러리와 네이버 클라우드 구글 클라우드 등

## 깃헙 원격 remote origin 추가하기

```bash
$git remote add origin <https://github.com/K-Dongil/TIL.git>
```

## 깃헙 원격 remote origin 삭제하기

`````
$git remote rm origin
`````

## push

``````
$git push origin master
# 만약, 지정이 안되있다면 git아 원격저장소 추가해줘 origin이라는 이름으로 url을
``````

## 연결 확인

``````
$git remote -v
``````



## 원격 저장소 등록

``````
$git remote add origin 주소
``````

## staging area

버전을 나눠서 commit하고 싶을 때 필요한 영역

![image-20210716111435852](git.assets/image-20210716111435852.png)



## 로그인 정보

- 자격 증명 관리자에서 확인



## 오류

``````
$ git push origin master
To https://lab.ssafy.com/kdi1569/test.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://lab.ssafy.com/kdi1569/test.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
``````

- 원격저장소랑 로컬저장소 커밋 로그가 다른 경우
  - 원격저장소를 지원하는 곳에서 직접 수정한 경우 (Github/Gitlab)
  - 혹은 저장소 만들 때, README랑 같이 만들기 이런 옵션 클릭했을 때
  - 원격저장소에서는 파일만 만들어주지 않는다 
  - GIt은 버전관리시스템
  - Github/Gitlab 저장소에서 보이는 모든 파일은 단순히 특정 시점의 파일 구조인 것이고 실제로는 버전이 기록 되어 있다.

- 해결하기

  - 원격 저장소 버전 가져오기

    ``````
    git pull origin master
    ``````

  - Merge commit
    - 두 버전을 합치는 커밋
      - 일반적으로 충돌이 없으면 vs ocde창이 열리고(커밋메시지) 저장하고 종료하면 됨
      - 이 과정에서 동일 파일이 수정되어 있으면 충돌 발생
        - 충돌난 파일 확인해서 수정하고 add, commit-

## clone

- git hub에 올려져 있는 것들 모두 가져옴
- 가져온 다음 git init해줘야 연동 됨

## pull, push 와  clone 

- pull, push : 버전관리 (작업 중)

- clone,init : 저장소를 받아오고 저장소를 로컬 새로 생성 (프로젝트 시작 때)
  - clone을 하면 init을 할 필요가 없다??



## Git Bash 

- UINX/LINUX 명령어 -> Git Bash(번역) -> Windows
  - UINX/LINUX 명령어를 Windows에서 실행할 수 있게 번역해주는 것



## CLI명령어들

- 띄어쓰기를 기준으로 명령어를 구분한다
- git bash창에서 노란색부분 : 내가 위치한 폴더
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
2.  repo 안에 repo를 만들지 않는다. (이미 git init한 폴더 안에서는 또 git ini하지 않는다.)



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

    - 노란색으로 강조된 부분 : 고유ID

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

- 터미널 오픈
  - ctrl + `(백틱)

- bash창에서 위에서 봤던 CLI 명령어들 사용가능

