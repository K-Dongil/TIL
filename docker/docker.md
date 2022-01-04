## 서버

##### * 자체 서버 운영 (과거)

- 서버 주문 -> 서버 설치 -> CPU, 메모리, 하드디스크 조립 -> 네트워크 연결 -> OS 설치 ->계정 설정 -> 방화벽 설정 -> ...
- 서버를 설정하기 위해 많은 노력과 시간이 필요

- node.js로 만든 application을 서버에 설치하는 과정

  <img src="C:\Users\Administrator\Desktop\TIL\docker\docker\image-20220104131847246.png" alt="image-20220104131847246" style="zoom:67%;" />



##### * 서버관리의 흐름

​	<img src="C:\Users\Administrator\Desktop\TIL\docker\docker\image-20220104131758414.png" alt="image-20220104131758414" style="zoom: 67%;" />



##### * 서버관리 5가지

1. 문서작성

   - ppt
   - 단점 : 문서의 정확성

2. 상태관리 도구

   - 상태관리 도구를 사용해서 Enter를 치면 도구가 Server에 접속해서 설치가 되어있는지 확인 필요에 따라 설치, 업그레이드 실행

   <img src="C:\Users\Administrator\Desktop\TIL\docker\docker\image-20220104132506157.png" alt="image-20220104132506157" style="zoom:50%;" />

3. 가상머신

   - Jenkins, Wordpress, Chat
   - 단점 : 용량이 크다, 처음부터 다시 셋팅하기 어려움, 서버 이미지 공유, 느림

4. 클라우드

   - AWS, Google Cloud, Azure

   - 하드웨어 파편화 문제 해결
   - 가상화된 환경만으로 아키텍처 구성이 가능
   - 이미지를 기반으로한 다수의 서버 상태 관리
     - 상태관리에 대한 새로운 접근
     - 서버운영의 문제는 여전히 그대로

5. Paas

   - Heroku, Netlify, AWS Elastic Beantalk, Google Cloud App Engine
   - 소스 코드만으로 배포 가능
     - 깃허브 하나만으로도 배포가 가능
   - 일반화된 프로비저닝 방법 제공
     - 프로비저닝 과정에 개입 불가능
   - 단점
     - 애플리케이션을 PaaS방식에 맞게 작성해야함
     - 서버에 대한 원격 접속 시스템을 제공X
     - 서버에 파일 시스템을 사용 불가능
     - Site 패키지 설치X
     - 로그 수집을 제한적인 방식으로 허용(STDOUT)
     - 다음과 같은 작업이 어려워짐
       1. 크론잡(문자 발송, 예약, 정산 등)
       2. 데이터 분석(BigQuery, S3 등 연동)
       3. 로그 분석(엘라스틱 서치, 스택드라이버, 클라우드와치 등)
       4. 애플리케이션 성능 모니터링
       5. A/B테스트 Canary 배포
       6. 네트워크, 스토리지 설정



## 도커와 쿠버네티스

##### * 도커

- OS 레벨 가상화를 이용하여 컨테이너화 된 스프트웨어 패키징 및 관리가 가능한 가상화 도구

  <img src="C:\Users\Administrator\Desktop\TIL\docker\docker\image-20220104145510265.png" alt="image-20220104145510265" style="zoom:67%;" />

- 컨테이너(애플리케이션)

  - 격리된 환경에서 작동하는 프로세스

  - App을 동작시키는데 필요로하는 환경/설비(라이브러리, node.js, java 등과 같은 플랫폼)와 같은 하나의 독립된 공간

  - 원활한 서비스를 제공하기 위한 하나의 묶음 단위

  - 하나의 리눅스 프로세스가 전용 서버에서 동작하고 있는 것 같은 분리 상태를 만들어 낸다

    - Why 리눅스?

      ```
      container는 리눅스 커널에 의해 사용됨.
      -> 리눅스 커널 안에 chroot(독립된 공간 형성), namespace(6가지 독립된 isolate 기능 지원),cgroup(필요한만큼 H/W지원) 3가지를 지원한다.
      
      이 커널의 기능으로 컨테이너들이 만들어짐
      ```

      <img src="https://postfiles.pstatic.net/MjAyMTEwMDNfOSAg/MDAxNjMzMjY3NzAyNTM4.6lzLWzib2bLGP5sYdMfaOUUqXNcVBcSU7VyculEn_Wog.ni1MusqPBvALNAlHHqr6nKdzzHmwpRKvUZ-pgv-qLb4g.PNG.gmlakd5944/image.png?type=w773" alt="img" style="zoom: 80%;" />

