# Baekjoon-Edition

본 레포지터리는 자기개발을 목적으로 운영합니다.

알고리즘 트레이닝 웹사이트 [Baekjoon OJ](https://www.acmicpc.net/) 문제의 코드를 모은 레포지터리입니다.

***

## 파일 구조

```bash
├── 00000 문제 제목
│   ├── examples.json
│   └── code.py
==============================  
├── driver.py
└── path.json
```
* **examples.json** 입출력 예제 샘플.
* **driver.py** 입출력 만족 여부 확인용 실행 프로그램.
* **path.json** 문제, 프로그래밍 언어에 따라 구성한 소스 코드의 경로 매칭 목록.

***

## 문제 프로그램 실행
```
python3 driver.py <문제 번호>ㄴ
```