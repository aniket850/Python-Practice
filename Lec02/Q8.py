# Take a number and print its table -> 5*1=5    , 5*2=10
a=int(input("enter a number"))
# by this you are getting onky value but we have to print 5*1=5 this type

# for i in range(a,(a*10)+1,a):
#     print(i) 
for i in range(1,11): #1-10 er range setup in i
    print(f"{a}*{i}={a*i}")
    