import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

# empty dictionary
D = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    ext = ext.lower()
    # create dictionary with ext = key, mt =value
    D[ext] = mt
# print(dict)

for i in range(q):
    fname = (input()).lower()  # One file name per line, lowercase

    parts = fname.split(".")
    if len(parts) < 2:
        print("UNKNOWN")
    else:
        end = parts[-1]

        sol = 0

        if end in D.keys():
            for i in D.keys():
                if end == i:
                    sol = D[i]

            print(sol)
        else:
            print("UNKNOWN")
