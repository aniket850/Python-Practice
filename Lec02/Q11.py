# print all the factors of a number
# 12-> 1,2,3,4,6,12
a=int(input("enter a number"))
for i in range (1,a+1):
    if a%i==0:
        print(i,end =" ") #empty space after all number


