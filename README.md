# Python-lecture 

교재 : [파이썬 코딩 도장](https://dojang.io/course/view.php?id=7)  
소스코드 : [파이썬코딩도장 소스코드](https://github.com/namjaeyoon/python.dojang)  
저자 : 남재윤 (도서출판 길벗)  
<br>

## 학습에 도움이 되는 사이트 및 유튜브 채널
 > + [파이썬 튜터](http://pythontutor.com/live.html#mode=edit)는 live programing으로 파이썬의 작동원리를 파악할 수 있습니다.   
 > + [K-Mooc](http://www.kmooc.kr/)은 한국형 온라인 공개 강좌입니다. 다양한 대학의 강의를 들을 수 있습니다.  
 > + [허민석님 유투브](https://www.youtube.com/user/TheEasyoung/videos)는 다양한 파이썬 강의와 머신러닝 딥러닝 등의 정보를 제공해 줍니다.
 > + [파이썬 - 기본을 갈고 닦자](https://wikidocs.net/book/search/result/1553)에서 파이썬 기초 문법을 공부할 수 있습니다.
 > + [다양한 파이썬 내장함수 - 점프 투 파이썬](https://wikidocs.net/32)은 파이썬 기초 문법뿐만아니라 다양한 내외장 함수에 대한 설명을 제공해 줍니다.
 > + [데이터 사이언스 스쿨](https://datascienceschool.net/view-notebook/39569f0132044097a15943bd8f440ca5/)  
 <br>
 
## Anaconda 설치 방법
 > 1. [아나콘다 홈페이지 다운로드](https://www.anaconda.com/distribution/)페이지로 이동 합니다.
 > 2. Windowns 버전을 선택하고 python 3.7 vesrion을 컴퓨터 환경(64bit|32bit)에 맞게 설치 파일을 다운로드 합니다. 
 > 3. 설치파일을 실행한 후 사용자 환경(`All user | Just me`)과 폴더 위치를 선택합니다.
 > 4. Advanced Options에서 기존 파이썬이 설치되어 있지 않다면 `Register Anaconda as the system python 3.7`옵션을 선택합니다.
 > 5. 그리고 `Add Anaconda to the system PATH enviroment variable` 옵션으로 (시스템)환경변수를 자동으로 설정해주고 `install`합니다.  
 
 > *단, 아나콘다에서 추천하는 방법은 아닙니다. 옵션의 설명은 다음과 같습니다.*
 > - PATH 환경 변수에 Anaconda를 추가할지 여부를 선택하십시오. 
 > - PATH 환경 변수에 **다른 소프트웨어를 방해 할 수 있으므로** Anaconda를 추가하지 않는 것이 좋습니다. 
 > - 대신 시작 메뉴에서 Anaconda Navigator 또는 Anaconda Prompt를 열어 Anaconda 소프트웨어를 사용하십시오.
 > - 환경변수에 추가할지를 선택 아나콘다 외에 다른 파이썬 인터프리터를 환경변수에 등록해서 사용 한다면 체크 해제 하고,
 > - 아나콘다만을 사용하는 경우 또는 아나콘다가 주력일 경우로 윈도우 CMD창에서 파이썬을 실행할 경우 선택합니다. 
 > - 선택할 경우 **윈도우 CMD창 경로와 상관없이 아나콘다를 파이썬으로 인식합니다.** 
 <br>
 
## 파이참(PyCharm) 설치 방법 및 사용자 설정
 > 1. [파이참 홈페이지](https://www.jetbrains.com/pycharm/download/#section=windows)에서 Community버전을 다운로드 합니다.
 > 2. 경로를 원하는 곳을 지정 한 후 `Installation Options`에서 `64-bit launcher`와 `.py`, `Add launchers dir to the PATH`를 체크해줍니다.
 > 3. 설치를 마무리 합니다.
 > 4. 파이참 실행 후 `File -> Settings -> Project:`에서 `Interpreter`를 `anaconda에 설치된 pytheon`으로 설정해줍니다.
 > 5. 다음으로 `Setting -> Appearance & behavior와 Editor`에서 폰트를 변경할 수 있습니다.
 > 6. 또한 `Keymap`에서 검색창에 `Execute selection in console`을 검색한 후 편한 단축키로 변경합니다.
 > + 기본 단축키인 Alt+shift+E는 코드를 한 줄 씩 실행합니다. 이를 통해 `console`창에서 코드 각각을 확인할 수 있습니다.  
 > + [파이참 단축키 모음](https://m.blog.naver.com/PostView.nhnblogId=passion053&logNo=220684364208&proxyReferer=https%3A%2F%2Fwww.google.com%2F)  
 <br>
 
## 아나콘다(Anaconda)와 파이참(PyCharm) 가상환경 연동시키기
 > 1. 먼저 `Anaconda Navigator`에서 왼쪽에 있는 `Environments`를 선택합니다. 
 > 2. 하단에 있는 `Create`를 눌러 가상환경으로 사용할 폴더 이름과 파이썬 버전을 선택하고, 가상환경을 만들어 줍니다.
 > 3. 기존의 `base(root)` 아래에 가상환경이 만들어집니다. 
 > - *추가적으로 `Search Packages`를 통해 필요한 패키지를 선택하여 설치할 수 있습니다.*
 > 4. 우선 파이참을 실행시킨 후 오른쪽 상단의 `File -> Close Project`로 기존의 프로젝트롤 종료해줍니다.
 > 5. 그리고 `Create New Project`를 눌러 새로운 프로젝트를 만들 준비를 합니다.
 > 6. 다음으로 `Location`에서 새로운 프로젝트의 폴더명을 만들어 준 후, 아래에 있는 `Project Interpreter 부분의 화살표`를 눌러줍니다.
 > 7. 여기서 `Existing interpreter`를 눌러 `Anaconda에서 만든 가상환경 폴더에 위치한 Python`을 선택해 주고, `Create`를 눌러줍니다.
 > 8. 새로운 환경에서 `test.py`를 생성한 후 아래에 있는 `Console`창에서 파이썬 버전을 확인하고,`hello world`를 출력해 봅니다.
 > 9. 출력이 정상적으로 된다면 가상환경을 제대로 구축한 것입니다.  
 > [참고 : 파이참(PyCharm) 설치 및 아나콘다 가상환경 적용](https://bradbury.tistory.com/63)  
 > [참고 : Python 가상환경 venv 간단한 사용법 + 주의사항](https://seolin.tistory.com/96)  
<br>

## 강의 핵심 내용 요약본   
### **2019.07.15**  
 > - [기본문법 핵심정리](https://dojang.io/mod/page/view.php?id=2168)  
 > - [숫자 계산, 변수 입력 및 사용, 출력 방법, 파이썬 연산자 핵심정리](https://dojang.io/mod/page/view.php?id=2189)
 > - [불과 비교 및 논리 연산자, 문자열, 리스트와 튜플, 시퀀스 자료, 딕셔너리 사용법 핵심정리](https://dojang.io/mod/page/view.php?id=2218)

### **2019.07.16**
 > - [논리 및 비교 연산자, 문자열, 리스트, 튜플, 시퀀스 자료형, 딕셔너리 핵심정리](https://dojang.io/mod/page/view.php?id=2218) 

### **2019.07.17**
 > - [if, else, elif 핵심정리](https://dojang.io/mod/page/view.php?id=2239)
 > - [for, while, break, continue 핵심정리](https://dojang.io/mod/page/view.php?id=2279)
 > - [for문을 이용한 별 찍기, FizzBuzz 문제](https://dojang.io/mod/page/view.php?id=2259)
### **2019.07.18**
 > - [1~3차원 리스트, 튜플, 문자열 응용하기 핵심정리](https://dojang.io/mod/page/view.php?id=2305)
### **2019.07.19**
 > - [딕셔너리 응용하기, 세트 사용하기 핵심정리](https://dojang.io/mod/page/view.php?id=2323)
 > - [파일 다루기](https://dojang.io/mod/page/view.php?id=2325)  
 > - [파일 다루기 참고자료](https://godoftyping.wordpress.com/2017/07/01/python-%ED%8C%8C%EC%9D%BC-%EB%94%94%EB%A0%89%ED%84%B0%EB%A6%AC-%EC%A1%B0%EC%9E%91/)  
 > - [회문 판별과 N-gram 만들기 핵심정리](https://dojang.io/mod/page/view.php?id=2335)
### **2019.07.22**
 > - 함수 다루기 기초
 > - 코딩도장 예제, 파이썬 300제 문제 풀기 
### **2019.07.23**
 > - [함수 사용하기 핵심정리](https://dojang.io/mod/page/view.php?id=2357)
 > - [람다, 클로저 사용하기 핵심정리](https://dojang.io/mod/page/view.php?id=2370)
 > - 클래스 입문  
### **2019.07.24**
 > - [클래스 속성과 정책, 클래스 메서드 사용하기](https://dojang.io/mod/page/view.php?id=2378)  
 > - [클래스 상속 사용하기](https://dojang.io/mod/page/view.php?id=2384)  
 > - 연습문제 다시한번 풀어보기  
### **2019.07.25**
 > - 파이썬 시험
 > - [예외처리 사용하기](https://dojang.io/mod/page/view.php?id=2398)
 > - [이터레이터 맛보기](https://dojang.io/mod/page/view.php?id=2405) 
 > - 제너레이터 맛보기 
### **2019.07.26**
 > - [데코레이터 사용하기](https://dojang.io/mod/page/view.php?id=2427)  
 > - [정규표현식 사용하기](https://dojang.io/mod/page/view.php?id=2435)  
 > - [정규표현식 정리](https://whatisthenext.tistory.com/116)  
 > - [모듈과 패키지 사용하기 및 만들기 핵심정리](https://dojang.io/mod/page/view.php?id=2454)  
### **2019.07.29**
 > - Numpy 기초 다루기  
### **2019.07.30**
 > - [Pandas 패키지 소개](https://datascienceschool.net/view-notebook/ee0a5679dd574b94b55193690992f850/)
 > - [Pandas 데이터 입ㆍ출력](https://datascienceschool.net/view-notebook/c5ccddd6716042ee8be3e5436081778b/)
 > - [Pandas 데이터프레임 : 고급 인덱싱](https://datascienceschool.net/view-notebook/704731b41f794b8ea00768f5b0904512/)
 > - [Pandas 데이터프레임 : 데이터 조작](https://datascienceschool.net/view-notebook/aa62265f02fc429aa636ef343c3b1fda/)
 > - [Pandas 데이터프레임 : 인덱스 조작](https://datascienceschool.net/view-notebook/a49bde24674a46699639c1fa9bb7e213/)  
 
 
