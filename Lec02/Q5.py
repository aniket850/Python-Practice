# Accept a year and check if it is a leap year or not
year=int(input("enter the year"))
if year%4==0 and year%100 !=0:
    print("leap year")
elif year%100==0 and year %400 ==0:
    print("leap year")
else:
    print("not a leap year")