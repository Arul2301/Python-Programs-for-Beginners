#1 Method
# Finding the MAX value of A, B, C using if_else statement
def maximum(a,b,c):
    if (a>=b) & (a>=c):
        return a
    elif (b>=a) & (b>=c):
        return b
    else:
        return c

a=int(input())
b=int(input())
c=int(input())
print("Finding the MAX value of A, B, C using if_else statement is:")
print(maximum(a,b,c))
print("\n")

#2 Method
#Finding the MAX value of A, B, C using the MAX() 

a=int(input())
b=int(input())
c=int(input())
print(" Finding the MAX value of A, B, C using the MAX() is :")
Result=max(a,b,c)
print(Result)
print("\n")

#3 Method
#Finding the Max value of A,B, C using List

def maximum(a,b,c):
    list=[a,b,c]
    return max(list)
a=int(input())
b=int(input())
c=int(input())
print(" Finding the Max value of A,B, C using List is :")
print(maximum(a,b,c))