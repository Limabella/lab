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

---

## Psychology & Bias

- [2025/2026] [The “Web Browser” of the Collective Unconscious: The Mirror and Oracle of Generative AI](https://link.springer.com/article/10.1007/s12115-026-01193-1?utm_source=copilot.com)
  - 생성형 AI를 집단무의식의 거울·오라클로 해석
  - Midjourney 같은 이미지 생성 AI가 상징적 어휘를 재구성하며 새로운 의미를 창출
  - 윤리적 문제(데이터 편향, 저작권, 신뢰성) 논의

- [2025-12-11] [The Algorithmic Unconscious: Structural Mechanisms and Implicit Biases in LLMs](https://hal.science/hal-2025)
  - 토큰화·어텐션·정렬 과정에서 발생하는 구조적 편향 분석
  - "알고리즘적 무의식" 개념 제안
  - LLM alignment와 bias 연구 참고용

- [2025-03-01] [공감과 공격성의 관계: 어두운 4요소 성격의 매개효과](https://doi.org/10.0000/kjhp.2025.31.2.429)
  - 한국심리학회지
  - 공감과 공격성의 간접 관계 분석
  - 사이코패시·사디즘 매개효과 확인

- [2014-02-01] [Narcissism in the Modern World](https://doi.org/10.1080/14753634.2014.894225)
  - Pat MacDonald
  - 현대 사회의 자기애적 성향 확산 분석
  - 문화적·임상적 함의 논의

- [2008-06-01] [Distracted: The Erosion of Attention and the Coming Dark Age](https://prometheusbooks.com)
  - Maggie Jackson 저서
  - 현대 사회의 집중력 붕괴와 기술·문화적 요인 비판

- [2002-12-01] [Bad Boys, Good Mothers, and the “Miracle” of Ritalin](https://doi.org/10.1017/S0269889702000650)
  - ADHD와 리탈린의 사회적·역사적 맥락 분석
  - 진단 및 약물 사용의 문화적 정당화 과정 탐구