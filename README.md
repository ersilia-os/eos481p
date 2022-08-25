# ToxCast toxicity panel
## Model identifiers
- Slug: grover-toxcast
- Ersilia ID: eos481p
- Tags: Toxicity

# Model description
Prediction across the ToxCast toxicity panel, containing hundreds of toxicity outcomes for about ten thousand molecules.
- Input: SMILES
- Output: Toxicity 
- Model type: Classification
- Training set: 10,000,000 (https://paperswithcode.com/dataset/moleculenet)
- Mode of training: Pretrained

# Source code
This model was published by Yu R., Yatao B. et al. Self-Supervised Graph Transformer on Large-Scale Molecular Data. arXiv Labs 2018. DOI: https://doi.org/10.48550/arXiv.2007.02835

- Code: https://github.com/tencent-ailab/grover
- Checkpoints: https://github.com/tencent-ailab/grover/tree/main/grover/model

# License
The GPL-v3 license applies to all parts of the repository that are not externally maintained libraries. This repository uses the externally maintained library "grover", located at /model and licensed under an MIT license 

# History 
- Model was downloaded on 12.05.21 from TencentAILab
- We duplicated task/predict.py and scripts/save_features.py from Tencent GitHub repository
- Model was incorporated to Ersilia on 7/12/2022

# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
