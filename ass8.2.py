# Write a program to print given number is a Armstrong number or not.

n=int(input('Enter a number:'))
temp=n
res=0
while n!=0:
    r=n%10
    n=n//10
    res=res+r*r*r
print(res)
if(temp==res):
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")


