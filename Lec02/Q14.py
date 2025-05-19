# seprate each digit of a number and print it on the new line 
n=int(input("Enter a number"))
m=n
while n>0:
    l_digit = n%10
    print(l_digit)
    n=n//10 # divide means not / here you have to use floor division //
