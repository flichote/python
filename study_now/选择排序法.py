"""
金典排序之选择排序法

"""

def selection_sort(alist):
    n = len(alist)
    #需要进行n-1次选择操作
    for i in range(n-1):
        #记录最小位置
        min_index = i
        # 从i+1位置到末尾选择出最小数据
        for j in range(i+1,n):
            if alist[j] < alist[min_index]:
                min_index = j
        #如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index],alist[i]

li = [32,23,43,54,44,55,65,77]
selection_sort(li)
print(li)

