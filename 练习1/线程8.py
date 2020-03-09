# for i in range(1,1001):
#     j = str(i)
#     index = j.find('3',0)
#     if index == -1 and i % 3 ==0:
#         print(i)
#     # if i % 3 == 0:
#     #     if i !=3:
#     #         print(i)

#
# i = 1
# while i:
#     if i % 3 ==0:
#         j = str(i)
#         index = 0
#         for k in j:
#             if k =='3':
#                 index +=1
#         if index ==0:
#             print(i)
#     i +=1
#     if i == 1001:
#         i =0
#
# i = 1
# while i < 1001:
#     if i %3 ==0:
#         j = str(i)
#         for k in j:
#             if k =='3':
#                 break
#         print(i)
#     i +=1

c  = 11
cv =1
i = 4
while i:
    cv = c *cv
    c = c -1
    i = i -1

print(cv)








