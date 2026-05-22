````md
---
title: Experiment Template
author:
date:
tags: []
status: planned
project:
paper:
---

# Experiment Overview

> One experiment = one document

---

# Objective

## Goal

- What are we trying to verify?
- What hypothesis are we testing?

Example:

- Compare caption quality between BLIP and LLaVA
- Evaluate hallucination reduction with higher image resolution

---

# Background

## Related Papers

| Paper | Contribution | Notes |
|---|---|---|
|  |  |  |

---

## Key References

- 
- 
- 

---

# Dataset

| Dataset | Samples | Type | Source |
|---|---|---|---|
|  |  |  |  |

---

## Dataset Notes

```text
- filtering strategy
- preprocessing
- train/val split
- annotation quality
````

---

# Input / Output Template

```text
Input: <image>
Response: {caption}
```

---

# Environment

| Item       | Value |
| ---------- | ----- |
| GPU        |       |
| CUDA       |       |
| Framework  |       |
| Python     |       |
| Batch Size |       |
| Resolution |       |
| Epochs     |       |

---

# Model Configuration

## Backbone

```yaml
model:
  vision_encoder:
  llm:
```

---

## Hyperparameters

```yaml
learning_rate:
weight_decay:
scheduler:
optimizer:
warmup_steps:
```

---

# Training Procedure

## Steps

1.
2.
3.

---

## Prompt Template

```text
Describe the image in detail.
```

---

# Experiment Log

| Time | Event | Notes |
| ---- | ----- | ----- |
|      |       |       |

---

# Results

## Quantitative Results

| Model | Metric | Score |
| ----- | ------ | ----- |
|       |        |       |

---

## Qualitative Results

### Example 1

#### Input

```text
<image>
```

#### Output

```text
Generated caption here
```

#### Observation

*

---

# Analysis

## What Worked

*
*

---

## Failure Cases

*
*

---

## Hallucination Analysis

| Case | Cause | Possible Fix |
| ---- | ----- | ------------ |
|      |       |              |

---

# Ablation Study

| Setting | Change | Result |
| ------- | ------ | ------ |
|         |        |        |

---

# Conclusion

## Summary

*
*

---

## Next Actions

* [ ]
* [ ]
* [ ]

---

# Appendix

## Useful Commands

```bash
python train.py \
    --config configs/train.yaml
```

---

## File Structure

```text
project/
├── experiments/
├── datasets/
├── outputs/
├── checkpoints/
└── scripts/
```

---

# Links

| Type   | Link |
| ------ | ---- |
| WandB  |      |
| GitHub |      |
| Paper  |      |

```
```
