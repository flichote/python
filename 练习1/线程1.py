# index = 11
# cv =1
# for i in range(1,5):
#     cv = index * cv
#     index = index -1
#
# print(cv)

# namelist = [ 'a','b','c']
#
# for i in range(0,len(namelist)):
#     if namelist[i] == 'b':
#         continue
#     print(namelist)



# sum = 0
# for i in range(0,31):
#     i = i + 1
#     sum = sum + i
#     print(i,sum)
#
# print(sum)


sum = 0
i = 1
while i < 31:
    if i % 10 ==0:
        i  = i *2
    sum = sum +1
    i = i +1

print(sum)