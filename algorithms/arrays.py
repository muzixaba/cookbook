# Array indexing is O(1)

# python autmatically/dynamically allocates memory for arrays
import sys
def mem_size(n):
    data = []
    for i in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print(f"Length: {a:3d}; Size in bytes: {b:4d}")
        data.append(n)
# mem_size(10)

#==========
# Anagrams
#==========
# Check if two words are anagrams
# An anagram is when two string can be written using the exact same letters
# Example: "public relations" == "crap built on lies"
# Note: Spaces & Capitalization to be ignored
def anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2) # using a builtin function

# print(anagram('dog', 'god'))

def anagram2(s1, s2):
    """Designed using no built in functions"""
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    # Create dict to check letter frequency
    count = {}
    # add letters and their frequency using s1
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    # decrease letter counts using s2
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    # check the counts values & return False if any are above 0
    for key in count: # looping through a dict using its keys
        if count[key] != 0:
            return False
    
    return True

# print(anagram2("clint eastwood", "old west action"))

#===============
# Array Pair Sum
#===============
# Given an int array, outpu all the unique pairs that sum up to
# a specific value k
# pair_sum([1,3,2,2], 4) == [[1,3],[2,2]]

def pair_sum(array, k):
    if len(array) < 2:
        return print("array too small")

    seen = set()
    output = set()

    for num in array:
        target = k - num
        
        if target not in seen:
            seen.add(num) #TODO: set methods
        else:
            output.add((min(num, target), max(num, target)))

    print("\n".join(map(str, list(output))))


pair_sum([1,3,2,2], 4)

# end time 1:20:47