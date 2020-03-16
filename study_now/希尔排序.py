"""
金典排序之希尔排序
"""
def shell_sort(alist):
    n = len(alist)

    gap = int(n /2)

    while gap > 0:
        for i in range(gap,n):
            j = i
            while j>=gap and alist[j-gap] > alist[j]:
                alist[j-gap],alist[j] = alist[j],alist[j-gap]
                j-=gap

        gap = int(gap/2)


li = [32,23,22,33,34,45,65,39]
shell_sort(li)
print(li)