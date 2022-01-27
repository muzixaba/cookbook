"""
sys.argv() returns a list of all command line args that were passed
sys.argv[0] is the name of the script
"""

# simple sys.argv program
import sys
print(f"Name of program: {str(sys.argv[0])}")
print(f"List of args: {str(sys.argv())}")