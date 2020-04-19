import seaborn as sns

#================
# Distribution Plot
#================
sns.distplot(df['col_name'], bins=30)

#================
# Joint Plot
#================
# Joins two distribution plots By adding a scatter/hex,regression plot
sns.jointplot(x='col_1', y='col_2', data=df, kind='scatter')

#===============
# Pair Plot
#===============
# Creates joint plots for the numerical data in your df
# Add 'hue' arg to add color to categorical data
# Add 'pallet' argument to add pallete to graphs
sns.paiplot(df)


#================
# Rug Plot
#================
# Similar to distribution plot by uses dashes to show points
sns.rugplot(df['col_name'])

#===============
# Kde Plot
#==============
# Returns kde plot without distribution
# KDE == Kernel Density Estimation. The sum of all distributions in a graph
sns.kdeplot(df['col_name'])

#===================
# Bar Graphs
#====================
sns.barplot(x='col_1', y='col_2', data=df)

#================
# Count Plot
#================
# Counts the number of occurances
sns.countplot(x='col_name', data=df)

#===============
# Box Plot
#==============
sns.boxplot(x='col_1', y='col_2', data=df)

#===========
# Violin Plot
#============
# Similar to boxplot but may be harder to read
sns.violinplot(x='col_1', y='col_2', data=df)

#==================
# Strip Plot
#==================
sns.stripplot(x='categorical_col', y='numerical_col', data=df)

#===============
# Swarm Plot
#===============
# Mix between violin & stripplot
sns.swarmplot(x='categorical_col', y='numerical_col', data=df)