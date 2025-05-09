#task1
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))
inp=int(input('Enter a number: '))
result=factorial(inp)
print('Factorial of',inp,'is:',result)


#task2:
import math

num = float(input("Enter a number: "))

square_root = math.sqrt(num)
logarithm = math.log(num)
sine = math.sin(num)

print("Square root:", square_root)
print("Logarithm:", logarithm)
print("Sine:", sine)
