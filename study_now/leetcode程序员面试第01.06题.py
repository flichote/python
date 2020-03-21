S  = "aabcccccaaa"

#如果给的字符串是空的，则直接返回
if S == "":
    print(S)
#定义一个字符串，将首字母和给定的字符串首字母设为一样的
string = S[0]
print(string)

count = 0
for i,j in enumerate(S):
    #因为在定义的时候就设为何给定的字符串首字母相同，所有一进来就是相同的，直接给计数器加1
    if string[-1] == j :
        count +=1
    else:
        #如果给定字符串中的某一个开始不相同了，则将最后一次的计数器数字拼接到字符串中。
        string = string+str(count)
        #出现和前一个字符不相同，则直接和字符串拼接，并将其个数记为1
        string = string+j
        count = 1
string = string+str(count)
print(string)
if len(string) > len(S):
    print(S)
else:
    print(string)





