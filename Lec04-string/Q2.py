# Arrange string characters such that lowercase letters should come first in another string
# check each elecmet == lower case conactinate to emtpy string b='' 
# Reminder ->   split a str into list ->    a=" Hi Aniket" -> next line -> b=a.split() -> print(b)
a="Aniket How Are You"
b=''
for i in a:
    if i.islower():
        b=b+i
for i in a:
    if i.isupper():
        b=b+i
print(b)
