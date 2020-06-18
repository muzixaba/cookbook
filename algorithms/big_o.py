#===========
# Intro
#===========
# Big O measures the effeciency of an algorithm.
# Looks at the number of assignments made to n
# Uses time & space (memory) complexities to do the measurements
# Time complexity looks at how quickly runtime will grow
# Space complexity looks at how much memory will be used

# O(n) - Linear growth
def adder(n):
    """Inputs n & returns th sum of numbers from 0 to n"""
    final_sum = 0
    for x in range(n+1): # n is assigned n times
        final_sum += x
    return final_sum


# O(1) - Constant
def adder2(n):
    """Inputs n & returns the sum of numbers from 0 to n"""
    return (n*(n+1))/2 # n is assigned only once

def first_element(n):
    '''Returns the first element of a list'''
    return n[0]


# O(n**3) - Cubic
def nightmare(n):
    return 20*n**3 + 15*n**2 + 8
# The big limiting factor is the n**3


# log(n) - Lagarithmic
# nlog(n) - Log Linear
# n**2 - Quadratic
# 2**n - Exponantial

from math import log
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

# runtime comparisons
n = np.linspace(1,10)
labels = ["Constant", "Logarithmic", "Linear", "Log Linear", "Quadratic",
        "Cubic", "Exponential"]
big_o = [np.ones(n.shape), np.log(n), n, n*np.log(n), n**2, n**3, 2**n]

# plot
plt.figure(figsize=(12,10))
plt.ylim(0,50)
for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])
plt.legend(loc=0)
plt.ylabel("Relative Runtime")
plt.xlabel("n")
plt.title("Big O")
plt.show() 