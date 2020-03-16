
"""
金典排序之快速排序法
"""
def quick_sort(alist,start,end):
    #递归的退出条件
    if start >= end:
        return

    #假设其实元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右的游标
    low = start

    #high 为序列右边的由右向左移动的游标
    high = end

    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1

        alist[low] = alist[high]

        while low < high and alist[low] < mid:
            low +=1

        alist[high] = alist[low]

    alist[low] = mid

    quick_sort(alist,start,low -1)
    quick_sort(alist,low +1,end)

li = [32,23,22,33,34,45,65,39]
quick_sort(li,0,len(li) -1)
print(li)



