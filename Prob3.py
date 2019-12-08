import numpy as n
import ast

print('Enter the points below:')
print('Program is limited to 10th Degree only')
print("Press Enter when there is no value to skip")

X1 = input("Input the Value of X1: ")
Y1 = input("Input the Value of Y1: ")
X2 = input("Input the Value of Y2: ")
Y2 = input("Input the Value of X2: ")
X3 = input("Input the Value of X3: ")
Y3 = input("Input the Value of Y3: ")
X4 = input("Input the Value of X4: ")
Y4 = input("Input the Value of Y4: ")
X5 = input("Input the Value of X5: ")
Y5 = input("Input the Value of Y5: ")
X6 = input("Input the Value of X6: ")
Y6 = input("Input the Value of Y6: ")
X7 = input("Input the Value of X7: ")
Y7 = input("Input the Value of Y7: ")
X8 = input("Input the Value of X8: ")
Y8 = input("Input the Value of Y8: ")
X9 = input("Input the Value of X9: ")
Y9 = input("Input the Value of Y9: ")
X10 = input("Input the Value of X10: ")
Y10 = input("Input the Value of Y10: ")

array = n.array([(X1, Y1), (X2, Y2), (X3, Y3), (X4, Y4), (X5, Y5),
                (X6, Y6), (X7, Y7), (X8, Y8), (X9, Y9), (X10, X10)])

length = len(array)
x = array[0:length, 0]
y = array[0:length, 1]

polyfitArray = []
polyvalArray = []
errornorm = []
leastnormerrorArray = []

def poly():
    for n in range (1, length):
        if n <=10:
            polyfitvalue = n.polyfit(x, y, n)
            n.concatenate(polyfitArray, polyfitvalue)
            
            polyvalvalue = n.polyval(polyfitvalue, x)
            n.concatenate(polyvalArray, polyvalvalue)

            norm= n.linalg.norm(y-polyvalvalue)
            n.concantenate(errornorm, norm)
            
            leastNormError = n.min(norm)
            n.concantenate(leastnormerrorArray,leastNormError)
            
            print('Coefficients of the Polynomial:', polyvalArray)
            print('Least Norm Error: ',leastnormerrorArray)     
            return