"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""

def fn(a):
    list = []
    relist = []
    str1 = str(a)
    for i in str1:
        list.append(i)
    print(list,'list')
    list.reverse()
    print(list)
    for i in list:
        relist.append(i)
    relist.reverse()
    print(relist,'relist',list,'list')

    if list == relist:
        return True
    if a <0:
        return False

fn(-12)

