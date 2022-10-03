[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](LICENSE.md)

# Job Salary Prediction

This project was developed to solve a challenge to **Data Scientist** opportunity from [GRIA](https://www.gria.com.br/).

Briefly, the challenge was:

> Develop a model to predict salaries from job ads.

**NOTE:**<br>
This project will be developed follow **CRISP-DM** methodology.

## Project Overview

 - [Challenge objectives (Business understanding)](#challenge-objectives)
 - [Dataset proposed (Data understanding)](#problem-proposed)
 - [Exploratory Data Analysis (Data understanding)](#eda)
 - [Credits](#credits)


---

<div id="challenge-objectives"></div>

##  Challenge objectives (Business understanding)

The main [GRIA](https://www.gria.com.br/) objectives were to evaluate how the candidate would work as a **Data Scientist** in the company.

 - **The main evaluation criteria were:**
   - Documentation;
   - Reproducibility:
     - The ability to be reproduced or copied.
   - Code analysis and quality;
   - Pipeline modeling (Modelagem de pipeline);
   - Efficiency.

The problem proposed were [Job Salary Prediction](https://www.kaggle.com/competitions/job-salary-prediction/) available on [Kaggle](https://www.kaggle.com/). The objectives and specifications described in the competition will be considered by [GRIA](https://www.gria.com.br/).

**Briefly, the challenge was:**<br>
 - Create a model to predict salaries from job ads.
 - The **Evaluation Metric** to the competition were [Mean Absolute Error](https://en.wikipedia.org/wiki/Mean_absolute_error).

---

<div id="problem-proposed"></div>

## Dataset proposed (Data understanding)

The dataset consists of a large number of rows (240k+ samples) representing individual job ads, and a series of fields about each job ad.

These fields are as follows:

 - **Id:**
   - A unique identifier for each job ad
 - **Title:**
   - Briefly, the **Title** is the summary (resumo) of the position or function.
 - **FullDescription:**
   - The full text of the job ad as provided by the job advertiser.
   - Where you see ***s, we have stripped values from the description in order to ensure that no salary information appears within the descriptions.
   - There may be some collateral damage here where we have also removed other numerics.
 - **LocationRaw:**
   - Imagine that this column represents the job location, however, using cardinal points (West, East) and/or references.
 - **LocationNormalized:**
   - It has the same meaning as the LocationRaw column, but with less information and references.
   - That's because this column is the result of a Pre-Processing of the LocationRaw column did by Adzuna.
 - **ContractType:**
   - This column represents the types of contracts per job vacancy sample, which are **full_time** or **part_time**.
   - In fact, this column tells us whether the employee works **full-time (eg 40 hours per week)** or **part-time (eg 20 hours per week)**.
 - **ContractTime:**
   - Contract type, which can be **permanent** or **contract**.
 - **Company:**
   - The employer (empregador) name provided by the job advertiser.
 - **Category:**
   - Job categories (are 30):
 - **SalaryRaw:**
   - Imagine that this column represents the salary of the ad (sample). However:
     - No formatting;
     - With bonus;
     - Remuneration:
       - Per hour;
       - Per month;
       - Per annum.
 - **SalaryNormalised:**
   - It has the same meaning as the "SalaryRaw" column, however Adzuna has *normalized* the data so that the salary is represented in an *annualized* way.
 - **SourceName:**
   - The website name or advertiser from whom we received the job ad.

**NOTE:**<br>
**All of the data is real**, live data used in job ads so is clearly subject to lots of real world noise, including but not limited to:

  - Ads that are not UK based;
  - Salaries that are incorrectly stated;
  - Fields that are incorrectly normalised;
  - And duplicate adverts.

---

<div id="eda"></div>

## Exploratory Data Analysis (Data understanding)

> Here, we go understanding more about the data, applying an **Exploratory Data Analysis (EDA)**.

**To see Exploratory Data Analysis click on the link (Jupyter Notebook) below:**<br>
<a target="_blank" href="notebooks/eda.ipynb">
    <img src="res/jupyter-icon.ico" />
    Exploratory Data Analysis (EDA)
</a>

---

<div id="credits"></div>

## Credits

**Mentor:**<br>
[Fernando Felix](https://www.linkedin.com/in/fernandofnjr/)<br>

**Resources:**<br>
[Job Salary Prediction (Predict the salary of any UK job ad based on its contents)](https://www.kaggle.com/c/job-salary-prediction)<br>

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
