# Stuff around using the ipython repl

# Get object doctstring
?obj_name

# Read obj documentation
??obj_name

# find methods matching a certain string
import os
?os.*dir* #returns all methods containing 'dir'

# retrive output from specific cell
Out[<cell-number>]

# avoid storing results of a cell in cache
# also suppresses output
1+2;

# ==========
# Magic Funcitons: Over 120 in total
#==========
# Start with % = line magic or %% = cell magic

# Check execution time using line magic
#  %timeit -n 100 -r 3 sum(range(5))

# Check time to run code using cell magic
#. %%timeit -n 100 -r 3
# total = 0
# for x in range(5): total += 1

# Return history of commands
# %history

# Ask ipython to open command in text editor
# %edit

# Run py script and load its data into current namespace
# %run

# Run other programming languages in ipython
#. %%javascript

# Load extenstions already on sytem
# %load_ext <extension_name>

# Run shell commands
!pwd

# Auto-await async code
await obj_name

# View stacktrace of last error/exception
# %debug

# Profile code
# %prun func_name()