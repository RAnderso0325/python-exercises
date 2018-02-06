# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example method call
#
# factorial(5)
#
# > 120
#

def factorial(num):
    tot = 1
    if(num == 0):
        tot = 1
    else:
        for i in range(2,num+1):
            tot *= i
    print(tot)

factorial(5)