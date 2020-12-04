"""
Challenge #8:

Create a function that returns the number of arguments it was called with.

Examples:
- num_args() ➞ 0
- num_args("foo") ➞ 1
- num_args("foo", "bar") ➞ 2
- num_args(True, False) ➞ 2
- num_args({}) ➞ 1
"""
# ...array


def num_args(*args):
    print(len(args))
    return


num_args()
num_args("foo")
num_args("foo", "bar")
num_args(True, False)
num_args({})
