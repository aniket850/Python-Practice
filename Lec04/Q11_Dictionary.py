# Count the number of items a element occur from a List uing Dictionary
# Concept -> dict[3]=10 -> dict={3:10}
# Concept -> dict={3:10} -> dict[3]=dict[3]+1 ->dict[3] = 10 + 1 → 11
# This means:-
# Start with dict = {3: 10}
# Then you're updating dict[3] by increasing its value by 1
# So: dict[3] = 10 + 1 → 11

a= [1,2,3,3,3,4,5]
dict={ }
for i in a:
    if i in dict.keys():
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)
