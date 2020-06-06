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
from sklearn.preprocessing import MinMaxScaler, StandardScaler
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

# Variable Selection (types)
# Ratios
# Intervals - Numerice, diff btw values is meaningful but no ratio level info given (time & date)
# Categorical - No numeric meaning, indicate group membership (gender, marrige status)
# Ordinal - Categorical, indicate ranking (age brackets)
# Use One-Hot or GetDummies encoding to turn into numerical data

# Feature Engineering - Modifiying/Creating/Deleting features to help your model make better predictions
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
# Feature Creation: Use current features to create new one(s)

# Regularization - All features are kept but subject to constraint
#   Alpha is used to control the degree to which coefficients are penalised
#   In Ridge Regression, the coefficients can be minimised towards 0 but never get to it.
#       Some bias is added, due to the penalty, to keep the model from overfitting
#       Use cross validation to decide on value of lambda/alpha
#   Lasso Regression is similar to Ridge but can shrink coefficients down to 0
#       Easier to interpret as unimportant variables get removed
#       Known as a sparse model, ends up using less features than given to it.
# Ridge squares the residuals while Lasso takes the absolute value


# Train test split
X_train, X_test, y_train, y_test = train_test_split(
                                        X, y,
                                        test_size=0.2,
                                        random_state=1
                                        )
# Check shapes after train test split
X_train.shape, X_test.shape, y_train.shape, y_test.shape


# Scaling the Features (Normalisation & Standardisation)
# Normalise - get all values to be bwt 0 & 1 (sensitive to outliers)
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_trainform(X_test)

# Standardise - subtract the mean & divide by std deviation (robust to outliers) *Recommended for most cases
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

# Ensamble Methods (Combination models):
#   Heterogenoues Models - combines models of diff types
#       Voting - Use agg predictions from group of models
#       Stacking - Good for when diff models have diff strengths on the same dataset
#               - Predictions/Errors are uncorrelated
#   Homogeneous Models - combines models of the same type
#       Bagging - (Bootstrap Aggregating)
#               - Multiple versions of the same model are trained on diff subsets of the same training data
#               - Models are trained in paralled
#       Boosting - Models are trained sequentially
# Fit model
lm = LinearRegression()
lm.fit(X_train_scaled, y_train)

# check for intercepts
beta_0 = float(lm.intercept_)

# Check for errors in train data predictions
y_pred_train = lm.predict(X_train)
mse = metrics.mean_squared_error(y_train, y_pred_train)
rmse = np.sqrt(mse)
r2 = metrics.r2_score(y_train, y_pred_train)

# Make predictions in unseed data
y_pred = lm.predict(X_test_scaled)


# Check for errors & compare training errors against test errors
print(metrics.mean_squared_error(y_test, y_pred))
print(metrics.r2_score(y_test, y_pred))