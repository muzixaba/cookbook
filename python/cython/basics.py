"""
QUICK INTRO
-----------
Cython is a programming language that helps you to move between Python and C/C++ easily.
It's a superset of python
Speeds up python code using CPython

STEPS
-----
- Change file extension to .pyx (cython file extension)
- Change python objects into c types (cdef, cpdef)
- Compile pyx file into C-code using Cython.
- Compile this C-code using a C-Compiler (gcc) that turns the code into a shared library/object (.so) or extension module.
- Import the library back into python & be amazed at the speed gains.

INSTALL
-------
sudo apt-get install cython
pip install cython
Comes with Anaconda, i think

EXTRAS
------
Use CProfile to see where to optimize
cython -a file_name.py => file_name.html which shows which lines are causing the script to be slow
"""

#======================
# Define functions
#======================
def python_only(a, b):
    result = a + b + c
    return result

cdef c_only(int a, double b):
    cdef c int # static type declaration
    result = a + b * c
    return result

cpdef double hybrid(int a, double b):
    cdef c int
    result = a + b + c
    return result




#================================
# Create setup.py and add the ff
#================================
from distutils.core import setup, Extension
from Cython.Distutils import build_ext
    setup(
        cmdclass={'build ext':build_ext},
        ext_modules=[Extension('file_name', ['file_name.pyx'])]
    )

#===================
# Run setup.py
#===================
python setup.py build_ext --inplace



#=========================
# Inside Jupyter notebook
#========================

# load cython ext right at the top
%load_ext Cython

# import Cython

# run a cell using cython & annotate it
# jupyter compiles & does the import in the background
%%cython -a 

@cython.cfunc # good for internal functions
def some_calculation(value: cython.double) -> cython.double:
    # uses python's type annotation
    cdef double some_multiplier
    result = value * some_multiplier
    return result
