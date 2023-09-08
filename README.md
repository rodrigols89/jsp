[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](LICENSE.md)
[![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black/)

# Job Salary Prediction

> The Job Salary Prediction project was developed with the aim of predicting job advertisement salaries in the United Kingdom (UK).

## Project Overview

 - [Data Lake Architecture](#architecture)
 - [Settings](#settings)

<!--- ( Architecture ) --->

---

<div id="architecture"></div>

## Data Lake Architecture

The project follows the following **Data Lake Architecture** to store and make available data:

![img](assets/architecture.png)

 - **Landing (Entry Point/Ingestion):**
   - The *"Landing"* bucket serves as the *entry point* for the data lake.
   - It is used to receive **raw data**, often in its original format, with little or no transformation.
   - Data here can come from various sources such as server logs, IoT devices, social media feeds, etc.
   - The primary purpose of this bucket is to store **raw data**, allowing data to be quickly dumped into the data lake without an immediate need for processing or structuring. This helps capture all available data for future analysis and transformation.
 - **Processing:**
   - The *"Processing"* bucket is where *raw data* from the *"Landing"* layer undergoes processing and transformation to make it more usable and valuable.
   - Data here may be cleaned, enriched, structured, and transformed into suitable formats for advanced analytics, machine learning, reporting, and other use cases.
   - Typically, data processing tools like Apache Spark, Apache Flink, or ETL (Extract, Transform, Load) services are used in this layer.
 - **Curated:**
   - The *"Curated"* bucket is where processed and ready-to-use data is stored in an organized and structured manner.
   - Data in this bucket is usually refined, optimized, and may be indexed to enable quick and efficient access.
   - This layer is often used by Data Analysts, Data Scientists, and other professionals to conduct analyses, create Dashboards, reports, and other activities that require high-quality data.
   - This is where data becomes "curated" and prepared for consumption by applications and systems that rely on accurate and reliable information.

<!--- ( Settings ) --->

---

<div id="settings"></div>

## Settings

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
 - Extract them in the [jsp/datalake/landing](./jsp/datalake/landing) folder in *.CSV format*.

Finally, you can run the command **"jsp etl"** CLI to load the DataFrames into PostgreSQL:

```bash
jsp etl --help
```

```bash
Usage: jsp etl [OPTIONS] COMMAND [ARGS]...

  Command to apply ETL processes.

Options:
  --help  Show this message and exit.

Commands:
  load-all    Loads all train and test data into PostgreSQL.
  load-test   Loads test data into PostgreSQL.
  load-train  Loads train DataFrames into PostgreSQL.
```

Here you can use:

 - **jsp etl load-all:**
   - To load the *train* and *test* data into PostgreSQL.
 - **jsp etl load-test:**
   - To load the *test* data into PostgreSQL.
 - **jsp etl load-train:**
   - To load the *train* data into PostgreSQL.

**NOTE:**<br>
If you are interested in committing something initialize [pre-commit](https://pre-commit.com/#3-install-the-git-hook-scripts) settings:

```bash
pre-commit install
```

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
