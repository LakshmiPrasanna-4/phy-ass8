#Write a  program to print given number number is a palindrome number or not

n=int(input('Enter a number:'))
temp=n
res=0
while n!=0:
    r=n%10
    n=n//10
    res=res*10+r
print(res)
if(temp==res):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
