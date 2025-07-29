# write a python script to merge python dictionaries
# Deep copy -> b=a -> b[0]=100 -> print (a)-> a's 1st index also updated to 100
# shallow copy-> b=a.copy()
a={1:10,2:20,3:30}
b={3:40,5:50,6:70}

# 1st way - (merged + add the values) for common dictionaries
for i in b.keys():
    if i in a.keys():
        a[i]=a[i]+b[i]
    else:
        a[i]=b[i]
print(a)


# 2nd way- (Update only)
# for i in b:
#     a[i]=b[i]
# print(a)  #print the merged dictionary


# 3rd way- (Update only)
# a.update(b) # update the a and put the b values into a
# print(a)
