# Sum of the all values in Dictionaries
a={1:10,2:20,3:30}
# 1st way ->
sum=0
for i in a.values():
    sum=sum+i
print(sum)

# 2nd way ->
# for i in a:
#     sum=sum+a[i]
# print(sum)