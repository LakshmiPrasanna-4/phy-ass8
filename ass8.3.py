# Write a program to print the biggest of three numbers.

a,b,c=map(int,input().split())
if(a>b and a>c):
    print("a is big")
elif(b>c):
    print("b is big")
else:
    print("c is big")
