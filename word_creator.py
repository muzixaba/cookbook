"""
A script used to create words from given characters
"""
from itertools import permutations
import argparse

def word_permutations(args):
    """
    Takes in string and returns a list containing
    various combinations of that string

    Example:
    create_word('abc') == ['abc','bac', 'cab']
    """
    words = []
    combos = permutations(args.initial_string)
    for word in combos:
        words.append(word)

    return [" ".join(w) for w in words]


# print(word_permutations('abc'))

def main():
    parser = argparse.ArgumentParser(
                        prog="Word Permutations",
                        description="Return permuations of a string")
    parser.add_argument("-str", "--initial_string", type=str, help="Enter string to be used for permutaions")
    args = parser.parse_args()
    print(word_permutations(args))

if __name__ == "__main__":
    main()