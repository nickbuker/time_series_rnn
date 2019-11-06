# TODO

## Author
Nick Buker

## Introduction
TODO

## Disclaimer
TODO

## Project requirements
Use of a virtual environment is highly recommended. The author suggests use of [pyenv](https://github.com/pyenv/pyenv) for controlling both Python and package versions.
- Python version 3.6 (project constructed using 3.6.8)
- Upgrade to the latest version of pip
```
$ pip install --upgrade pip
```
- Navigate to the root directory of this repo and install of the contents of the `requirements.txt` file
``` 
$ pip install -r requirements.txt 
```

## Results

## Project structure
```
├── data/
│   ├── daily_temp_ts.csv
│   ├── detrend_scale_data.csv
│   └── prep_daily_temp_ts.csv
├── notebooks/
│   ├── 00_tidy_data.ipynb
│   └── 01_fit_rnn.ipynb
├── README.md
├── requirements.txt
└── src/
    └── utils.py

```
- `data/` - Directory housing CSV data
    - `daily_temp_ts.csv` -
    - `detrend_scale_data.csv` -
    - `prep_daily_temp_ts.csv` -
- `notebooks/` - Directory housing notebooks
    - `00_tidy_data.ipynb` -
    - `01_fit_rnn.ipynb` -
- `requirements.txt` - Python packages required to run project
- `src/` - 
