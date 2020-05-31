#================================
# Fits a line through the data
#================================
# Assumes linearity, independence, homoscedasticity, and normality
# Multicollinearity has to be checked btw the features
# Outliers must also be taken into consideration

# imports
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# datasets
mt_cars = pd.read_csv(
                "https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/regression_sprint/mtcars.csv",
                index_col=0
                )

# Exploratory Data Analysis
mt_cars.shape # rows & columns
mt_cars.info() # summary of features

# Regression line model
# y = B0 + B1(X1), where B0 is the intercept, B1 is the line slope

# Separating the response from the features
# X == predictors, features, independant variables
# y == response, target, dependant variable, output
X = mt_cars.drop(['mpg'], axis=1)
y = mt_cars['mpg'] # also do EDA on the response

# Featurs Engineering
# Check for linearity, might have to log features/reponse
#   check 1: Draw scatter/regplots to check for linearity
# Remove multicollinear features (corr(), Variance Inflation Factor)
    # check 1: Visualise an sns.paiplot
    # check 2: Corralation heatmaps
# Check for Autocorralation (Residuals, Durbin-Watson stat)
# Check for Homoscedasticity - Constant variance amongst residuals of all fitted values
# Check for Normality of the residuals - Errors are generated from a normal distribution
    # check 1: Visualise distribution of resduals
    # check 2: Quantile quantile plot
    # check 3: Shapiro-Wilkes test - If sw>=0.05, Data from normal dist
# Train test split
X_train, X_test, y_train, y_test = train_test_split(
                                        X, y,
                                        test_size=0.2,
                                        random_state=1
                                        )
# Check shapes after train test split
X_train.shape, X_test.shape, y_train.shape, y_test.shape

# Fit model
lm = LinearRegression()
lm.fit(X_train, y_train)

# check for intercepts
beta_0 = float(lm.intercept_)

# Check for errors in train data predictions
y_pred_train = lm.predict(X_train)
mse = metrics.mean_squared_error(y_train, y_pred_train)
rmse = np.sqrt(mse)
r2 = metrics.r2_score(y_train, y_pred_train)

# Make predictions in unseed data
y_pred = lm.predict(X_test)


# Check for errors & compare training errors against test errors
print(metrics.mean_squared_error(y_test, y_pred))
print(metrics.r2_score(y_test, y_pred))