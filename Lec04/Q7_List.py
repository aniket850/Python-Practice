# list sorted or not
a=[12,13,17,19]
for i in range(len(a)-1):
    if (a[i]<a[i+1]):
        continue
    else:
        print("list is not sorted")
        break
else:
				print("sorted list")
