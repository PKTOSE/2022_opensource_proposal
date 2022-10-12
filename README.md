# 2022_opensource_proposal

<img src="https://img.shields.io/github/issues/PKTOSE/2022_opensource_proposal">
<img src="https://img.shields.io/github/forks/PKTOSE/2022_opensource_proposal">
<img src="https://img.shields.io/github/stars/PKTOSE/2022_opensource_proposal">
<img src="https://img.shields.io/github/license/PKTOSE/2022_opensource_proposal">
<img src="https://img.shields.io/badge/Python-#3776AB?style=flat&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/opensource-%EC%98%A4%ED%94%88%EC%86%8C%EC%8A%A4%EA%B8%B0%EC%B4%88%EC%84%A4%EA%B3%84__%EA%B0%9C%EB%B3%84%EC%A0%9C%EC%95%88%EC%84%9C-brightgreen">

2022년도 오픈소스기초설계 개별 제안서 업로드용 깃허브

## 과제 내용

> - Github 페이지 생성, public으로 전체 공개 (5점)
> - Github 페이지의 라이선스 형태 명시 (2점)
> - 폴더 생성: src/ --> 폴더 안에 프로그래밍 파일 1개 이상 업로드 (2점)
> - 폴더 생성: doc/ --> 폴더 안에 프로젝트 제안서 업로드 (2점)
> - 파일 수정: src/ --> 폴더 안에 파일 내용 수정 commit & push 1회 이상 (2점)
> - Github 페이지의 README.md 생성 (2점)
> - Github 페이지의 README.md 편 --> 5개 이상의 문법 요소 활용 (5점)
>   e.g. 내용 작성, 문서 제목, 항목 열거, 문단 강조/나눔, 폰트 크기/스타일 변경, 링크 삽입 등

### **src** 폴더

**distribute.py**
아직까지 관련 소스코드가 없어서 이산수학 과제를 업로드 하였습니다(추후 관련된 소스코드가 생긴다면 수정할 계획입니다).

```python
average = 0


def recur_variance(arr: tuple, avg=1):
    if avg == 1:
        global average
        average = sum(arr) / len(arr)
    if len(arr) == 1:
        return (arr[-1] - avg) ** 2
    length = len(arr)
    mid = length // 2
    Y = arr[:mid]
    Z = arr[mid:]
    return (recur_variance(Y, average) * mid + recur_variance(Z, average) * (length - mid)) / length

```

위의 코드는 주어진 튜플을 재귀함수를 이용하여 분산을 구하는 코드이다.
