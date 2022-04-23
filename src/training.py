from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

import pandas as pd
import numpy as np
import joblib


class Training:

  def split_data(self, x, y):
    x_train, x_valid, y_train, y_valid = train_test_split(x, y, test_size=0.3, random_state=42)
    return x_train, x_valid, y_train, y_valid


  def linear_regression(self, x_train, y_train, x_valid_test, predict=False, model_name=None):
    model = LinearRegression() # Instance.
    model.fit(x_train, y_train) # Training.
    # Save model process.
    if model_name is not None:
      joblib.dump(
        value=model,
        filename=f"../resources/load/{model_name}.pkl"
      )
      print("Model saved!")
    # Predict process.
    if predict is True:
      salaries_predicted = pd.DataFrame(model.predict(x_valid_test), columns=["SalaryNormalized"])
      return salaries_predicted


  def ridge_regression(self, x_train, y_train, x_valid_test, predict=False, model_name=None):
    model = Ridge(alpha=1.0) # Alpha = Learning Rate.
    model.fit(x_train, y_train) # Training.
    # Save model process.
    if model_name is not None:
      joblib.dump(
        value=model,
        filename=f"../resources/load/{model_name}.pkl"
      )
      print("Model saved!")
    # Predict process.
    if predict is True:
      salaries_predicted = pd.DataFrame(model.predict(x_valid_test), columns=["SalaryNormalized"])
      return salaries_predicted


  def lasso_regression(self, x_train, y_train, x_valid_test, predict=False, model_name=None):
    model = Lasso(alpha=10, max_iter=1000, tol=0.1)
    model.fit(x_train, y_train) # Training.
    # Save model process.
    if model_name is not None:
      joblib.dump(
        value=model,
        filename=f"../resources/load/{model_name}.pkl"
      )
      print("Model saved!")
    # Predict process.
    if predict is True:
      salaries_predicted = pd.DataFrame(model.predict(x_valid_test), columns=["SalaryNormalized"])
      return salaries_predicted


  def elasticnet_regression(self, x_train, y_train, x_valid_test, predict=False, model_name=None):
    model = ElasticNet(alpha=1, l1_ratio=0.5, tol=0.3)
    model.fit(x_train, y_train) # Training.
    # Save model process.
    if model_name is not None:
      joblib.dump(
        value=model,
        filename=f"../resources/load/{model_name}.pkl"
      )
      print("Model saved!")
    # Predict process.
    if predict is True:
      salaries_predicted = pd.DataFrame(model.predict(x_valid_test), columns=["SalaryNormalized"])
      return salaries_predicted


  def random_forest_regressor(self, x_train, y_train, x_valid_test, predict=False, model_name=None):
    model = RandomForestRegressor(n_jobs=-1) # Instance.
    model.fit(x_train, np.ravel(y_train)) # Training.
    # Save model process.
    if model_name is not None:
      joblib.dump(
        value=model,
        filename=f"../resources/load/{model_name}.pkl"
      )
      print("Model saved!")
    # Predict process.
    if predict is True:
      salaries_predicted = pd.DataFrame(model.predict(x_valid_test), columns=["SalaryNormalized"])
      return salaries_predicted


  def get_mae_scores(self, x, y):

    # KFold instance -  # shuffle=True, Shuffle (embaralhar) the data.
    kfold = KFold(
      n_splits=10,
      shuffle=True
    )

    # Models instances.
    randomForestRegressor = RandomForestRegressor(n_jobs=-1)
    linearRegression      = LinearRegression()
    elasticNet            = ElasticNet()
    ridge                 = Ridge()
    lasso                 = Lasso()

    # Apply cross-validation with KFold for all models.
    randomForestRegressor_result = abs(cross_val_score(randomForestRegressor, x, y, cv = kfold, scoring='neg_mean_absolute_error'))
    linearRegression_result      = abs(cross_val_score(linearRegression, x, y, cv = kfold, scoring='neg_mean_absolute_error'))
    elasticNet_result            = abs(cross_val_score(elasticNet, x, y, cv = kfold, scoring='neg_mean_absolute_error'))
    ridge_result                 = abs(cross_val_score(ridge, x, y, cv = kfold, scoring='neg_mean_absolute_error'))
    lasso_result                 = abs(cross_val_score(lasso, x, y, cv = kfold, scoring='neg_mean_absolute_error'))

    # Create a dictionary to store the Models.
    dic_models = {
      "randomForestRegressor": randomForestRegressor_result.mean(),
      "LinearRegression": linearRegression_result.mean(),
      "ElasticNet": elasticNet_result.mean(),
      "Ridge": ridge_result.mean(),
      "Lasso": lasso_result.mean()
    }
    bestModel = min(dic_models, key=dic_models.get) # Select the best model.

    print("MAE for Random Forest Regressor: {0}\nMAE for Linear Regression: {1}\nMAE for Ridge (L2) Regression: {2}\nMAE for Lasso (L1) Regression: {3}\nMAE for Elastic Net (L2 + L1) Regression: {4}".format(randomForestRegressor_result.mean(), linearRegression_result.mean(), elasticNet_result.mean(), ridge_result.mean(), lasso_result.mean()))
    print("The best model is {0} with MAE value: {1}".format(bestModel, dic_models[bestModel]))
