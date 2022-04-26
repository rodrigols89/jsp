import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from math import floor

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import learning_curve
from sklearn.model_selection import KFold


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


  def create_train_sizes(self, x, cv):
    train_sizes = [1] # Start train_size with 1 element.
    count_while = 1 # While control.
    div_train_sizes = floor(x.shape[0]/2) #
    while count_while < cv:
      train_sizes.insert(1, div_train_sizes) # Always add train_size in to index=1, index 0 always is 1.
      div_train_sizes = floor(div_train_sizes/2) # Set new value to div_train_sizes
      count_while += 1 # While increment.
    return train_sizes


  def create_learning_curves(self, x=None, y=None, estimator=None, cv=5, save=None):

    # Check X, y variables.
    if x is None:
      return print("Please, enter X variables!")
    elif y is None:
      return print("Please, enter target (Y) variable!")
    
    # Check estimator before create Learning Curves.
    if estimator is None:
      return print("Please, enter your estimator!")
    else:
      try:
        estimator = estimator()
      except NameError:
        print("Invalid estimator!")
      else:
        # Get train sizes.
        train_sizes = self.create_train_sizes(x, cv)
        # Get Learning Curve statistics.
        train_sizes, train_scores, validation_scores = learning_curve(
          estimator = estimator,
          X = x,
          y = y,
          train_sizes = train_sizes,
          cv = cv,
          scoring = 'neg_mean_squared_error',
          shuffle=True
        )
        # Get mean statistics.
        train_scores_mean = -train_scores.mean(axis = 1)
        validation_scores_mean = -validation_scores.mean(axis = 1)
        # Display statistics.
        print("train_sizes: ", train_sizes)
        print('\n', '-' * 70) # Estamos multiplicando o caractere '-' por 70, ou seja, uma linha tracejada.   
        print('Training scores:\n\n', train_scores)
        print('\nValidation scores:\n\n', validation_scores)
        print('\n', '-' * 70)  
        print('\nMean training scores:\n', pd.Series(train_scores_mean, index = train_sizes))
        print('\nMean validation scores:\n',pd.Series(validation_scores_mean, index = train_sizes))
        # Create a plot.
        if save is None:
          plt.figure(figsize=(10, 7))
          plt.style.use('seaborn')
          plt.plot(train_sizes, train_scores_mean, marker='o', label = 'Training error')
          plt.plot(train_sizes, validation_scores_mean, marker='o', label = 'Validation error')
          plt.ylabel('MAE', fontsize = 14)
          plt.xlabel('Training set size', fontsize = 14)
          plt.title('Learning curves for a ' + str(estimator).split('(')[0] + ' model', fontsize = 18, y = 1.03)
          plt.legend()
          plt.show()
        else:
          plt.figure(figsize=(10, 7))
          plt.style.use('seaborn')
          plt.plot(train_sizes, train_scores_mean, marker='o', label = 'Training error')
          plt.plot(train_sizes, validation_scores_mean, marker='o', label = 'Validation error')
          plt.ylabel('MAE', fontsize = 14)
          plt.xlabel('Training set size', fontsize = 14)
          plt.title('Learning curves for a ' + str(estimator).split('(')[0] + ' model', fontsize = 18, y = 1.03)
          plt.legend()
          plt.savefig(f"../resources/load/{save}.png", format='png')
          plt.show()
