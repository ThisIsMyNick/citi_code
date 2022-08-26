### flatten

"""
Given a nested list with arbitrary level of nesting, write a function, flatten to flatten it.

sample input:
x = [[4,5],[[1,2,3]],6]

flatten(x) --> [4,5,1,2,3,6]
"""

def flatten(L):
    result = []
    for e in L:
        if type(e) == type([]):
            result += flatten(e)
        else:
            result.append(e)
    return result

x = [[4,5],[[1,2,3]],6]
print(flatten(x))

x = [[4,5],[[1,2,3,[4,9]]],6,[[], [8]]]
print(flatten(x))
