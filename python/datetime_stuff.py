# %%
from datetime import datetime as dt

#========
#Timestamps
#========

# Creating a timestamp (timezone unaware == UTC)
# Returns a float, accurate down to nanosecond
# Cast to int if fine with accuracy down to second
ts = dt.timestamp(dt.now()) # -> 1623147020.690588

# Read timestomp
datetime_obj = dt.fromtimestamp(ts)

# Read string rep of time
datetime_obj.strftime("%d %b %Y %H:%M:%S")

# %%
# read formatted time string
date_time_str = '18/09/19 01:55:19'
date_time_obj = dt.strptime(date_time_str, '%d/%m/%y %H:%M:%S')