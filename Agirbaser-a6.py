
def factorial(n):
    #Base case
    if n == 0:
        return 1
    #Recursive case
    else:
        return n * factorial(n - 1)

#Set number to number you want to find the factorial of
number = 5
#apply factorial to the number and store it in result
result = factorial(number)
#print out the number you were taking the factorial of and the resulting factorial
print("The factorial of " + str(number) + " is: " + str(result))