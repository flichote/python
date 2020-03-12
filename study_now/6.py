
"""
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。
"""
string = 'aassddty'

conter = 0

list = []
def backstring(string):
    for i in string:
        if i not in list:#如果里面没有该字母，则添加到里面
            list.append(i)

        else:#如果在里面就移除该字母
            list.remove(i)
    if len(list) >1:
        print('False')
    else:
        print('True')

backstring(string)



#一下方法要考虑的要素太多了，不适合

# def fn(string):
#     if len(string) == 2*len(set(string)) or len(string) <= (2*len(set(string))) or len(string)/2 > len(set(string)):
#         print('Turn')
#     else:
#         print('False')
#
# fn(string)
# print(len(string),2*len(set(string)))
# print(len(set(string)))