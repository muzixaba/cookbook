#==================================================
# A collection of pandas tips and tricks
#==================================================

# Returns a series of col 'Age'
df['Age'] 

# Returns a dataframe with two columns, 'Age', 'Fare'
df[['Age', 'Fare']] 

# Delete a column
del df['col_name']

# Slicing rows from 2 up to but not including 8
df[2:8] 


# Slicing df using both a row and column names
df.loc['row_name', 'col_name'] 

# Change column data type
df['col_name'] = df['col_name'].astype('int64')

# Return df by column types
df.select_dtypes(exclude=['object','int64','float64','bool','datetime64','timedelta[ns]','category'])

# Finds sum of nans in each column
df.isna().sum()

# Count non-NA cells for each column or row.
df.count()

# Filter on age column greater than 30
df[df['Age'] > 30]

# Filter using two or more columns
df[(df['Age'] > 30) & (df['Overall'] > 90)]

# Create column from existing ones
df['Rating Per Year of Age'] = df['Overall'] / df['Age']

# Drop a column
df.drop('Rating Per Year of Age', axis=1)

# Get unique values from a series/column
df['col_name'].unique()

# Get sum/mean/min/max of df columns
df.mean()

#Count number of unique values in a series/column
df['col_name'].value_counts()

# Groupby some column & merge row enties entries into a list
col_list = df.groupby(["Col_Name"])['col_with_entries_to_list'].apply(list)


#==========================================
# Combining DataFrames
#=========================================

# Merged 2 dfs using different columns
new_df = pd.merge(left=df1, right=df2, how='inner', left_on='df1_col', right_on='df2_col')

# merge 2 dfs using their indecies
df3 = pd.merge(df1, df2, right_index=True, left_index=True)


#===========================
# Sorting by column
#==========================
df.sort_values(by='Age', ascending=False)

#===================
# Groupby
#===================

# Group by single column
df.groupby([by='Nationality').mean()[['cols','to','calculate','means']]


# Group by multiple columns
df.groupby(['Age', 'Nationality']).mean()

# Group by using custom aggregate function Survival rate by gender
df.groupby('Gender')[['Survived_Crash']].aggregate(lambda x: x.sum() / len(x)) 

#=======================
# Add rows/observations
#=======================
df = df.append({'col_name' : value} , ignore_index=True)

#==================================
# Apply Custom Functions 
#==============================

# Change days to years
df['num_of_days'].apply(lambda x: x/365)

