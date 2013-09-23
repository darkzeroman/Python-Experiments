#!/bin/python

# Head ends here
def partition(ar):
    smaller = []
    larger = []

    for i in ar[1:]:
        if i < ar[0]:
            smaller.append(i)
        else:
            larger.append(i)

    print " ".join(map(str, (smaller+ [ar[0]] + larger)))

def swap(ar, first, second):
    temp = ar[first]
    ar[first] = ar[second];
    ar[second] = temp
# Tail starts here

partition([4, 5, 3 ,7, 2])