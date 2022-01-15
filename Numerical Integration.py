
====================================================================='''
from os import system
from prettytable import PrettyTable
from math import *
import sympy as sp
x = sp.Symbol('x')
system("cls")
# ------------------------------------------------------------------------------
# Method used to cut float numbers to the 4th decimal, without rounding.
def truncate(num):
    return floor(float(num) * 10 ** 4) / 10 ** 4
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Method used to calculate the average between two numbers.
def average(numOne, numTwo):
    avg = (numOne + numTwo) / 2
    return avg
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Method used to calculate f(X) according to user's input function.
def fX(x, function):
    func = eval(function)
    return func
# ------------------------------------------------------------------------------

function = str(input("Input function: "))
A = float(input("Enter the First Interval: "))
B = float(input("Enter the Last Interval: "))
H = float(input("Enter the Interval Width: "))

# function = 'sin(x)'
# A = 0
# B = 2
# H = 0.5

print('=' * 50)
import sympy
integ_Function = sympy.integrate(function)
# print(integ_Function)
Exact = fX(B, str(integ_Function)) - fX(A, str(integ_Function))
Exact = truncate(Exact)
print('>> Exact:', Exact)

# MidPoint = (B-A) * f(B-A/2)
numerical_mid = truncate((B - A) * fX(((B - A) / 2), function))

# Trapezoidal = (B-A) * (f(A) + f(B) / 2)
numerical_trap = truncate((B - A) * ((fX(A, function) + fX(B, function)) / 2))

# Simpson = (B-A / 6) * (f(A) + [4*f(A+B/2)] + f(B))
numerical_simpson = truncate(( ((B - A) / 6) * ((fX(A, function) + (4 * fX(((A + B) / 2), function)) + fX(B, function)))))

print(">> Numerical Midpoint (normal):", numerical_mid)
print(">> Numerical Trapezoidal (normal):", numerical_trap)
print(">> Numerical Simpson (normal):", numerical_simpson)
print('=' * 50)

Intervals = [A]

tempA = A
FLAG = True
while FLAG:
    subInterval = tempA + H
    Intervals.append(subInterval)
    if subInterval >= B:
        FLAG = False
    else:
        tempA = subInterval
        
print('>> Intervals:', Intervals)

innerSubIntervals = [truncate(average(Intervals[i], Intervals[i+1])) for i in range(0, len(Intervals)-1)]
innerSubFunctions = [truncate(fX(subSubInterval, function)) for subSubInterval in innerSubIntervals]

print('>> innerSubIntervals:', innerSubIntervals)
print('>> innerSubFunctions:', innerSubFunctions)

SUM_xStar = truncate(sum(innerSubFunctions))
print('>> Sum of X*:', SUM_xStar)
print('=' * 50)


table_compMid = PrettyTable()
table_compMid.add_column("X", innerSubIntervals)
table_compMid.add_column("f(X)", innerSubFunctions)
print(table_compMid.get_string(title="Composite Midpoint",padding_width=5))


COMP_mid = truncate(H * SUM_xStar)
print(">> Composite Midpoint:", COMP_mid)
print('=' * 50)
fX_subIntervals = [] 
for i in range (len(Intervals)):
    afterProcess = truncate(fX(Intervals[i], function))
    fX_subIntervals.append(afterProcess)

# print('>> Sub-Intervals:', (fX_subIntervals))

table_compTrap = PrettyTable()
table_compTrap.add_column("X", Intervals)
table_compTrap.add_column("f(X)", fX_subIntervals)
print(table_compTrap.get_string(title="Intervals",padding_width=5))


SUM_middleFX = 0
for i in range (1, len(fX_subIntervals)-1):
    middleFX = 2 * fX_subIntervals[i]
    SUM_middleFX = SUM_middleFX + middleFX

COMP_trap = truncate((H/2) * ( (fX(A, function)) + SUM_middleFX + (fX(B, function))  ))
print(">> Composite Trapezoidal:", COMP_trap)
print('=' * 50)
SUM_middleFX = 0

for i in range (1, len(fX_subIntervals)-1):
    if i % 2 == 0:
        SUM_middleFX = SUM_middleFX + (2* fX_subIntervals[i])
    else:
        SUM_middleFX = SUM_middleFX + (4* fX_subIntervals[i])

COMP_simpson = truncate((H/3) * ( ((fX(A, function))) + SUM_middleFX + ((fX(B, function))) ))

print('>> Composite Simpson:', COMP_simpson)
print('=' * 50)
# from math import *
# x = (3-2.75)*(3-4) // ((2-2.75)*(2-4)) * 0.5
# y = (3.2)*(3-4) // (2.75-2)*(2.75-4) * (4/11)
# z = (3-2)*(3-2.75) // (4-2)*(4-2.75) * (1/4)
# print(x+y+z)