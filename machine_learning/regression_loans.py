import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.correlation import plot_corr

df = pd.read_csv('https://raw.githubusercontent.com/Explore-AI/Public-Data/master/bootcamps/Personal_Loans.csv')
df.head()

# Insert underscores on column names
df.columns = [col.replace(" ","_") for col in df.columns]

# Look at customers who've already taken out a loan
df = df[df['Personal_Loan']==1] # return df where personal loan has been taken out
y = df['Personal_Loan']
df = df.drop(["Personal_Loan"], axis=1)

# get dummies
df_dummies = pd.get_dummies(df)

# Move response to end of df
col_titles = [col for col in df_dummies.columns if col!='Loan_Size'] + ["Loan_Size"]
df_dummies = df_dummies.reindex(columns=col_titles)

# plot corralation heatmap using statsmodels
fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111)
plot_corr(df_dummies.corr(), xnames=df_dummies.corr().columns, ax=ax)