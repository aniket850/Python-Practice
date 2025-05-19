# count all leter, digits and special symbols in a given string ->" P@#n26at^&i5ve "
# reminder -> convert a letter to its ascii value ->  print(ord("b"))
# reminder -> convert a ascii value to char -> print(chr(65))

str="P@#yn26at^&i5ve" # if you use " P@#yn26at^&i5ve " -> space also count in special char
char=0
digits=0
special_char=0
for i in str:
    if i.isalpha(): #method to check char or not
        char=char+1
    elif i.isdigit(): #method to check digit or not
        digits=digits+1
    else:
        special_char =special_char+1
print(f"char={char}")
print(f"digits={digits}")
print(f"special_char={special_char}")

