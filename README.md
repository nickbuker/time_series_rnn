# Time Series Forecasting with RNN's

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
TODO

## Project structure
```
├── README.md
├── __init__.py
├── data/
│   ├── daily_temp_ts.csv
│   ├── detrend_scale_data.csv
│   └── prep_daily_temp_ts.csv
├── notebooks/
│   ├── 00_tidy_data.ipynb
│   └── 01_fit_rnn.ipynb
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── data_prep.py
│   └── utils.py
└── test
    ├── __init__.py
    └── test_data_prep.py
```
- `data/` - Directory housing CSV data
    - `daily_temp_ts.csv` - Raw temperature data
    - `detrend_scale_data.csv` - Parameters used to detrend and scale the data
    - `prep_daily_temp_ts.csv` - Detrended and scaled data suitable for model ingestion
- `notebooks/` - Directory housing notebooks
    - `00_tidy_data.ipynb` -
    - `01_fit_rnn.ipynb` -
- `requirements.txt` - Python packages required to run project
- `src/` - Directory housing Python scipts
    - `data_prep.py` -
    - `utils.py` -
- `test/` - Directory housing tests for the Python scripts
    - `test_data_prep.py` -
