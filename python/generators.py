def basic_generator():
    """Will yield numbers from 0 to 9"""
    for i in range(10):
        yield i

# Assign func to variable & call next() on it
gen = basic_generator()
print(next(gen))
print(next(gen))

def gen_with_multiple_yields():
    """Generators can have multiple yields"""
    count = 0
    for i in range(10):
        yield f"first yield: {i}"
        count += 1
        yield f"count is {count}"

gen_multiple = gen_with_multiple_yields()
print(next(gen_multiple))
print(next(gen_multiple))
print(next(gen_multiple))
# Generator comprehension
# Same syntax as list comprehension but () brackets
gen2 = (i for i in range(10))
print(next(gen2))
print(next(gen2))
print(next(gen2))
