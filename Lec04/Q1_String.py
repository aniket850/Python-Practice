# string + Tuple + set + dictinary questions
# print string in reverse, its length, in uppercase,lowercasw abd copy into another string
# n=int(input())
a="aniket"
b=a
c=''
print(a.upper())
print(a.lower())
print(len(a))

# 1st way of reverse
for i in range(len(a)-1,-1,-1): # len(a)-1 = zero based indexing
    print(a[i], end=" ") #normal using indexing

# 2nd way of reverse
for i in range(len(a)-1,    -1,-1):
    c=c+a[i] # concatination -> works for string only if digit different
print(c)

# 3rd way of reversing
print(a[::-1])




