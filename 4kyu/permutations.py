#PROBLEM: https://www.codewars.com/kata/5254ca2719453dcc0b00027d

#SOLUTION:
import itertools
def permutations(string):
    perm = list(itertools.permutations(string))
    perm = set(["".join(list(item)) for item in perm])
    return list(perm)
