# Accept the gender from the user as char and print the msg- "Good Morning Sir/mam"
gender=input()

if gender == "m" or gender == "M":
    print("Good Morning Sir")
elif gender == "f" or gender == "F":
    print("Good Morning Mam")
else:
    print("Wrong Input")