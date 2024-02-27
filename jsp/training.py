# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
# ============================================================================
"""Module to train ML models."""


from __future__ import annotations

import time

import pandas as pd
from catboost import CatBoostRegressor, Pool
from sklearn.model_selection import train_test_split

train_df = pd.read_csv("datalake/landing/Train_rev1.csv")

X = train_df.drop(  # Independent variables.
    columns=[
        "Id",
        "LocationRaw",
        "SalaryNormalized",
    ]
).astype(str)
y = train_df["SalaryNormalized"]  # Dependent variable.


# Split data into train and test.
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Encapsulate training data.
pool_train = Pool(
    X_train,
    y_train,
    cat_features=[
        "LocationNormalized",
        "ContractType",
        "ContractTime",
        "Company",
        "Category",
        "SourceName",
    ],
    text_features=["Title", "FullDescription", "SalaryRaw"],
)

# Encapsulate validate data.
pool_valid = Pool(
    X_valid,
    y_valid,
    cat_features=[
        "LocationNormalized",
        "ContractType",
        "ContractTime",
        "Company",
        "Category",
        "SourceName",
    ],
    text_features=["Title", "FullDescription", "SalaryRaw"],
)


# Train the model.
start = time.time()
model = CatBoostRegressor()
model.fit(
    pool_train,
    eval_set=pool_valid,
    silent=True,
)
end = time.time()
elapsed_time = end - start
model.save_model("datalake/curated/model-v1.cbm")  # Save the model.
