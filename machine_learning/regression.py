# Fits a line through the data

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

from skelearn import metrics

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_stat=50)

# Fit model
lm = LinearRegression()
lm.fit(X_train, y_train)

# Check for errors in train data predictions
y_pred_train = lm.predict(X_train)
mse = metrics.mean_squared_error(y_train, y_pred_train)
r2 = metrics.r2_score(y_train, y_pred_train)

# Make predictions in unseed data
y_pred = lm.predict(X_test)


# Check for errors
print(metrics.mean_squared_error(y_test, y_pred))
print(metrics.r2_score(y_test, y_pred))