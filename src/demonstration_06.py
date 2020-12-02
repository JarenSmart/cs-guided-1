"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""


def XO(txt):
    # txt_lower = txt.lower()
    # return txt_lower.count('x') == txt_lower.count('o')
    txt_lower = txt.lower()
    count_x = 0
    count_o = 0
    # loop over each character, and count X and O
    for char in txt_lower:
        # check if char is X or O
        if char == 'x':
            count_x += 1
        elif char == 'o':
            count_o += 1

    return count_x == count_o


print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zpzpzpp"))
print(XO("zzoo"))
