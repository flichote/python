

# s = "abcd"
# p = "dddabce"

star = ["*"]
star = star[0]
point =['.']
point = point[0]
s = "abcd"
p = "ddabcddd"
lists = list(s)
listp = list(p)
lst = []
for i in range(len(s)):
    for j in range(len(p)):
        if point not in listp and star not in listp:
            if len(p) < len(s):
                print(False)
                break

            if lists[i] == listp[j] and i == j:
                lst.append(lists[i])
                break
            if lists[i] == listp[j] and i != j:
                del listp[:j]  # listp.remove(listp[:j])
                lst.append(lists[i])
                listp.insert(j,j)
                break
            if lists[i] == listp[j] and i == j:
                lst.append(lists[i])
                break
        if point in listp or star in listp:
            if lists[i] == listp[j] and i == j:
                lst.append(lists[i])
                break
            if lists[i] == listp[j] and i != j:
                del listp[:j]  # listp.remove(listp[:j])
                lst.append(lists[i])
                print('listp',listp)
                break
            if listp[j] == point:
                lst.append(lists[i])
                print(lst,"~~~~~~~~~~~~~~~~")
                print('j',j,'i',i)
                break
            if listp == star:
                lst.append(listp[-1])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(lst,"lst")
print(lists,"lists")
print(listp,"listp")


