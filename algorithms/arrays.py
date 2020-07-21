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


# pair_sum([1,3,2,2], 4)

#===============
# Maximum Sum
#===============
# Take an array with +ve & -ve integers and return running max sum of that array
def largest_sum(arr):
    if len(arr) == 0:
        return print("too small")
    
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(current_sum, max_sum)
    
    return max_sum


# print(largest_sum([3,2,-5,7,8,-4,2]))


#=======================
# Reverse String
#=======================
# Given a string of words, reverse all the words
# e.g "This is the best" == "best the is This"
def reverse(s):
    length = len(s)
    spaces = [" "]
    words = []
    i = 0

    while i < length:
        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in spaces:
                i += 1 # increase i until we hit a space

            words.append(s[word_start:i])

        i += 1

    return " ".join(words[::-1])

# print(reverse("This is the best"))


#===================================
# Is one array a rotation of another
#===================================
# Given 2 arrays with no duplicates, is array one array a rotation of another (True or False)
def rotation(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    
    key = lst1[0]
    key_index = 0

    for i in range(len(lst2)):
        # search for where array 2 == key
        if lst2[i] == key:
            key_index = i
            break
    
    # if we don't find the key in array 2
    if key_index == 0:
        return False

    for x in range(len(lst1)):
        l2_index = (key_index+x) % len(lst1)

        if lst1[x] != lst2[l2_index]:
            return False
    
    return True

# print(rotation([3,4,5,6], [5,6,3,4]))


#=======================================
# Common elements in Two Sorted Arrays
#=======================================
# Return the common elements, as an array btw two sorted arrays
# e.g [1,3,4,6,7,9] & [1,2,4,5,9,10] == [1,2,3,9]
def common_elements(a,b):
    p1 = 0
    p2 = 0
    result = []

    while p1 < len(a) and p2 < len(b):
        if a[p1] == b[p2]:
            # add common element to result & increament pointers
            result.append(a[p1])
            p1 += 1
            p2 += 1
        elif a[p1] > b[p2]:
            p2 += 1
        else:
            p1 += 1
    
    return result
        
# print(common_elements([1,3,4,6,7,9], [1,2,3,4,9,10]))

#=============
# Minesweeper
#============
# Write a function that will take three arguments:
# bombs(list of bomb locations), rows, colums
# e.g mine_sweeper([[0,0], [1,2]], 3, 4)
def mine_sweeper(bombs, num_rows, num_cols):
    # create a 2D array to keep track of playing field size
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    
    # mark fields with bombs with a -1
    for bomb_location in bombs:
        bomb_row, bomb_col = bomb_location
        field[bomb_row][bomb_col] = -1

        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)

        for i in row_range:
            for j in col_range:
                if (0 <= i < num_rows and 0 <= j < num_cols and field[i][j] != -1):
                    field[i][j] += 1
    
    return field

# print(mine_sweeper([[0, 0], [1, 2]], 3, 4))


#======================
# Most occuring element
#======================
# Given an array, what is the most frequently occuring element
def most_frequent(lst):
    count = {}
    max_count = 0
    max_item = None

    for i in lst:
        # if element not in count yet, add it to count dict 
        if i not in count:
            count[i] = 1
        else:
            # add 1 to current count
            count[i] += 1
        
        # if item count > max_count, update max_count & max_item
        if count[i] > max_count:
            max_count = count[i]
            max_item = i

    return max_item, max_count

# print(most_frequent([1,3,3,3,2,1,1,1]))  

#=====================
# Check for unique characters in a string
#==========================================
# Given a string, are all the characters unique?
def unique(s):
    s = s.replace(" ", "")
    chars = set()
    for i in s:
        if i in chars:
            return False
        else:
            chars.add(i)
    return True




#===============
# Non Repeating Element
#=======================
# In a given string, return the character that never repeats
# If multiple uniques, return the first unique
def non_repeating(s):
    s = s.replace(" ", "").lower()
    char_count = {}
    # add char counts in to dict
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    # check which char has a count of 1
    for c in s:
        if char_count[c] == 1:
            return c
    
    return None


def max_num(items):
    """Returns the max value in a sequence"""
    max_no = items[0]
    index = 0
    for i in items:
        if i > max_no:
            max_no = i
        index += 1
    return max_no


print(max_num([2,4,6,3,3,1]))