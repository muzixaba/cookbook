import matplotlib.pyplot as plt
import seaborn as sns

# Load seaborn dataset(s)
# dataset_names = exercise, titanic, iris, etc
data = sns.load_dataset("dataset_name")


#===================
# Distribution Plots
#===================

# Distplot
#----------
# Similar to plt.hist. Estimates the required num of bins. Adds kde plot
iris = sns.load_dataset('iris')
sns.distplot(iris['sepal_length'], kde=True)
plt.xlabel('Sepal Lenght in CM')
plt.ylabel('Distribution')
plt.title('Distribution of Sepal Length')
plt.show()


# Joint Plot
#------------
# Joins two distribution plots By adding a scatter/hex,regression plot
iris = sns.load_dataset('iris')
sns.jointplot(x='sepal_length', y='petal_length', data=iris, kind='scatter')
plt.show()


# Pair Plot
#----------
# Creates joint plots for the numerical data in your df
# Add 'hue' arg to add color to categorical data
# Add 'pallet' argument to add pallete to graphs
sns.pairplot(iris)
plt.show()



# Rug Plot
#------------
# Similar to distribution plot by uses dashes to show points
sns.rugplot(iris['sepal_length'])
sns.rugplot(np.random.random(100))
plt.show()

# Kde Plot
#------------
# Returns kde plot without distribution
# KDE == Kernel Density Estimation. The sum of all distributions in a graph
sns.kdeplot(iris['sepal_length'])


#===================
# Categorical Plots
#===================

# Bar Graphs
#------------
sns.barplot(x='species', y='sepal_length', data=iris)
plt.title('Chart Title')
plt.show()

# Count Plot
#------------
# Counts the number of occurances
sns.countplot(x='col_name', data=df)


# Box Plot
#------------
# Shows the spread of data points
# Range = lowest_point - highest_point
# Median = center line inside box
sns.boxplot(x='species', y='sepal_length', data=iris)
plt.title('Chart Title')
plt.show()

# Violin Plot
#------------
# Similar to boxplot but may be harder to read
sns.violinplot(x='species', y='sepal_length', data=iris)
plt.title('Chart Title')
plt.show()

# Strip Plot
#------------
# sns.stripplot(x='categorical_col', y='numerical_col', data=df)
sns.stripplot(x='species', y='sepal_length', data=iris)
plt.title('Chart Title')
plt.show()

# Swarm Plot
#------------
# Mix between violin & stripplot
# sns.swarmplot(x='categorical_col', y='numerical_col', data=df)
sns.swarmplot(x='species', y='sepal_length', data=iris)
plt.title('Chart Title')
plt.show()

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
flights = sns.load_dataset('flights')
flights = flights.pivot("month", 'year', 'passengers')
heat_map = sns.heatmap(flights)
plt.title('Chart Title')
plt.show()


#========
# Grids
#========

# Pair Grid
#----------
# Subplot grid for plotting pairwise relationships in dataset
iris = sns.load_dataset('iris') # dataset is a DataFrame
grid = sns.PairGrid(iris, hue='species') # Create instance of PairGrid
grid = grid.map(plt.scatter) # Runs map method to display results
plt.title('Chart Title')
plt.show()

# Show a univariate ditribution on the diagonal
g = sns.PairGrid(iris, hue='species')
g = g.map_diag(plt.hist)
g = g.map_offdiag(plt.scatter)
plt.title('Chart Title')
plt.show()

# Facet Grid
#-----------
# g = sns.FacetGrid(data=df, col='col_1', row='col_2')
# g.map(sns.distplot, 'col_3')