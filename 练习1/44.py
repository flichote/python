alist = ["flower","flo","foth"]

list = []

for i,j in enumerate(alist):
    for m in range(len(j)):
        if j[m] == j[i] and i ==m:
            list.append(j[m])

print(list)



