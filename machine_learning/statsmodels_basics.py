
from statsmodels.graphics.correlation import plot_corr
from statsmodels.graphics.gofplots import qqplot
import statsmodels.formula.api as sm
from statsmodels.stats.outliers_influence import OLSInfluence as influence
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#data import
df = pd.read_csv(
        'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/regression_sprint/mtcars.csv',
        index_col=0
        )

# calculate corralations between the features
corr = df.drop('mpg', axis=1).corr()

# Draw a heatmap to check Multicollinearity
fig = plot_corr(corr, xnames=corr.columns)

# String 2b used to Regress y on X (y~X)
formular_str = df['mpg'].name+"~"+"+".join((df.drop('mpg', axis=1)).columns)

# Fit model
model = sm.ols(formula=formular_str, data=df)
fitted = model.fit()

# Print model summary
print(fitted.summary())

# Visualising Resuduals vs Predictor Variable Plots
# Checking for independence
fig, axs = plt.subplots(2,5, figsize=(14,6), sharey=False)
fig.subplots_adjust(hspace=0.5, wspace=0.2)
fig.suptitle("Predictor variables vs Model Residuals", fontsize=16)
axs = axs.ravel() #?????

for index, column in enumerate(df.columns):
    axs[index-1].set_title(f"{column}", fontsize=12)
    axs[index-1].scatter(x=df[column], y=fitted.resid,
                        color='blue', edgecolor='k'
                        )
    axs[index-1].grid(True)
    xmin = min(df[column])
    xmax = max(df[column])
    axs[index-1].hlines(y=0, xmin=xmin*0.9, xmax=xmax*1.1,
                        color='red', linestyle="--", lw=3
                        )
    if index==1 or index==6:
        axs[index-1].set_ylabel("Residuals")

# Checking for Homoscedasticity
# Fitted vs Residuals (If variance is constant, there's homoscedasticity)
# If  variance is not constant, heteroscedasticity is observed
plt.figure(figsize=(8,3))
p = plt.scatter(x=fitted.fittedvalues, y=fitted.resid, edgecolor='k')
xmin = min(fitted.fittedvalues)
xmax = max(fitted.fittedvalues)
plt.hlines(y=0, xmin=xmin*0.9, xmax=xmax*1.1, color='red', linestyle='--', lw=3)
plt.xlabel("Fitted Values", fontsize=15)
plt.ylabel("Residuals, fontsize=15")
plt.title("Fitted vs Residuals Plot", fontsize=18)
plt.grid(True)
plt.show()

# Checking for normality
# Histogram of Normalised Residuals
plt.figure(figsize=(8,5))
plt.hist(fitted.resid_pearson, bins=8, edgecolor='K')
plt.ylabel("Count", fontsize=15)
plt.xlabel("Normalized Residuals", fontsize=15)
plt.title("Histogram of normalized residuals", fontsize=18)
plt.show()

# Quantile-Quantile Plot
plt.figure(figsize=(8,5))
fig = qqplot(fitted.resid_pearson, line="45", fit='True')
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.xlabel("Theoratical Quantiles", fontsize=15)
plt.ylabel("Sample Quantiles", fontsize=15)
plt.title("Q-Q plot of normalized residuals", fontsize=18)
plt.grid(True)
plt.show()

# Checking for outliers in residuals
# Green line is 4x > Cook's distance mean
inf = influence(fitted)
(c, p) = inf.cooks_distance
plt.figure(figsize=(8,5))
plt.title("Cook's distance plot for the residuals", fontsize=16)
plt.stem(np.arange(len(c)), c, markerfmt=",", use_line_collection=True)
plt.hlines(y=c.mean()*4, xmin=0, xmax=fitted.fittedvalues*1.1, colors='green', linestyle='--')
plt.grid(True)
plt.show()