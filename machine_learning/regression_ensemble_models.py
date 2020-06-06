#=============================
# Types of Ensembled Models
#=============================

# Heterogenous Models
#---------------------
# Diff types of models grouped together to return an aggregate predition
# Types:
#   Voting - The mean is used in Regression. Mode is used for Classification
#   Stacking



# Homogeneous Models
#-------------------
# Models of the same kind are used together to make a prediction
# Types:
#   Bagging
#   Boosting

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import (VotingRegressor, 
                            StackingRegressor, 
                            BaggingRegressor,
                            AdaBoostRegressor)

df = pd.read_csv("https://github.com/Explore-AI/Public-Data/blob/master/house_price_by_area.csv?raw=true")
df.head()

# Separate the independent varaiblese from the dependent
X = df['LotArea']
y = df['SalePrice']

# Visualise SalesPrice vs LotArea
plt.scatter(X,y)
plt.title("House Price vs Area")
plt.xlabel("Lot in m$^2$")
plt.ylabel("Sale Price in ZAR")
plt.show()

# Scaling the data
x_scaler = StandardScaler()
y_scaler = StandardScaler()

X_scaled = x_scaler.fit_transform(X[:, np.newaxis])
y_scaled = y_scaler.fit_transform(y[:, np.newaxis])

# train_test_split
x_train, x_test, y_train, y_test = train_test_split(
                                    X_scaled, y_scaled,
                                    test_size=0.2,
                                    random_state=6
                                    )

# Create & fit linear model
lr = LinearRegression()
lr.fit(x_train, y_train)

y_pred_test = lr.predict(x_test)

#Visualise regression line over data points
x_domain = np.linspace(min(x_train), max(x_train), 100)

y_pred_rescaled = y_scaler.inverse_transform(lr.predict(x_domain))
x_rescaled = x_scaler.inverse_transform(x_domain)

plt.figure()
plt.scatter(X, y)
plt.plot(x_rescaled, y_pred_rescaled, color='red', label='predictions')
plt.xlabel("LotArea in M$^2$")
plt.ylabel("SalePrice in ZAR")
plt.title("Linear Regression")
plt.legend()
plt.show()

# Decision Tree Model
regr_tree = DecisionTreeRegressor(max_depth=3)
regr_tree.fit(x_train, y_train)

y_pred = regr_tree.predict(x_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse}")

# Plot decision tree line over data
x_domain = np.linspace(min(x_train), max(x_train), 100)

y_pred_rescaled = y_scaler.inverse_transform(regr_tree.predict(x_domain))
x_rescaled = x_scaler.inverse_transform(x_domain)

plt.figure()
plt.scatter(X, y)
plt.plot(x_rescaled, y_pred_rescaled, color='red', label='predictions')
plt.xlabel("LotArea in m$^2$")
plt.ylabel("SalePrice in ZAR")
plt.title("Decison Tree")
plt.legend()
plt.show()

# Instantiate & fir SVR
svr = SVR(kernel='rbf', gamma='auto')
svr.fit(x_train, y_train[:,0])

y_pred = svr.predict(x_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse}")

# Plot SVR prediction over data
x_domain = np.linspace(min(x_train), max(x_train), 100)

y_pred_rescaled = y_scaler.inverse_transform(svr.predict(x_domain))
x_rescaled = x_scaled = x_scaler.inverse_transform(x_domain)

plt.figure()
plt.scatter(X, y)
plt.plot(x_rescaled, y_pred_rescaled, color='red', label='predictions')
plt.xlabel("LotArea in M$^2$")
plt.ylabel("SalePrice in ZAR")
plt.title("Support Vector Regression")
plt.legend()
plt.show()


# Heterogenous Ensembles (Voting)
models = [
    ("LR", lr),
    ("DT", regr_tree),
    ("SVR", svr)
]

# Specify model weights & model averaging
model_weightings = np.array([0.1, 0.3, 0.6])
v_reg = VotingRegressor(estimators=models, weights=model_weightings)

v_reg.fit(x_train, y_train[:,0])

y_pred = v_reg.predict(x_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE: {rmse}")

# Plot voting regression prediction
x_domain = np.linspace(min(x_train), max(x_train), 100)

y_pred_rescaled = y_scaler.inverse_transform(v_reg.predict(x_domain))
x_rescaled = x_scaler.inverse_transform(x_domain)

plt.figure()
plt.scatter(X, y)
plt.plot(x_rescaled, y_pred_rescaled, color='red', label='predictions')
plt.xlabel("LotArea in m$^2$")
plt.ylabel("SalePrice in ZAR")
plt.title("Voting Ensemble Regression")
plt.legend()
plt.show()


# Heterogeneous Ensembles(Stacking)
models = [
    ("LR", lr),
    ("DT", regr_tree),
    ("SVR", svr)
]

# instead of choosing model weights, stacking uses a meta learner
# models training happens twice. once for base models, once for meta learner
meta_learner_reg = LinearRegression()

s_reg = StackingRegressor(
            estimators=models,
            final_estimator=meta_learner_reg
            )

s_reg.fit(x_train, y_train[:,0])

y_pred = s_reg.predict(x_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse}")

# Plot stacking regression prediction line over data
x_domain = np.linspace(min(x_train), max(x_train), 100)

y_pred_rescaled = y_scaler.inverse_transform(s_reg.predict(x_domain))
x_rescaled = x_scaler.inverse_transform(x_domain)

plt.figure()
plt.scatter(X, y)
plt.plot(x_rescaled, y_pred_rescaled, color='red', label='predictions')
plt.xlabel("LotArea in m$^2$")
plt.ylabel("SalePrice in ZAR")
plt.title("Stacking Ensemble Regression")
plt.legend()
plt.show()


# Homogeneous Ensembles

# Bagging (Bootstrap Aggregating)
d_tree = DecisionTreeRegressor(max_depth=4)

# Instantiate BaggingRegressor model with a decision tree as base model
bag_reg = BaggingRegressor(base_estimator=d_tree)
bag_reg.fit(x_train, y_train[:,0])

y_pred = bag_reg.predict(x_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse}")

# plot bagging regression prediction line
x_domain = np.linspace(min(x_train), max(x_train), 100)

y_pred_rescaled = y_scaler.inverse_transform(bag_reg.predict(x_domain))
x_rescaled = x_scaler.inverse_transform(x_domain)

plt.figure()
plt.scatter(X, y)
plt.plot(x_rescaled, y_pred_rescaled, color='red', label='predictions')
plt.xlabel("LotArea in M$^2$")
plt.ylabel("SalePrice in ZAR")
plt.title("Decision Tree Bagging Regression")
plt.legend()
plt.show()

# Instantiate decision tree regressor
d_tree = DecisionTreeRegressor(max_depth=3)

# Instantiate AdaBoostRegressor model with decision tree as base model
bst_reg = AdaBoostRegressor(base_estimator=d_tree)
bst_reg.fit(x_train, y_train[:,0])

y_pred = bst_reg.predict(x_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse}")

# plot the boosting regression prediction line over data
x_domain = np.linspace(min(x_train), max(x_train), 100)

y_pred_rescaled = y_scaler.inverse_transform(bag_reg.predict(x_domain))
x_rescaled = x_scaler.inverse_transform(x_domain)

plt.figure()
plt.scatter(X, y)
plt.plot(x_rescaled, y_pred_rescaled, color='red', label='predictions')
plt.xlabel("LotArea in m$^2$")
plt.ylabel("SalePrice in ZAR")
plt.title("Decision Tree Boosting Regression")
plt.legend()
plt.show()