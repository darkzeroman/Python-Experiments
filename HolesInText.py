
# http://www.codechef.com/problems/HOLES

n = int(raw_input())

def fn(x):
    if x in "ADOPQR":
        return 1
    if x in "CEFGHIJKLMNSTUVWXYZ":
        return 0
    if x in "B":
        return 2

for i in range(n):
    print sum(map(fn, list(raw_input())))
