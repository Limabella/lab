# Research Papers Log

---

## Agent

- [2026-05-18] [Toolformer](https://arxiv.org/abs/2302.04761)
  - LLM의 tool-use 능력을 self-supervised 방식으로 학습
  - API 호출 and 외부 도구 활용을 모델 내부에 통합
  - Hermes Agent tool orchestration 구조 참고용

---

## Language

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
  - Transformer architecture 제안
  - Self-attention 기반 구조
  - 현대 LLM 구조의 기반 논문
  - 향후 agent memory 구조와 연결 가능

---

## Vision

- [2023-03] [Vision Transformer with Quadrangle Attention](https://arxiv.org/abs/2303.15105?utm_source=copilot.com)
  - 고정된 window attention을 일반화한 Quadrangle Attention(QA) 기반의 Q-Former 아키텍처를 제안함.
  - 다양한 크기·형태·방향의 객체에 적응적으로 attention 영역을 생성하여 이미지 분류, 객체 탐지, 의미 분할, 포즈 추정 등 여러 비전 태스크에서 성능 향상을 달성함.
  - learnable transformation matrix를 활용해 유연한 receptive field를 형성하고, 기존 shifted window 방식 대비 더 풍부한 문맥 정보를 학습할 수 있음을 보임.

- [Segment Anything](https://arxiv.org/abs/2304.02643)
  - Meta의 범용 segmentation foundation model
  - Promptable segmentation 구조 제안
  - 멀티모달 perception 시스템 연구 참고용

---

## Robotics

- [RT-2](https://arxiv.org/abs/2307.15818)
  - Vision-Language-Action(VLA) 모델
  - 웹 지식과 로봇 행동을 연결
  - 멀티모달 robotics agent 연구 핵심 사례

---

## Multimodal AI

- [2026-05-18] [Multi-emotion and intensity-driven response generation for richer multimodal dialogue](https://www.nature.com/articles/s41598-026-41034-z?utm_source=copilot.com)
  - 입력 문장의 감정 강도와 종류를 인식해 다층적 반응을 생성하는 방법 제안
  - 표층 반응과 심층 상태를 분리해 조정하는 구조 ("양파 로직"과 유사)
  - 감정 벡터 기반으로 멀티모달 대화 시스템의 풍부한 반응을 구현

- [2026-05-18] [Nous Research — Token Superposition](https://nousresearch.com/token-superposition?utm_source=chatgpt.com)
  - Token Superposition Training(TST) 공식 기술 설명
  - sparse activation 및 representation overlap 개념 설명
  - 차세대 효율적 pretraining 접근 방식 참고 자료

- [2026-05-07] [Efficient Pre-Training with Token Superposition](https://arxiv.org/abs/2605.06546)
  - Nous Research 제안
  - 토큰 슈퍼포지션(TST) 기법으로 학습 효율 향상
  - 10B 규모 모델에서 최대 2.5배 학습 시간 단축
  - 긴 컨텍스트 및 메모리 효율 연구와 연결 가능

- [2026-04-15] [Aurora: Towards Universal Generative Multimodal Time Series Forecasting](https://openreview.net/forum?id=aurora2026)
  - ICLR 2026 발표
  - 멀티모달 시계열 foundation model Aurora 제안
  - 텍스트·이미지·시계열을 결합한 범용 예측 구조

- [2025-09-30] [90% Faster, 100% Code-Free: MLLM-Driven Zero-Code 3D Game Development](https://arxiv.org/abs/2509.26161?utm_source=chatgpt.com)
  - 자연어 요구사항으로부터 코딩 없이 실행 가능한 3D 게임을 생성하는 멀티 에이전트 프레임워크 UniGen 제안
  - Planning, Generation, Automation, Debugging 에이전트 간의 협업 체계를 통해 Unity 및 Unreal 엔진 기반 프로젝트를 자동 구축
  - 사용자 코딩 없이도 복잡한 게임 로직과 상태 관리를 처리하며, 기존 방식 대비 개발 시간을 91.4% 단축

- [2024-11-29] [A Survey on Multimodal Large Language Models](https://arxiv.org/abs/2306.13549)
  - GPT-4V 이후 급격히 발전한 멀티모달 LLM 연구를 종합적으로 정리한 서베이 논문
  - 아키텍처, 학습 전략, 평가, 확장 방향 논의

- [2024-09] [Efficient Visual-Language Alignment of the Q-Former](https://arxiv.org/abs/2410.09489?utm_source=copilot.com)
  - BLIP-2, InstructBLIP에서 사용되는 Q-Former의 효율적 파인튜닝(PEFT) 연구
  - 전체 파라미터의 2% 미만만 학습해도 풀 파인튜닝과 유사한 성능 달성
  - AdaLoRA 기법으로 Q-Former 내부 서브레이어 중요도 분석
  - Self-attention 레이어가 시각-언어 추론에서 핵심적 역할을 한다는 결과

---

## Neuroscience

- [2026-03-31] [Neural signatures of human psychological resilience driven by acute stress](https://doi.org/10.1073/pnas.2524075123)
  - 급성 스트레스 노출 후 1.5시간 동안 fMRI, EEG, 말초 생리신호를 함께 측정해 인간의 심리적 회복탄력성과 관련된 신경생리학적 변화를 분석
  - 스트레스 직후보다 약 1시간 뒤에 회복탄력성 차이를 나타내는 지연된 신경 동역학이 두드러짐
  - 회복탄력성이 낮은 집단에서는 피질 현저성 네트워크 활성과 high-beta·gamma 파워가 증가하고, 높은 집단에서는 기본모드 네트워크와 후방 해마의 자발적 활성이 증가
  + 웨어러블 모델(시계열 데이터셋) - 프로젝트에서 스트레스 순간값뿐 아니라 회복 궤적과 시간 지연을 모델링하는 근거로 활용 가능

---

## Wearable

- [2026-04] [Enabling Adaptive Cardio-Respiratory Biofeedback Training on Ubiquitous Hand-Worn Devices](https://doi.org/10.1145/3772318.3790488)
  - 스마트워치와 스마트링의 PPG·IMU를 이용해 심박·호흡 지표를 동시에 추정하는 손 착용형 심폐 바이오피드백 시스템 제안
  - 사용자가 손을 복부에 올리는 상호작용과 실시간 HRV·호흡 정렬 상태를 결합해 호흡 안내 속도를 폐루프 방식으로 개인화
  - 고정 속도 안내와 비교해 지속적인 HRV, 안내 호흡과의 정렬, 참여 경험을 개선하는 적응형 설계를 평가
  + 웨어러블 모델(센서와 바이오피드백) - 프로젝트의 센서 융합, 적응형 호흡 중재, 중재 후 재측정 루프 설계에 가용할 사례

---

## Psychology & Bias

### Flourishing / Positive Psychology


- [2025] [Global Flourishing Study](https://hfh.fas.harvard.edu/global-flourishing-study)
  - Harvard Human Flourishing Program이 주도하는 대규모 국제 플로리싱 연구
  - 22개국, 20만 명 이상을 대상으로 인간 번영의 분포와 결정 요인을 장기 추적하는 패널 연구
  - 행복, 건강, 의미, 성격/덕성, 관계, 경제 안정성 등 다차원적 플로리싱 영역을 포함

- [2026] [GPT-Powered Chatbot-Based Positive Psychology Intervention](https://formative.jmir.org/2026/1/e85060)
  - GPT 기반 챗봇을 활용한 Positive Psychology Intervention(PPI) 연구
  - 감사(Gratitude), 강점(Strengths), 의미(Meaning) 중심 활동 제공
  - AI가 긍정심리학 개입을 개인화하여 수행할 수 있음을 검증

- [2025/2026] [The “Web Browser” of the Collective Unconscious: The Mirror and Oracle of Generative AI](https://link.springer.com/article/10.1007/s12115-026-01193-1?utm_source=copilot.com)
  - 생성형 AI를 집단무의식의 거울·오라클로 해석
  - Midjourney 같은 이미지 생성 AI가 상징적 어휘를 재구성하며 새로운 의미를 창출
  - 윤리적 문제(데이터 편향, 저작권, 신뢰성) 논의

- [2025-12-11] [The Algorithmic Unconscious: Structural Mechanisms and Implicit Biases in LLMs](https://hal.science/hal-2025)
  - 토큰화·어텐션·정렬 과정에서 발생하는 구조적 편향 분석
  - "알고리즘적 무의식" 개념 제안
  - LLM alignment와 bias 연구 참고용

- [2025-10-18] [Reading Minds, Sparking Ideas: How Machiavellian Leaders Boost Team Creativity Through Cross-Understanding](https://www.mdpi.com/2076-3387/15/10/400)  
  - 마키아벨리적 리더십이 팀 창의성을 촉진할 수 있음을 실증적으로 검증  
  - **교차 이해(cross-understanding)**: 팀원들이 서로의 지식·관점·사고방식을 이해하는 과정이 창의성의 매개 역할  
  - **과업 상호의존성(task interdependence)**: 팀 과제가 서로 긴밀히 연결될수록 리더의 긍정적 효과가 강화됨  
  - 사회학습이론(Social Learning Theory)과 특성활성화이론(Trait Activation Theory)을 기반으로 분석  
  - 중국 기술·제조·금융 기업의 86개 팀(379명)을 대상으로 다원적 설문조사 진행  
  - 실무적 시사점: 조직은 마키아벨리적 리더의 야망을 혁신 목표에 맞추고, 교차 이해를 촉진하는 협업 구조를 설계해야 함  

- [2025-03-01] [공감과 공격성의 관계: 어두운 4요소 성격의 매개효과](https://doi.org/10.0000/kjhp.2025.31.2.429)
  - 한국심리학회지
  - 공감과 공격성의 간접 관계 분석
  - 사이코패시·사디즘 매개효과 확인
- [2023] [공감과 공격성의 관계: 어두운 4요소 성격의 매개효과](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003316966&utm_source=copilot.com)
  - 공감(Empathy)이 공격성(Aggression)에 미치는 영향을 어두운 성격 요인(Dark Tetrad: 마키아벨리즘, 나르시시즘, 사이코패시, 사디즘)을 매개로 분석
  - 구조방정식 모형(SEM)을 통해 공감 → Dark Tetrad → 공격성이라는 간접 경로 규명
  - 공감 수준이 높을수록 사이코패시·사디즘 경로가 약화되어 공격성이 줄어드는 효과 확인

- [2017] [On the promotion of human flourishing](https://doi.org/10.1073/pnas.1702996114)
  - Tyler J. VanderWeele의 인간 플로리싱 확장 모델
  - 행복과 삶의 만족, 정신·신체 건강, 의미와 목적, 인격과 덕성, 가까운 사회적 관계를 핵심 영역으로 제시
  - Harvard Flourishing Measure의 이론적 기반으로 활용 가능
  - Secure Flourish 버전은 경제적·물질적 안정성까지 포함하여 지속 가능한 번영을 측정

- [2016] [The PERMA-Profiler: A brief multidimensional measure of flourishing](https://www.internationaljournalofwellbeing.org/index.php/ijow/article/view/526)
  - Butler & Kern이 제안한 플로리싱 측정도구
  - Seligman의 PERMA 모델을 기반으로 Positive Emotion, Engagement, Relationships, Meaning, Accomplishment를 다차원적으로 측정
  - 부정 정서와 건강 영역도 함께 포함하여 개인의 웰빙 프로파일을 구성할 수 있음

- [2014-02-01] [Narcissism in the Modern World](https://doi.org/10.1080/14753634.2014.894225)
  - Pat MacDonald
  - 현대 사회의 자기애적 성향 확산 분석
  - 문화적·임상적 함의 논의

- [2011] [Flourish: A Visionary New Understanding of Happiness and Well-being](https://www.simonandschuster.com/books/Flourish/Martin-E-P-Seligman/9781439190753)
  - Martin E. P. Seligman의 플로리싱 이론 핵심 저서
  - 웰빙을 단순한 행복감이 아니라 Positive Emotion, Engagement, Relationships, Meaning, Accomplishment로 구성된 PERMA 모델로 설명

- [2009] [New measures of well-being: Flourishing and positive and negative feelings](https://doi.org/10.1007/s11205-009-9493-y)
  - Diener et al.이 Flourishing Scale과 SPANE을 제안한 논문
  - Flourishing Scale은 관계, 유능감, 의미와 목적, 자존감, 낙관성 등 전반적 인간 기능을 8문항으로 간단히 측정
  - 복잡한 PERMA 구조보다 빠르게 “전반적 번영 점수”를 확인하는 데 적합
  + MND 상담사봇에서 사전/사후 변화 점수 또는 간단한 플로리싱 총점 지표로 활용 가능

- [2008-06-01] [Distracted: The Erosion of Attention and the Coming Dark Age](https://prometheusbooks.com)
  - Maggie Jackson 저서
  - 현대 사회의 집중력 붕괴와 기술·문화적 요인 비판

- [2002-12-01] [Bad Boys, Good Mothers, and the “Miracle” of Ritalin](https://doi.org/10.1017/S0269889702000650)
  - ADHD와 리탈린의 사회적·역사적 맥락 분석
  - 진단 및 약물 사용의 문화적 정당화 과정 탐구

---

## Character AI
- [2026-01-15] [Role-Playing Agents Driven by Large Language Models: Current Status, Challenges, and Future Trends](https://arxiv.org/abs/2601.10122)
  - LLM 기반 role-playing agent의 발전 흐름, 핵심 기술, 평가 방법, 한계를 정리한 서베이 논문
  - psychological scale-driven character modeling, memory-augmented prompting, motivation-situation-based behavior control 등을 주요 기술 경로로 설명
  + MoAM 성격 모델링, 메모리 구조, 캐릭터 일관성 평가 기준 참고용

- [2025-07-23] [An LLM-Based Behavior Agent with Natural Language Personality Control: Enabling Trait-Driven NPC Decision-Making through Prompt Engineering](https://etasr.com/index.php/ETASR/article/view/12631)
  - OCEAN(Big Five) 성격 모델을 활용해 NPC의 의사결정과 행동을 제어하는 LLM 기반 게임 NPC 연구
  - NPC traits, game state, environment를 prompt generator로 구성하여 성격 기반 행동을 생성
  + Unity NPC의 성격 기반 행동 제어 및 prompt-driven behavior 설계 참고용

---

## Food

- [2025-07-05] [A chemical language model for molecular taste prediction](https://doi.org/10.1038/s41538-025-00474-z)
  - 15,025개 맛 분자 데이터셋과 사전학습 ChemBERTa를 이용해 SMILES만으로 단맛·쓴맛·신맛·감칠맛 및 undefined를 예측하는 화학 언어모델 FART를 제안
  - SMILES 증강과 예측 합의 기반 confidence metric을 결합한 모델은 테스트셋의 94%를 판정하면서 91.55% 정확도와 0.9806 macro AUROC를 기록
  - Integrated Gradients로 맛 예측에 기여한 원자와 작용기를 시각화하여 식품화학적 해석 가능성을 제공
  - 다중 맛 분자의 단일 라벨화, 입체화학 구분 실패, confidence 적용 시 일부 분자를 판정하지 않는 한계가 있어 성능 수치 해석에 주의 필요

- [2024-10-07] [Digital Fingerprinting of Complex Liquids Using a Reconfigurable Multi-Sensor System with Foundation Models](https://doi.org/10.1002/advs.202407513)
  - 휴대형 다중 화학 센서의 신호를 시각적 fingerprint로 변환하고 사전학습 vision foundation model로 분석하는 IBM HyperTaste 계열 연구
  - 적은 도메인별 학습 데이터로 서로 다른 네 가지 화학 감지 과제를 처리하며, 전문가가 설계한 센서 특징과 대등하거나 더 나은 성능을 제시
  - 센서가 인간처럼 맛을 느끼는 것이 아니라 복합 액체의 다중 신호 패턴을 표현·비교한다는 점에서 전자혀 기반 음식 식별의 방법론적 참고 자료

- [2022-12] [Accelerated estimation of coffee sensory profiles using an AI-assisted electronic tongue](https://doi.org/10.1016/j.ifset.2022.103205)
  - 저선택성 전위차 센서 배열과 머신러닝을 결합해 커피 21종을 평균 정확도 91.3%로 구분
  - 단일 회귀 모델로 13개 관능 묘사의 강도를 동시에 예측하고, 33개 샘플의 관능 프로파일을 0.78 RV coefficient로 재구성
  - 개인 미각 모델이 센서 측정값과 인간의 관능 언어를 연결하는 방법을 설계할 때 직접적인 참고 사례

- [2022-05-04] [Mastication-Enhanced Taste-Based Classification of Multi-Ingredient Dishes for Robotic Cooking](https://doi.org/10.3389/frobt.2022.886074)
  - 혼합으로 저작 과정을 모사하고 여러 위치의 전도도를 측정해 토마토 스크램블에그 9종을 분류하는 로봇 조리 시스템
  - 균질화된 샘플 한 번만 측정했을 때의 F1 0.55에서 혼합 전후 두 상태를 이용했을 때 F1 0.93으로 향상
  - 음식의 공간적 분포와 섭취 과정의 시간 변화를 데이터화한다는 의의가 있지만, 실험은 단일 염도 센서와 제한된 요리 조합에 기반한 개념 증명

- [2019-05-01] [A portable potentiometric electronic tongue leveraging smartphone and cloud platforms](https://doi.org/10.1109/ISOEN.2019.8823244)
  - 이온 감응 필름 센서, 마이크로컨트롤러, 스마트폰 인터페이스, 클라우드 머신러닝을 결합한 IBM HyperTaste의 휴대형 전자혀 기반 연구
  - 센서의 전위차 시계열을 학습해 음료와 생수를 분류하며, 데이터 수집부터 클라우드 추론까지 1분 이내 처리 가능성을 시연
  - 개인 미각 자체보다 음식·음료의 객관적 화학 fingerprint를 수집하는 보조 계층으로 활용 가능

---