- 도커와 가상머신의 차이

  - 가상머신은 가상의 OS(윈도우 위에 리눅스라는 OS가 있고 그 위에 프로그램이 존재) -> overhead존재
  - 도커는 별도의 가상의 공간X -> overhead존재X
    - 다른 프로세스와 격리되어 가상머신처럼 사용하지만 성능저하 거의X

  ![image-20220104135615330](C:\Users\Administrator\Desktop\TIL\docker\docker\image-20220104135615330.png)

- 도커의 특징
  - 프로세스를 가상으로 분리
  - 파일, 디렉토리 가상으로 분리
  - CPU, Memory, I/O 그룹별로 제한
  - 리눅스 기능을 이용한 빠르고 효율적인 서벌관리
- 도커의 문제점
  - 관리, 서비스 검색, 서비스 노출, 서비스 이상 & 부하 모니터링



##### * Container Orchestration

- 복잡한 컨테이너 환경을 효과적으로 관리하기 위한 도구

1. 중앙제어(CLUSTER)

   - 개발자, master, cluster로 구분

   - master에게 명령을 내리는 중앙제어 시스템

     - master에게 서버를 띄어주라는 명령 -> 관리하고 있는 cluster서버중에서 여유있는 쪽에 배포

   - cluster끼리 네트워킹 연결

     <img src="C:\Users\Administrator\Desktop\TIL\docker\docker\image-20220104142417489.png" alt="image-20220104142417489" style="zoom:67%;" />

2. 상태관리(STATE)

   - 실제 server에 들어가서 container를 띄우는게 아니라 설정을 통해 관리

     <img src="C:\Users\Administrator\Desktop\TIL\docker\docker\image-20220104142338855.png" alt="image-20220104142338855" style="zoom:80%;" />

3. 배포관리(scheduling)

   - 가장 여유가 있는 서버에 배포
     - 서버에 여유가 없을 때 새로운 서버를 생성

4. 배포 버전관리

   - 설정으로 손쉽게 관리

     <img src="C:\Users\Administrator\Desktop\TIL\docker\docker\image-20220104142454875.png" alt="image-20220104142454875" style="zoom:67%;" />

     <img src="C:\Users\Administrator\Desktop\TIL\docker\docker\image-20220104142518955.png" alt="image-20220104142518955" style="zoom:67%;" />

5. 서비스 등록 및 조회(service discovery)

   - server 실행시 server의 ip를  오케스트레이션이 알아내서 저장(로드밸런싱)

     ![image-20220104142842905](C:\Users\Administrator\Desktop\TIL\docker\docker\image-20220104142842905.png)

6. 볼륨 스토리지
   - ebs 관리



##### * 쿠버네티스

- 컨테이너를 쉽고 빠르게 배포/확장하고 관리를 자동화해주는 오픈소스 플랫폼

- 언제 어디서든 빠르고, 유연하게 동일한 품질의 서비스를 제공할 수 있도록 만든 조직구성 방법

----

- 참고 사이트

컨테이너 : [참고1](https://losskatsu.github.io/it-infra/docker00/#2-%EA%B0%80%EC%83%81%EC%84%9C%EB%B2%84-vs-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88) [참고2](https://blog.naver.com/gmlakd5944/222525538213) [참고3](https://blog.naver.com/ji_sung31/222030918443)

