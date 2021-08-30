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

# Change value at specific cell
df.set_value(index, 'col_name', value)
df.loc[condition, 'col_name'] = new_value
df['col_name'] = np.where(condition, new_value, df['col_name'])


# Change column data type
df['col_name'] = df['col_name'].astype('int64')

# Return df by column types
df.select_dtypes(exclude=['object','int64','float64','bool','datetime64','timedelta[ns]','category'])

# Finds sum of nans in each column
df.isna().sum()

# replace nans with empty string
df = df.fillna('')

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

# Delete multiple columns
df.drop(["col_1", "col_2"], axis=1)

# drop a specific row by index
df.drop(df.index[0])

# drop row with specif index name
df.drop("Ireland", axis=0)

# Drop the rows specific indicies
df.drop([0,1,2], axis=0)

# drop rows by index name
df.drop(['index_1', 'index_2'])

# drop a row(s) if it contains a specific value
df[df['col_name'] != 'value']

# Get unique values from a series/column
df['col_name'].unique()

# Get sum/mean/min/max of df columns
df.mean()

#Count number of unique values in a series/column
df['col_name'].value_counts()

# Groupby some column & merge row enties entries into a list
col_list = df.groupby(["Col_Name"])['col_with_entries_to_list'].apply(list)

# Rename Columns
df.rename(columns={"old1": "new1", "old2": "new2"})

# Rename index
df.rename(index={0: "x", 1: "y", 2: "z"})

# set column as index, inplace
df.set_index('Date', inplace=True)

# Slice datetime index
df['2020-01':'2020-02']

# dropping ALL duplicte values  in certain column
df.drop_duplicates(subset ="ref_colName", keep='first', inplace=True) 

# Export df as csv
df.to_csv(r'Path\To\File_Name.csv', index = False)

#=============
# Math Functions
#=============

# Get column totals
df.loc['Column_Total']= df.sum(numeric_only=True, axis=0)
# Get row totals
df.loc[:,'Row_Total'] = df.sum(numeric_only=True, axis=1)

# Create new column with row sums
df["sum"] = df.sum(axis=1)

#==========================================
# Combining DataFrames
#=========================================

# Merged 2 dfs using different columns
new_df = pd.merge(left=df1, right=df2, how='inner', left_on='df1_col', right_on='df2_col')

# merge 2 dfs using their indecies
df3 = pd.merge(df1, df2, right_index=True, left_index=True)

# join dfs at the end of each other
df_all = pd.concat([df1, df2, df3], ignore_index=True)

#===========================
# Sorting by column
#==========================
df.sort_values(by='Age', ascending=False)

#================
# Transposing a df
#=================
df.T

#===================
# Groupby
#===================

# Group by single column
df.groupby([by='col_name']).mean()[['cols','to','calculate','means']]


# Group by multiple columns
df.groupby(['Age', 'Nationality']).mean()

# Group by using custom aggregate function Survival rate by gender
df.groupby('Gender')[['Survived_Crash']].aggregate(lambda x: x.sum() / len(x)) 



#=======================
# Add rows/observations
#=======================

# Add single row
df = df.append({'col_name' : value} , ignore_index=True)

# Populate df using for loop
for i in iterable:
    df = df.append({'col_name' : value} , ignore_index=True)

# Add values for specific column after certain index
df['col_name'][df.index > 60] = 'scalar value after index=60'

# Add random choice in a new column
df['NewCol'] = df['AnyCol'].apply(lambda x: random.choice(('yes', 'no')))



#========================
# Apply Custom Functions 
#========================

# Change days to years
df['num_of_days'].apply(lambda x: x/365)

# add thousand separators
df['thousands_sep'] = df['values'].apply(lambda x: '{:,}'.format(x))



#============
# TimeSeries
#============

# from timestamp to string
dt.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

# Change column type to datetime
df['date'] = pd.to_datetime(df['date']) # if pandas can read the date string
df["date"] = pd.to_datetime(["date"], format='%Y-%m-%d %I-%p') # to tell pandas exactly what the string looks like

# Parse datetime at import
d_parser = lambda x: pd.datetime.strptime(x, "%Y-%m-%d %I-%p")
df = pd.read_csv("ETH_1h.csv", parse_dates=["Date"], date_parser=d_parser)

# fiter df by datetime
date_filter = (df["Date"] >= "2019") & (df["Date"] < "2020") # time as strings
date_filter2 = (df["Date"] >= pd.to_datetime('2019-01-01')) & (pd.to_datetime('2020-01-01')) # time as datetime

df.loc[date_filter]