# Wearable Neuropsychology Lab

웨어러블 생체신호와 신경심리학적 맥락을 결합해, 사용자의 상태를 단정적으로 진단하지 않으면서 **자기 인식과 저위험 심리 중재를 보조하는 AI 모델**을 연구하는 프로젝트입니다.

> 이 프로젝트는 연구·교육·웰빙 보조를 목적으로 합니다. 의료 진단, 응급 판단, 치료 대체를 목적으로 하지 않습니다.

## 1. 연구 목표

다음 질문을 단계적으로 검증합니다.

1. PPG, ECG, EDA, 호흡, 움직임 등의 신호로 개인의 평상시 기준선에서 벗어난 변화를 안정적으로 포착할 수 있는가?
2. 생체신호, 자기보고, 활동 맥락을 함께 사용하면 스트레스·각성 상태 추정의 불확실성을 줄일 수 있는가?
3. 모델이 충분히 확신할 때만 호흡, 짧은 움직임, 휴식 같은 저위험 선택지를 제안하고 이후 변화를 재측정할 수 있는가?
4. 피부색, 성별, 연령, 기기와 착용 방식이 달라도 성능과 오류가 공정하게 유지되는가?

이 프로젝트에서 모델이 출력해야 할 것은 “당신은 불안장애입니다” 같은 진단이 아니라 다음과 같은 **확률적이고 설명 가능한 상태 보조 정보**입니다.

- 현재 신호 품질
- 개인 기준선 대비 변화량
- 각성 또는 부담 증가 가능성 및 불확실성
- 판단에 사용한 센서와 맥락
- 지금 선택할 수 있는 저위험 행동
- 판단 보류(abstention) 또는 추가 자기보고 요청

## 2. 시스템 개념

```text
Wearable sensors
PPG / ECG / EDA / respiration / IMU / optional EEG
        │
        ▼
Signal quality & preprocessing
artifact detection / filtering / synchronization / missing data
        │
        ▼
Signal encoders
PaPaGei or NormWear / NeuroKit2 features / optional EEGNet
        │
        ├──────────────┐
        ▼              ▼
Context encoder    Self-report encoder
activity, time     perceived stress, mood, sleep
        └──────┬───────┘
               ▼
Multimodal fusion & calibration
personal baseline / uncertainty / fairness checks
               │
               ▼
Consent-aware support policy
explain / ask / abstain / suggest a low-risk action
               │
               ▼
Reassessment loop
did the signal and self-report improve?
```

fMRI는 실시간 입력 센서가 아니라, 스트레스 회복과 뇌 네트워크에 관한 가설을 세우고 EEG·말초생리 지표를 검증하기 위한 **오프라인 연구 근거**로만 취급합니다.

## 3. 센서와 해석 범위

| 신호 | 얻을 수 있는 정보 | 중요한 한계 |
|---|---|---|
| PPG | 심박, 박동 간 간격, HRV 대리지표 | 움직임, 접촉, 피부 특성, 기기 차이에 민감 |
| ECG | 심박과 HRV의 비교적 정밀한 측정 | 일상 착용성이 낮고 전극 품질의 영향을 받음 |
| EDA/GSR | 교감신경계 각성 변화 | 특정 감정이나 원인을 직접 구분하지 못함 |
| 호흡 | 호흡수, 호흡 주기, 호흡-심박 결합 | 센서가 없으면 PPG 기반 추정 오차가 커질 수 있음 |
| IMU | 활동량, 자세 변화, PPG 동작 잡음 탐지 | 심리 상태 자체를 나타내지는 않음 |
| EEG | 뇌 전기활동의 시간적 변화 | 소비자 기기는 채널과 신호 품질이 제한적이며 잡음이 큼 |
| 자기보고 | 사용자가 지각한 스트레스와 맥락 | 회상·응답 편향이 있으나 생체신호의 의미를 정하는 핵심 자료 |

코르티솔과 세로토닌 농도는 일반적인 손목형 웨어러블 신호나 대화만으로 직접 측정할 수 없습니다. 모델은 이를 사실처럼 추정하거나 표시하지 않습니다.

