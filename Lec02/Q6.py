# accept an english alphabet from user and check if it is a consonant or a vowel
alphabet = input("enter a alphabet ")
# if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u':

if alphabet in "aeiouAEIOU": #operations in str
    print("vowel")
else:
    print("consonant")

