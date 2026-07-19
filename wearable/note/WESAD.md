# WESAD Dataset Note

## Source

- Official project page: <https://ubi29.informatik.uni-siegen.de/usi/data_wesad.html>
- Interactive preview: <https://kristofvl.github.io/wesadviz/>
- Original dataset download: <https://uni-siegen.sciebo.de/s/HGdUkoNlW1Ub0Gx>
- Paper: [Introducing WESAD, a Multimodal Dataset for Wearable Stress and Affect Detection](https://doi.org/10.1145/3242969.3242985)
- Authors: Philip Schmidt, Attila Reiss, Robert Duerichen, Claus Marberger, Kristof Van Laerhoven
- Venue: ICMI 2018

## Summary

WESAD is a multimodal wearable dataset for stress and affect recognition. It contains physiological and motion recordings collected from chest- and wrist-worn devices during a laboratory study with 15 participants.

The experiment provides three affective conditions:

- Baseline / neutral
- Stress
- Amusement

Participant self-reports collected with established questionnaires are included alongside the sensor recordings.

## Sensor modalities

| Modality | Typical project use |
|---|---|
| Blood Volume Pulse (BVP/PPG) | Heart rate, pulse intervals, HRV-related features |
| Electrocardiogram (ECG) | Heart rate and HRV reference features |
| Electrodermal Activity (EDA) | Sympathetic arousal-related features |
| Electromyogram (EMG) | Muscle activation and tension-related features |
| Respiration | Breathing rate and cycle features |
| Body temperature | Peripheral temperature trends |
| 3-axis acceleration (ACC) | Motion context and artifact detection |

## Dataset scale and reported benchmark

- Participants: 15
- Download size: approximately 2.5 GB compressed
- Original paper task: baseline vs. stress vs. amusement
- The official page reports accuracy up to 80% for the three-class problem and up to 93% for stress vs. non-stress using its benchmark setup.

These reported values are reference results, not expected performance for this project. They must not be directly compared with a new experiment unless the subject split, preprocessing, sensor selection, and evaluation metrics are equivalent.

## Planned use in this project

### Phase 1

Use wrist BVP, EDA, and ACC to build a minimal, reproducible baseline:

1. Detect missing or low-quality intervals.
2. Use ACC to flag motion-contaminated BVP intervals.
3. Extract interpretable features with NeuroKit2.
4. Train Logistic Regression and XGBoost baselines.
5. Evaluate with leave-one-subject-out or another strict subject-independent split.

### Phase 2

Extract frozen PaPaGei embeddings from BVP/PPG and compare:

- Handcrafted physiological features
- PaPaGei embeddings
- Feature and embedding fusion

### Phase 3

Compare NormWear representations when combining multiple available signals. Add self-report data as context rather than treating physiological measurements as direct psychological labels.

## Leakage prevention

- Never randomly split overlapping windows from the same participant across training and test sets.
- Fit normalization, imputation, feature selection, and calibration only on the training subjects in each fold.
- Keep raw subject identifiers available for splitting, but remove them from model inputs.
- Record window length, overlap, sampling rate, excluded intervals, and label mapping in every experiment.
- Treat repeated windows from the same recording as correlated observations.

## Interpretation limits

- WESAD is a small laboratory dataset and does not establish real-world clinical validity.
- The stress protocol label is not a psychiatric diagnosis.
- EDA indicates changes in arousal, not a specific emotion or cause.
- PPG quality varies with motion, contact, device, and participant characteristics.
- Cortisol and serotonin concentrations cannot be inferred directly from these signals.
- Results should be described as dataset-specific stress-condition classification or state estimation.

## License and storage

The official page permits scientific, non-commercial use with attribution. Confirm the current terms on the source page before redistribution or publication.

Do not commit the 2.5 GB archive or extracted participant recordings to Git. A suggested local layout is:

```text
wearable/
├── note/
│   └── WESAD.md
└── runtime/
    └── data/
        └── wesad/       # local only; ignored by Git
```

Keep checksums and a data manifest in version control instead of the raw data.

## Citation

Schmidt, P., Reiss, A., Duerichen, R., Marberger, C., & Van Laerhoven, K. (2018). *Introducing WESAD, a Multimodal Dataset for Wearable Stress and Affect Detection*. Proceedings of the 20th ACM International Conference on Multimodal Interaction. <https://doi.org/10.1145/3242969.3242985>
