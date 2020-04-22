import seaborn as sns

# Load seaborn dataset(s)
# dataset_names = exercise, titanic, iris, etc
data = sns.load_dataset("dataset_name")


#===================
# Distribution Plots
#===================

# Distplot
#----------
sns.distplot(df['col_name'], bins=30)


# Joint Plot
#------------
# Joins two distribution plots By adding a scatter/hex,regression plot
sns.jointplot(x='col_1', y='col_2', data=df, kind='scatter')


# Pair Plot
#----------
# Creates joint plots for the numerical data in your df
# Add 'hue' arg to add color to categorical data
# Add 'pallet' argument to add pallete to graphs
sns.pairplot(df)



# Rug Plot
#------------
# Similar to distribution plot by uses dashes to show points
sns.rugplot(df['col_name'])


# Kde Plot
#------------
# Returns kde plot without distribution
# KDE == Kernel Density Estimation. The sum of all distributions in a graph
sns.kdeplot(df['col_name'])


#===================
# Categorical Plots
#===================

# Bar Graphs
#------------
sns.barplot(x='col_1', y='col_2', data=df)


# Count Plot
#------------
# Counts the number of occurances
sns.countplot(x='col_name', data=df)


# Box Plot
#------------
sns.boxplot(x='col_1', y='col_2', data=df)


# Violin Plot
#------------
# Similar to boxplot but may be harder to read
sns.violinplot(x='col_1', y='col_2', data=df)


# Strip Plot
#------------
sns.stripplot(x='categorical_col', y='numerical_col', data=df)


# Swarm Plot
#------------
# Mix between violin & stripplot
sns.swarmplot(x='categorical_col', y='numerical_col', data=df)


# Factor Plot
#------------
# Mimicks all other categorical plots
sns.factorplot(x='col_1', y='col_2', data=df, kind='*')


#===================
# Matrix Plots
#===================

# Heatmap
#--------
# Data has to be already in matrix form
sns.heatmap(data)


# Cluster Map
#------------
# Similar to heatmap but adds tree type diagram to show clusters
sns.clustermap(data)


#========
# Grids
#========

# Pair Grid
#----------
# Subplot grid for plotting pairwise relationships in dataset
iris = sns.load_dataset('iris', hue='species') # dataset is a DataFrame
grid = sns.PairGrid(iris) # Create instance of PairGrid
grid = grid.map(plt.scatter) # Runs map method to display results

# Show a univariate ditribution on the diagonal
g = sns.PairGrid(iris, hue='species')
g = g.map_diag(plt.hist)
g = g.map_offdiag(plt.scatter)


# Facet Grid
#-----------
g = sns.FacetGrid(data=df, col='col_1', row='col_2')
g.map(sns.distplot, 'col_3')