# Find the second largest number in a list
l=[11,12,13,15,14]
largest=l[0]
s_largest=l[0]
for i in l:
    if i>largest:
        s_largest=largest
        largest=i
    elif i>s_largest: # when last index is the 2nd largest 
        s_largest=i    # -> here 14 < largest so elif runs
print(s_largest,largest)
        
