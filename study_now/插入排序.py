"""
金典排序之插入排查
"""

def insert_sort(alist):
    #从第二个位置，即下标为1的元素开始向前插入
    for i in range(1,len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i,0,-1):
            if alist[j] <alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]


li = [32,23,22,33,34,45,65,39]
insert_sort(li)
print(li)