## 4. 조사한 공개 모델과 도구

### 권장 우선순위

| 우선순위 | 모델·도구 | 역할 | 이 프로젝트에서의 판단 |
|---|---|---|---|
| 1 | [PaPaGei](https://github.com/nokia-bell-labs/papagei-foundation-model) | PPG 사전학습 인코더 | 공개 코드·가중치가 있고 PPG 기준선 구축에 적합. 우선 frozen embedding으로 사용 |
| 1 | [NeuroKit2](https://github.com/neuropsychology/NeuroKit) | ECG, PPG, EDA, 호흡 전처리와 특징 추출 | 해석 가능한 HRV·EDA 특징 기반 기준선에 사용 |
| 2 | [NormWear](https://huggingface.co/mosaic-laboratory/normwear) | PPG, ECG, EEG, GSR, IMU 멀티모달 파운데이션 모델 | 센서가 늘어날 때 PaPaGei와 비교할 핵심 후보. 약 0.2B 규모, Apache-2.0 |
| 2 | [Contrastive stress model](https://github.com/comp-well-org/clip-stress-detection) | 웨어러블 시계열, 설문, 맥락 텍스트 정렬 | MND-N 같은 대화형 보조자와 연결할 때 참고할 융합 구조 |
| 3 | [Pulse-PPG](https://github.com/maxxu05/pulseppg) | 실험실과 일상 환경을 함께 고려한 PPG 인코더 | 실제 환경 일반화 비교용 후보 |
| 3 | [EEGNet](https://arxiv.org/abs/1611.08024) | 소형 EEG 분류 기준선 | EEG를 시작할 때 거대 모델보다 먼저 사용할 가벼운 기준선 |
| 4 | [LaBraM](https://github.com/935963004/LaBraM) | 대규모 EEG 표현학습 | 데이터·연산·신호 품질을 확보한 뒤 연구 비교용으로 사용 |
| 참고 | [HeartBEiT](https://github.com/akhilvaid/HeartBEiT) | 대규모 ECG 표현학습 | 임상 ECG 중심이므로 초기 웰빙 MVP의 주 모델로는 사용하지 않음 |

EEG 모델 실험은 [Braindecode](https://braindecode.org/stable/index.html)의 PyTorch/MNE 기반 구현을 활용합니다.

### 현재의 모델 결정

첫 구현은 아래 조합으로 시작합니다.

```text
WESAD
  ├─ NeuroKit2 features ──> Logistic Regression / XGBoost baseline
  └─ PPG ──> frozen PaPaGei embeddings ──> calibrated classifier

Compare:
  PaPaGei vs handcrafted features vs feature+embedding fusion

Next:
  NormWear for PPG + EDA + ECG/IMU multimodal encoding
```

파운데이션 모델을 처음부터 재학습하지 않습니다. 먼저 공개 가중치를 고정한 특징 추출기로 사용하고, 작은 분류기나 회귀기만 학습합니다. 이 방식은 데이터 누수와 과적합을 더 쉽게 확인하고 비용도 낮춥니다.

## 5. 데이터셋 후보

| 데이터셋 | 신호와 라벨 | 사용 계획 | 주의점 |
|---|---|---|---|
| [WESAD](https://archive-beta.ics.uci.edu/dataset/465/wesad%2Bwearable%2Bstress%2Band%2Baffect%2Bdetection) | 손목·가슴 BVP/PPG, ECG, EDA, EMG, 호흡, 체온, 가속도; 중립·스트레스·즐거움 | 첫 재현 실험 | 15명 규모의 실험실 데이터이므로 일반화 주장 금지 |
| [AMIGOS](https://eecs.qmul.ac.uk/mmv/datasets/amigos/) | EEG, ECG, GSR, 영상; valence/arousal와 성격·기분·사회 맥락 | 정서·사회 맥락 융합 연구 | 영상 유발 감정이 일상 스트레스와 같지 않음 |
| [DREAMER](https://doi.org/10.1109/JBHI.2017.2688239) | 휴대형 EEG·ECG; valence/arousal/dominance | EEG-ECG 결합 비교 | 소규모이며 데이터 접근 조건 확인 필요 |
| [LifeSnaps/PMData 기반 연구](https://proceedings.mlr.press/v287/yang25a.html) | 웨어러블, 설문, 생활 맥락 | 대조학습 구조 재현 검토 | 데이터별 동의·라이선스와 라벨 정의 확인 필요 |

초기 실험은 WESAD 하나로 제한하고, 파이프라인과 평가가 재현된 뒤 데이터셋을 추가합니다.

## 6. 기술 스택

- Python 3.11
- PyTorch: 신호 인코더와 멀티모달 모델
- NeuroKit2: ECG, PPG, EDA, 호흡 처리
- MNE-Python + Braindecode: 선택적 EEG 처리와 모델 비교
- scikit-learn / XGBoost: 해석 가능한 기준선
- NumPy / Polars 또는 Pandas: 데이터 처리
- MLflow: 실험·지표·모델 버전 기록(후속 단계)
- DVC 또는 데이터 manifest: 원본 데이터와 파생 데이터의 계보 관리(후속 단계)
- ONNX Runtime: 경량 추론 검증(후속 단계)
- FastAPI: 동의된 신호만 받는 로컬 API 프로토타입(후속 단계)

NVIDIA NIM의 생성형 언어 모델은 신호를 직접 진단하는 모델이 아니라, 검증된 상태 요약을 사용자에게 이해하기 쉽게 설명하고 질문을 이어 가는 **대화 계층**으로만 분리합니다.

## 7. 평가 원칙

### 데이터 분할

- 동일 사용자의 창(window)이 학습과 시험에 동시에 들어가지 않도록 합니다.
- WESAD에서는 leave-one-subject-out 또는 엄격한 subject-independent split을 기본으로 합니다.
- 전처리 통계와 개인 기준선은 시험 데이터 전체를 미리 보지 않고 계산합니다.

### 지표

- 분류: macro-F1, balanced accuracy, AUROC, sensitivity, specificity
- 확률 신뢰도: Brier score, expected calibration error, reliability plot
- 개인화: 개인 기준선 적용 전후 성능과 적응에 필요한 시간
- 실사용: 신호 품질 실패율, 판단 보류율, 지연시간, 배터리 비용
- 공정성: 피부 특성, 기기, 성별, 연령대별 오류 차이
- 안전성: 거짓 경보, 거짓 안심, 맥락을 무시한 중재 제안 횟수

정확도 하나만으로 모델을 선택하지 않습니다. 확신이 낮거나 신호가 나쁘면 **판단하지 않는 능력**도 성능으로 평가합니다.

## 8. 단계별 로드맵

### Phase 0 — 연구 규약

- 데이터 사전, 센서 단위, 샘플링률, 시간 동기화 형식 정의
- 증거 레지스트리와 모델 카드 양식 작성
- 동의, 보관 기간, 삭제, 익명화 정책 정의

### Phase 1 — 재현 가능한 기준선

- WESAD 로더와 subject-independent split 구현
- NeuroKit2 기반 PPG/ECG/EDA/호흡 특징 추출
- Logistic Regression과 XGBoost 기준선 구축
- 데이터 누수 검사와 calibration 평가

### Phase 2 — PPG 파운데이션 모델

- PaPaGei를 frozen encoder로 연결
- handcrafted feature와 embedding을 공정하게 비교
- 움직임과 신호 품질에 따른 성능 저하 측정

### Phase 3 — 멀티모달·개인화

- NormWear로 PPG + EDA + ECG/IMU 표현 비교
- 자기보고와 활동 맥락을 late fusion 또는 contrastive alignment로 결합
- 사용자별 정상 범위를 학습하되 초기 데이터가 적을 때는 판단 보류

### Phase 4 — 폐루프 보조 프로토타입

- 설명 → 사용자 확인 → 저위험 선택지 → 재측정의 순환 구현
- 호흡법은 한 가지 패턴을 강제하지 않고 편안함, 안전성, 반응에 따라 조절
- MND-N/NIM 대화 계층과 신호 모델 사이에 안전 정책과 구조화된 API 배치

### Phase 5 — 선택적 EEG 연구

- EEGNet으로 신호 품질과 기준선 검증
- 데이터와 연산 근거가 확보된 경우에만 LaBraM 등 파운데이션 모델과 비교
- fMRI 연구 결과는 EEG 가설 설정에만 사용하고 실시간 추정값으로 가장하지 않음

## 9. 안전·윤리 원칙

- 진단명, 호르몬 농도, 자살 위험을 웨어러블 신호만으로 확정하지 않습니다.
- 사용자가 알지 못하는 상시 감시나 원시 신호 전송을 기본값으로 두지 않습니다.
- 가능한 한 기기 내부 또는 로컬에서 전처리하고, 필요한 최소 데이터만 저장합니다.
- 원시 데이터, 특징, 자기보고, 모델 출력의 보관과 삭제 권한을 분리합니다.
- 모델의 권고보다 사용자의 자기보고와 거부 의사를 우선합니다.
- 위기 상황은 생성형 모델의 임의 상담으로 처리하지 않고 별도의 안전 절차와 전문 지원 경로로 연결합니다.
- 연구 결과는 데이터셋·기기·대상 집단의 범위를 넘겨 일반화하지 않습니다.

## 10. 제안 디렉터리 구조

```text
wearable/
├── README.md
├── docs/
│   ├── research-questions.md
│   ├── evidence-registry.md
│   ├── data-governance.md
│   └── model-card-template.md
├── configs/
├── src/
│   ├── data/
│   ├── signals/
│   ├── models/
│   ├── fusion/
│   └── policy/
├── tests/
└── runtime/                 # 로컬 데이터·체크포인트, Git 제외
```

## 11. 다음 작업

1. WESAD 라이선스와 원본 파일 구조를 확인하고 데이터 manifest를 작성합니다.
2. Phase 1 실험의 입력 신호를 손목 BVP/EDA/ACC로 제한해 작은 기준선을 만듭니다.
3. subject-independent split과 누수 방지 테스트를 코드보다 먼저 고정합니다.
4. PaPaGei 가중치를 내려받아 frozen embedding 추출 시간을 측정합니다.
5. 같은 split에서 NeuroKit2 기준선과 PaPaGei를 비교합니다.

## 12. 핵심 참고 자료

- PaPaGei: [paper](https://arxiv.org/abs/2410.20542) · [official code](https://github.com/nokia-bell-labs/papagei-foundation-model)
- NormWear: [paper](https://arxiv.org/abs/2412.09758) · [model](https://huggingface.co/mosaic-laboratory/normwear) · [official code](https://github.com/Mobile-Sensing-and-UbiComp-Laboratory/NormWear)
- Pulse-PPG: [paper](https://arxiv.org/abs/2502.01108) · [official code and weights](https://github.com/maxxu05/pulseppg)
- Multimodal stress contrastive pretraining: [paper](https://proceedings.mlr.press/v287/yang25a.html) · [official code](https://github.com/comp-well-org/clip-stress-detection)
- HeartBEiT: [paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10242218/) · [official code](https://github.com/akhilvaid/HeartBEiT)
- EEGNet: [paper](https://arxiv.org/abs/1611.08024)
- LaBraM: [paper](https://arxiv.org/abs/2405.18765) · [official code](https://github.com/935963004/LaBraM)
- WESAD: [UCI dataset](https://archive-beta.ics.uci.edu/dataset/465/wesad%2Bwearable%2Bstress%2Band%2Baffect%2Bdetection) · [original paper](https://doi.org/10.1145/3242969.3242985)
- Slow breathing and autonomic outcomes: [systematic review and meta-analysis](https://pubmed.ncbi.nlm.nih.gov/35623448/)
- 4-7-8 breathing comparison: [study](https://doi.org/10.1007/s10484-025-09688-z)
- EEG-informed fMRI neurofeedback and stress resilience: [study](https://pubmed.ncbi.nlm.nih.gov/30932053/)

---

**Initial decision:** build a trustworthy, subject-independent baseline with **WESAD + NeuroKit2 + PaPaGei**, compare **NormWear** for multimodal sensing, and add EEG only after the wearable pipeline is reliable.
