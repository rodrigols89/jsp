[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](LICENSE.md)
[![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black/)

# Job Salary Prediction

> The Job Salary Prediction project was developed with the aim of predicting job advertisement salaries in the United Kingdom (UK).

 - The ["Job Salary Prediction | Kaggle"](https://www.kaggle.com/competitions/job-salary-prediction/data) dataset was used to train the model, which contains 240k job advertisements.
 - The project was developed following the **CRISP-DM** methodology.

## Project Overview

 - [Project Settings](#settings)

---

<div id="settings"></div>

## Project Settings

To use the project first, prepare the virtual environment and install the dependencies:

**Set environment:**
```bash
poetry env use python
```

**Activate environment:**
```bash
poetry shell
```

**Install dependencies:**
```bash
poetry install
```

I preferred to store the data in PostgreSQL (using the Docker container) because it is easier to apply SQL queries in all applications.

Knowing this, with *docker compose* installed, run:

```bash
sudo docker compose up -d
```

As the datasets are huge and cannot be downloaded using Kaggle API (are very old datasets) you will need:

 - Download [train (Train_rev1.zip)](https://www.kaggle.com/competitions/job-salary-prediction/data?select=Train_rev1.zip) and [test (Test_rev1.zip)](https://www.kaggle.com/competitions/job-salary-prediction/data?select=Test_rev1.zip) manually.
 - Extract them in the [/kaggle](jsp/data_sources/kaggle) folder in *.CSV format*.

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
