"""
URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，
并且知道字符串的“真实”长度。（注：用Java实现的话，请使用字符数组实现，以便直接在数组上操作。）
"""

astr = 'asdf   d'
list =[]
# print(len(astr))
for i in astr:
    if i == ' ':

        i = '20%'
    list.append(i)
    print(i)



print(list)

print(str(list))


class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        alist = []
        for i in str:
            if i == ' ':
                i = '20%'
            alist.append(i)
        print(alist)

S = 'asdf'

s = Solution(S,5)

s.replaceSpaces

return S[:length].replace(" ", "%20")
