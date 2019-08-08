#==================================================
# A collection of pandas tips and tricks
#==================================================

# Delete a column
del df['col_name']

# Change column data type
df['col_name'] = df['col_name'].astype('int64')

# Return df by column types
df.select_dtypes(exclude=['object','int64','float64','bool','datetime64','timedelta[ns]','category'])

# Finds sum of nans in each column
df.isna().sum()

# Count non-NA cells for each column or row.
df.count()


#==========================================
# Combining DataFrames
#=========================================

# Merged 2 dfs using different columns
new_df = pd.merge(left=df1, right=df2, how='inner', left_on='df1_col', right_on='df2_col')

# merge 2 dfs using their indecies
df3 = pd.merge(df1, df2, right_index=True, left_index=True)