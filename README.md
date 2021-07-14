TIPI NER
============

## Requirements

* Python 3.6
* Virtualenv (created and activated)


## Setup

TO-DO: check this

```
git clone git@github.com:politicalwatch/tipi-backend.git
cd tipi_ner
pip install -r requirements_dev.txt
set -a
source .env
python setup.py develop
```

# Run

To run without CUDA: `CUDA_VISIBLE_DEVICES="" python testing.py`


# Categories

The application predicts the following tags:

- PER: person name
- LOC: location name
- ORG: organization name
- MISC: other name

# Run tests

`runtests.sh`

# Notes

Spanish model: https://huggingface.co/flair/ner-spanish-large
How to download and deploy? Now I've downloaded the files manually to `ner_spanish_large` directory
