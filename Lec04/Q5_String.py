# check string pallindrome or not
a="naman"
b=""
# print(a==a[::-1]) #if true plaindrom
for i in range(len(a)-1,-1,-1):
    b=b+a[i]
if b==a:
    print("plaindrom")
else:
    print("not a plaindrom")
