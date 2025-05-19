# Prime or Not -> a number has only 2 factor 1  and the number itself

n=int(input("enter the number "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print("prime number")
else:
    print("composite number")


