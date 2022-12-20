from __future__ import annotations

from datetime import datetime

import pandas as pd
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split


class Training:
    def split_data(self, X, y):

        start_time = datetime.now()

        X_train, X_valid, y_train, y_valid = train_test_split(
            X, y, test_size=0.3, random_state=42
        )
        print("Data splitted!")

        end_time = datetime.now()
        print(f"Method runtime: {end_time - start_time}")

        return X_train, X_valid, y_train, y_valid

    def catBoostRegressor(
        self,
        X_train,
        y_train,
        X_valid_or_test,
        cat_features=[0],
        predict=False,
    ):

        start_time = datetime.now()

        train_data = X_train  # X data.
        train_labels = y_train  # y data.

        model = CatBoostRegressor()
        model.fit(train_data, train_labels, cat_features)

        if predict is True:
            salaries_predicted = pd.DataFrame(
                model.predict(X_valid_or_test), columns=["SalaryNormalized"]
            )
            end_time = datetime.now()
            print(f"Method runtime: {end_time - start_time}")
            return salaries_predicted
