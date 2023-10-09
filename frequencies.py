"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    for i in items:
        i = str(i)
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies.setdefault(i,1)

    return frequencies
