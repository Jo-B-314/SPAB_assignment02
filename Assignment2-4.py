import math

##
# Table of Binomial coefficients
##
def binomial(input):

    for i in range(input+1):
        print('% 2d'% i, end = ' ')
        x = 1
        for j in range(i+1):
            if i != 0 and j != 0:
                x = x * (i-j + 1) / j
            print('% 4d'% x, end = ' ')
        print("\n", end = '')

## Stirling numbers
def stirlingsubset(input):
    for i in range(input+1):
        print('% 2d'% i, end = ' ')
        x = 1
        for j in range(i+1):
            if i != 0 and j != 0:
                sum = 0
                ##x = (pow(j,i)-j)/j hinten raus werte zu hoch
                for y in range(j):
                    sum = sum + pow(-1, y) * math.comb(j, y) * pow(j-y,i)
                x = 1/math.factorial(j) * sum
            print('% 4d'% x, end = ' ')
        print("\n", end = '')

## Stirling cycle numbers
def stirlingcycle(input):
    for i in range(input+1):
        print('% 2d'% i, end = ' ')
        x = 1
        for j in range(i+1):
            if i != 0 and j != 0:
                sum = 0
                ##x = (pow(j,i)-j)/j hinten raus werte zu hoch
                for y in range(j):
                    sum = sum + pow(-1, y) * math.comb(j, y) * pow(j-y,i-1)
                x = 1/math.factorial(j) * sum
            print('% 4d'% x, end = ' ')
        print("\n", end = '')

## PRINTING
print('BINOMIAL')
binomial(9)
print('STIRLING SUBSET')
stirlingsubset(9)
print('STIRLING CYCLES')
stirlingcycle(9)