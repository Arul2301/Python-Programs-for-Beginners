#1 Method
#finding the MAX value using if_else statement in python

def maximum(a,b):
    if a>=b:
        return a
    else:
        return b
a=int(input())
b=int(input())
print("The Max value is:")
print(maximum(a,b))

# 2 Method
#finding the MAX value using the max function

a=int(input())
b=int(input())
print("The MAX value of a & b using the MAX function is :")
print(max(a,b))

# 3 Method
#finding the MAX value using the TERNARY OPERATOR

a=int(input())
b=int(input())
print("The MAX value of a & b using the TERNARY OPERATOR is :")
print(a if a>=b else b)