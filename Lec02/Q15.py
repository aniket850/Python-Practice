# palindrom or not
n=int(input("Enter A Number "))
m=n
rev=0
while n>0:
    l_digit=n%10
    rev=rev*10+l_digit
    n=n//10
if m==rev:
    print(f"{m} is a palindrom")
else:
    print("Not a Palindrom")
