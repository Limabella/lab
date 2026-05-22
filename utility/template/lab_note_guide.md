# 실험노트 작성 가이드

> 목적:
> 연구 과정, 실험 설정, 실패 사례, 결과를 재현 가능하게 기록한다.

> 나만의 잘하는 과정:
> 1. lab:  연구 논문 & 자료 참고 -> 보드에 그림으로 그려보기 -> 그림과 캡션으로 기록 
> 2. lab_note: 문제 의식 (R&D) -> 연구 노트 작성 -> 데이터셋 실험 -> 결과 기록
> 3. paper: 학술 논문 작성 or 연구 논문(research paper) 작성

> 논문 작성법:
> ....
---

# 작성 원칙

## 1. 한 문서 = 한 실험

실험 하나당 문서 하나를 사용한다.

좋은 예:

```text id="y5tx3x"
exp_001.md
exp_002.md
exp_003.md
```

나쁜 예:

```text id="1ws67r"
여러 실험을 하나의 md 파일에 혼합
```

---

## 2. "결과"보다 "변경점"을 기록한다

실험 기록에서 가장 중요한 것은:

- 무엇을 바꿨는가?
- 왜 바꿨는가?
- 어떤 차이가 발생했는가?

이다.

예시:

```text id="29pb4m"
해상도를 224 → 448로 증가
→ hallucination 감소 확인
```

---

## 3. 실패 실험도 반드시 기록한다

실패 사례는 이후 반복 실험을 줄여준다.

반드시 기록할 것:

- 학습 불안정
- 성능 하락
- 이상 출력
- 메모리 문제
- hallucination

---

## 4. 짧고 구조적으로 작성한다

긴 설명보다:

- 표
- bullet
- 짧은 observation

형태를 우선한다.

좋은 예:

```text id="2yy9ua"
- caption quality improved
- object count error reduced
- training became unstable after epoch 3
```

---

# 추천 작성 흐름

## Step 1. 목표 작성

```text id="aqg1pt"
BLIP와 LLaVA caption quality 비교
```

---

## Step 2. 변경점 기록

```text id="qvmy6z"
- resolution 224 → 448
- batch size 감소
```

---

## Step 3. 결과 기록

```text id="9j8r2v"
CIDEr +2.1
hallucination 감소
```

---

## Step 4. 관찰 내용 작성

```text id="6d6w8y"
고해상도에서 alignment가 더 안정적이었음
```

---

# 권장 폴더 구조

```text id="1x0b4d"
research/
├── templates/
│   └── 실험노트_템플릿.md
│
├── experiments/
│   ├── exp_001.md
│   ├── exp_002.md
│   └── exp_003.md
│
├── assets/
│   └── exp_001/
│       ├── result.png
│       └── graph.png
│
└── README.md
```

---

# 이미지 사용 규칙

실험 결과 이미지는 assets 폴더에 저장한다.

예시:

```text id="mjlwm8"
assets/exp_001/result.png
```

Markdown 사용:

```md id="73qh0z"
![result](../assets/exp_001/result.png)
```

---

# 논문 작성용 팁

## 1. Observation을 가장 중요하게 작성한다

논문에서는 단순 score보다:

- 왜 성능이 좋아졌는가
- 어떤 failure case가 있는가

가 더 중요하다.

---

## 2. 비교 가능한 형태로 기록한다

좋은 예:

| 설정 | 결과 |
|---|---|
| 224 | hallucination 발생 |
| 448 | hallucination 감소 |

---

## 3. 재현 가능성을 유지한다

반드시 기록:

- 모델 버전
- 데이터셋
- resolution
- learning rate
- prompt

---

# 추천 Git Commit 방식

```bash id="g1mjlwm"
git commit -m "exp001: increase resolution to 448"
```

좋은 commit은:

- 어떤 실험인지
- 무엇을 바꿨는지

가 드러나야 한다.

---

# 추천 상태 관리

| 상태 | 의미 |
|---|---|
| planned | 실험 예정 |
| ongoing | 진행 중 |
| done | 완료 |
| failed | 실패 |
| archived | 보관 |

---

# 좋은 실험노트의 특징

좋은 실험노트는:

- 짧고
- 구조적이고
- 비교 가능하고
- 재현 가능해야 한다.

논문 초안 작성 시:
실험노트 → 결과 정리 → 논문 표/분석

순서로 그대로 이어질 수 있어야 한다.