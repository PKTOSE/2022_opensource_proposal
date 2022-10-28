# 2022_opensource_proposal

2022년도 오픈소스기초설계 개별 제안서 업로드용 깃허브

<img src="https://img.shields.io/github/issues/PKTOSE/2022_opensource_proposal"> <img src="https://img.shields.io/github/forks/PKTOSE/2022_opensource_proposal"> <img src="https://img.shields.io/github/stars/PKTOSE/2022_opensource_proposal"> <img src="https://img.shields.io/github/license/PKTOSE/2022_opensource_proposal"> <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/opensource-%EC%98%A4%ED%94%88%EC%86%8C%EC%8A%A4%EA%B8%B0%EC%B4%88%EC%84%A4%EA%B3%84__%EA%B0%9C%EB%B3%84%EC%A0%9C%EC%95%88%EC%84%9C-brightgreen">

## 내 깃헙 프로필

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=PKTOSE&layout=compact"> <img src="https://github-readme-stats.vercel.app/api?username=PKTOSE&show_icons=true">

## 과제 내용 - 1

> - Github 페이지 생성, public으로 전체 공개 (5점)
> - Github 페이지의 라이선스 형태 명시 (2점)
> - 폴더 생성: src/ --> 폴더 안에 프로그래밍 파일 1개 이상 업로드 (2점)
> - 폴더 생성: doc/ --> 폴더 안에 프로젝트 제안서 업로드 (2점)
> - 파일 수정: src/ --> 폴더 안에 파일 내용 수정 commit & push 1회 이상 (2점)
> - Github 페이지의 README.md 생성 (2점)
> - Github 페이지의 README.md 편 --> 5개 이상의 문법 요소 활용 (5점)
>   e.g. 내용 작성, 문서 제목, 항목 열거, 문단 강조/나눔, 폰트 크기/스타일 변경, 링크 삽입 등

## 과제 내용 - 2

> - 각 문제에서 요구하는 출력을 보여주는 shell script 프로그래밍 각 3점씩 10문제
> - 각 문제별로 1개씩 파일 작성 후 출력화면을 스크린샷. 보고서에 결과 위주로 정리.
> - 각 문제별로 지각 -1점 감점. 스크린샷 없이 코드만 있는 경우 -2점 감점.
> - 개별 Github 페이지에 업로드. 보고서는 ./doc에서 소스 파일은 ./src에서 관리

### **src** 폴더

\***\*ex03-9.sh\*\***

```sh
dir=$1
if [ ! -d $dir ]; then
    mkdir $dir
fi
cd $dir
for ((i=0;i<5;i++))
do
	newdir="$dir$i"
	mkdir $newdir
	fname="$dir$i.txt"
	touch $fname
done
for ((i=0;i<5;i++))
do
	location="$dir$i.txt"
	todir="$dir$i/$location"
	ln -Tfs $location $todir
done
```

### doc 폴더

#### 오픈소스기초설계를 위한 개별 제안서 **Word 파일**로 업로드

1. 주제 : 노약자분들을 위한 약 관리 앱
2. 약물을 복용할 때 도움을 주기 위한 앱으로 배리어프리적인 시선에서 처음 출발한 아이디어 입니다. 본 앱은 본인이 먹는 약물을 앱에 등록해두고 약을 먹어야 하는 시간에 알림을 보내주어 약을 먹는 것을 잊어버리지 않고 먹도록 도움을 주는 것을 목표로 하고 있습니다. 약을 등록하여 미리 알림으로 알려주고, 노약자분들을 위한 기능으로 혼자 앱을 사용하는 부분에 어려움을 겪는 분들을 위하여 보호자가 등록을 대신 해주면 다른 설정 필요 없이 바로 사용할 수 있다는 것이 다른 앱들에 비해 이 아이디어가 가지는 장점입니다.

#### 3번째 과제: Shell Script (10/28까지)

프로그래밍(20221806, 이정원).docx 파일로 업로드
