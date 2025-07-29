# Count Vowels from given string
# create a fn 
def vowel_consonant(x):
    count=0
    consonant=0
    for i in x:
    # if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        if i in "aeiouAEIOU":
            count=count+1
        elif i==" ": #space thakle seta bad diye nect take check
            continue
        else:
            consonant=consonant+1

    return f"vowel {count} and consonant {consonant}"

a="hi aniket how are you"

print(vowel_consonant(a))

