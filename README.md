# ToxCast toxicity panel

Prediction across the ToxCast toxicity panel, containing hundreds of toxicity outcomes, as part of the MoleculeNet benchmark. This model has been trained using the GROVER transformer (see eos7w6n or grover-embedding for a detail of the molecular featurization step with GROVER)

This model was incorporated on 2022-07-13.

## Information
### Identifiers
- **Ersilia Identifier:** `eos481p`
- **Slug:** `grover-toxcast`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `Toxicity`, `ToxCast`, `Chemical graph model`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `617`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of toxicity against 617 biological targets

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| acea_t47d_80hr_negative | float | high | Probability of the toxicity property of ToxCast dataset from MoleculeNet |
| acea_t47d_80hr_positive | float | high | Probability of the toxicity property of ToxCast dataset from MoleculeNet |
| apr_hepg2_cellcyclearrest_24h_dn | float | high | Probability of the toxicity property of ToxCast dataset from MoleculeNet |
| apr_hepg2_cellcyclearrest_24h_up | float | high | Probability of the toxicity property of ToxCast dataset from MoleculeNet |
| apr_hepg2_cellcyclearrest_72h_dn | float | high | Probability of the toxicity property of ToxCast dataset from MoleculeNet |
| apr_hepg2_cellloss_24h_dn | float | high | Probability of the toxicity property of ToxCast dataset from MoleculeNet |
| apr_hepg2_cellloss_72h_dn | float | high | Probability of the toxicity property of ToxCast dataset from MoleculeNet |
| apr_hepg2_microtubulecsk_24h_dn | float | high | Probability of the toxicity property of ToxCast dataset from MoleculeNet |
| apr_hepg2_microtubulecsk_24h_up | float | high | Probability of the toxicity property of ToxCast dataset from MoleculeNet |
| apr_hepg2_microtubulecsk_72h_dn | float | high | Probability of the toxicity property of ToxCast dataset from MoleculeNet |

_10 of 617 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos481p](https://hub.docker.com/r/ersiliaos/eos481p)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos481p.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos481p.zip)

### Resource Consumption
- **Model Size (Mb):** `1534`
- **Environment Size (Mb):** `2550`
- **Image Size (Mb):** `7090.68`

**Computational Performance (seconds):**
- 10 inputs: `50.69`
- 100 inputs: `451.79`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/tencent-ailab/grover](https://github.com/tencent-ailab/grover)
- **Publication**: [https://arxiv.org/abs/2007.02835](https://arxiv.org/abs/2007.02835)
- **Publication Type:** `Preprint`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [Amna-28](https://github.com/Amna-28)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos481p
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos481p
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
