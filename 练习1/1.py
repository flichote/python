
a = [2,4,7,4]
b = [3,3,5,2]
c = []
a.reverse()
b.reverse()
print('a',a)
print('b',b)
if a[1] + b[1] >=10:
    flag = 0
else:
    flag = 1
for x,v in enumerate(a):
    for y,z in enumerate(b):



            if v+z >=10 and x == y:
                print('x',x,'y',y,"~~~~~~~~~~~")
                c.append(v+z-10)
                c.append(a[x+1]+b[y+1] +1)
        if flag ==1:
                # c.remove(c[x+1])
            if x == y and v+z < 10:
                print('x',x,'y',y,'_______')
                # c.pop()
                c.append(v+z)




print(c)






