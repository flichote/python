l1=[1,2,3,5]
l2=[5,6,4]

list3=[]

number1 = 0
number2 = 0
number3 = 0
length1 = len(l1)
length2 = len(l2)
for i in range(length1):
        number1 += l1[i]*10**(length1-i-1)
print(number1)

for j in range(length2):
    number2 += l2[j]*10**(length2-j-1)
print(number2)
number3 = number2 + number1

a=str(number3)
for i in a:
    list3.append(i)

print('number1',number1,'number2',number2)
print(list3)

