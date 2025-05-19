# perfect number or not -> a number whose sum of factors (excluding number itself) =number
# ex-> 6=1,2,3=6 (1+2+3=6)
n=int(input("Enter the number "))
sum=0
for i in range(1,n):
    
    if n%i==0:
        sum=sum+i
if n==sum:
    print(f"{n} is a Perfect Number")
else:
    print("Not a valid Perfect Number")