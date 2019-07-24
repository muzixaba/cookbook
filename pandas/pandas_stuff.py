#==================================================
# A collection of pandas tips and tricks
#==================================================

# Return df by column types
df = df.select_dtypes(exclude=['object','int64','float64','bool','datetime64','timedelta[ns]','category'])

# Finds sum of nans in each column
df.isna().sum()

