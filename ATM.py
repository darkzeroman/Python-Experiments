# http://www.codechef.com/problems/HS08TEST

from decimal import Decimal

input_str = raw_input().split()

withdraw = int(input_str[0])
funds = Decimal(input_str[1])

if withdraw % 5 != 0:
    print funds
elif withdraw + 0.50 > funds:
    print funds
else:
    print (funds - withdraw - Decimal(0.50))
