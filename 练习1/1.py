List = [3,3,4]
target = 6
dict = {}
for i in range(len(List)):
    for j in range(i+1,len(List)):
        if target - List[j] == List[i]:
            print([i,j])

