x = -123
a = []
y = abs(x)
number1 = 0
str1 = str(y)
for i in str(y):

    a.insert(0, int(i))
    if a[-1] == 0:
        a.pop()

for i in range(len(a)):
    number1 += a[i]*10**(len(a)-i-1)
if x >=2147483647 or x <=-2147483648 or number1>=2147483647 or number1<=-2147483648:
    number1 = 0
if x < 0:
    number1 = number1 * (-1)
print(number1)
