# 🚀 Python 학습 저장소
Python 프로그래밍 기초부터 객체지향까지  
체계적인 학습을 위한 단계별 튜토리얼과 실습 프로젝트를 포함한 학습 환경입니다.

---

## 📚 저장소 구조
- 📖 **학습 문서 (`learning_logs/`)**  
  - 일별 학습 기록 & 개념 정리
- 🎯 **실습 프로젝트 (`Practice/`)**  
  - 실제 구현 예시: 계산기, 주사위 게임 등
- 📝 **튜토리얼 챕터 (`ch00_starting/`, `ch03_indexing/`, `ch06_collections/`)**  
  - 단계별 Python 학습

---

## 🚀 Python 실습 프로젝트 전체 목록

### 📚 도서 관리 시스템 (`Practice/BookManager/`)
- 메인 UI: 8가지 메뉴 옵션 제공 콘솔 인터페이스 → `bookmanager.py:3-7`
- 비즈니스 로직: 책 추가, 제거, 구매, 검색, 재고 관리 → `bmfunction.py:5-17`
- 데이터 구조: 딕셔너리 기반 인메모리 도서 재고 관리 → `bmfunction.py:3`

### 🃏 블랙잭 게임 (`Practice/BlackJack/`)
- 게임 로직: 플레이어 vs 딜러 카드 게임 구현 → `blackjack.py:62-86`
- 덱 생성: 52장 표준 카드덱 생성 (이모지 포함) → `createDeck.py:1-26`
- 점수 계산: 블랙잭 규칙에 따른 자동 점수 계산 → `blackjack.py:17-21`

### 🎲 주사위 시뮬레이터 (`Practice/Dice/`)
- 확률 시뮬레이션: 10만회 주사위 게임 실행 → `dice.py:7-9`
- 통계 분석: 승률, 패배율, 무승부율 계산 → `dice.py:24-27`
- 데이터 시각화: matplotlib을 이용한 바차트 생성 → `dice.py:30-32`

### 🎰 로또 번호 생성기 (`Practice/Lotto/`)
- 번호 생성: 1-45 범위에서 중복 없는 6개 번호 생성 → `lotto.py:5-8`
- 사용자 입력: 유효성 검사가 포함된 번호 입력 시스템 → `lotto.py:13-21`
- 당첨 확인: 맞춘 개수에 따른 등수 계산 → `lotto.py:29-36`

### 🧮 계산기 (`Practice/Calculator/`)
- 수식 파싱: 문자열 입력을 숫자와 연산자로 분리 → `calculator.py:7-14`
- 사칙연산: 덧셈, 뺄셈, 곱셈, 나눗셈 구현 → `calculator.py:23-30`
- 오류 처리: 잘못된 입력값 검증 → `calculator.py:18-22`

### ✂️ 가위바위보 게임 (`Practice/RockScissorsPaper/`)
- 게임 로직: 가위바위보 승부 판정 함수 → `rsp.py:9-16`
- 대량 시뮬레이션: 100만회 게임 실행으로 확률 분석 → `rsp.py:7`
- 통계 출력: 승률 계산 및 결과 표시 → `rsp.py:27-30`

### 🏦 은행 계좌 관리 프로그램 (`Practice/BankAccountUser/`)
* 계좌 생성 및 관리: Bank 클래스
* 사용자 관리: User 클래스
* 계좌 기능: Account 클래스
* 시뮬레이션 실행: 계좌 생성, 입출금, 보고서 출력, 계좌 폐쇄

### 🎰 로또 계산기 (`Practice/LottoCalculator/`)
* 로또 번호 생성: `generate_lotto()`
* 시뮬레이션 및 당첨 판정: `simulate_lotto()`
* 결과 시각화: 바 차트 출력
* 시뮬레이션 실행

### 🎩 몬티홀 문제 시뮬레이터 (`Practice/MontyHall/`)
* 초기 설정 및 변수 선언
* 염소 공개/선택 유지 및 변경 시뮬레이션
* 염소 비공개/선택 유지 및 변경 시뮬레이션
* 확률 계산 및 결과 시각화
---

## 📊 프로젝트 특징 요약

| 프로젝트 | 주요 기술 | 학습 포인트 |
|-----------|-----------|-------------|
| BookManager | 딕셔너리, 모듈화 | CRUD 연산, 데이터 관리 |
| BlackJack   | 객체지향, 게임 로직 | 상태 관리, 조건문 |
| Dice        | 확률, 시각화 | 반복문, matplotlib |
| Lotto       | 랜덤, 유효성 검사 | 입력 처리, 중복 제거 |
| Calculator  | 문자열 처리 | 파싱, 예외 처리 |
| RockScissorsPaper | 함수, 시뮬레이션 | 함수 설계, 통계 |

---

## 🛠️ 개발 환경
- IDE: PyCharm 또는 VS Code  
- 언어: Python 3.x  
- 라이브러리: `matplotlib` (데이터 시각화)  
- Python 프로그래밍 기초부터 실전까지의 성장 과정을 보여주는 학습용 저장소
