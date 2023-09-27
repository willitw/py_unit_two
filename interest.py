#twig willaims
#interest.py
#9/27/23
#computing interest


# Assign values to variables
P = 10000  # principal amount
n = 12    # number of times interest is compounded per year
r = 0.08  # annual interest rate
t = 10    # number of years

# calculate the final amount
A = P * (1 + r/n)**(n*t)


print("The amount of compound interest is", A)
