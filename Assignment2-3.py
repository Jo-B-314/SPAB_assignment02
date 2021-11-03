import math

##
# Table of Binomial coefficients
##
def binomial(n,k):
    if (k > n) :
        print("\n" "0")
    else:
        for i in range(n+1):
            print('% 2d'% i, end = ' ')
            x = 1
            for j in range(k+1):
                if i != 0 and j != 0:
                    x = x * (i-j + 1) / j
                print('% 4d'% x, end = ' ')
            print("\n", end = '')

## Stirling numbers
def stirlingsubset(n,k):
    if (k > n) :
        print("\n" "0")
    else:
        for i in range(n+1):
            print('% 2d'% i, end = ' ')
            x = 1
            for j in range(k+1):
                if i != 0 and j != 0:
                    sum = 0
                    ##x = (pow(j,i)-j)/j hinten raus werte zu hoch
                    for y in range(j):
                        sum = sum + pow(-1, y) * math.comb(j, y) * pow(j-y,i)
                    x = 1/math.factorial(j) * sum
                print('% 4d'% x, end = ' ')
            print("\n", end = '')

## Stirling cycle numbers
def stirlingcycle(n,k):
    if (k > n) :
        print("\n" "0")
    else:
        for i in range(n+1):
            print('% 2d'% i, end = ' ')
            x = 1
            for j in range(k+1):
                if i != 0 and j != 0:
                    sum = 0
                    ##x = (pow(j,i)-j)/j hinten raus werte zu hoch
                    for y in range(j):
                        sum = sum + pow(-1, y) * math.comb(j, y) * pow(j-y,i-1)
                    x = 1/math.factorial(j) * sum
                print('% 4d'% x, end = ' ')
            print("\n", end = '')

## PRINTING
print("Enter n: ")
n = int(input())
print("Enter k: ")
k = int(input())

print('BINOMIAL')
binomial(n,k)
print('STIRLING SUBSET')
stirlingsubset(n,k)
print('STIRLING CYCLES')
stirlingcycle(n,k)