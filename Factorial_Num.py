# Program to print the factorial of a number

num1 = 7
fact = 1
if num1==1 or num1==0:
    print(f"Number should not be zero or 1")
else :
    for x in range(num1, 0, -1) :
        fact = fact * x
        print(f" number is {num1} and x is {x}")
    print(f"\n\nFactorial of {num1} is {fact}\n")
