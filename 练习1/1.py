"""冒泡排序法"""

# def bubble_sort(alist):
#     for i in range(len(alist)-1,0,-1):
#         for j in range(i):
#             if alist[j] > alist[j+1]:
#                 alist[j],alist[j+1] = alist[j+1],alist[j]
#
#
# alist = [1,2,44,55,34,32]
# bubble_sort(alist)
# print(alist)
#
# """选择排序法"""
# def select_sort(alist):
#     n = len(alist)
#     for i in range(n-1):
#         min_index = i
#         for j in range(i+1,n):
#             if alist[j] > alist[min_index]:
#                 min_index = j
#         if min_index != i:
#             alist[i],alist[min_index] = alist[min_index],alist[i]
#
# alist = [1,2,3,34,54,33,23,21]
# select_sort(alist)
# print(alist)
#
# """快速排序"""
#
#
#
# def insert_sort(alist):
#     for i in range(1,len(alist)):
#         for j in range(i,0,-1):
#             if alist[j] < alist[j-1]:
#                 alist[j],alist[j-1] = alist[j-1],alist[j]
#
# alist = [1,2,3,34,54,33,23,21]
# insert_sort(alist)
# print(alist)

"""
归并排序"""

# def merge_sort(alist):
#     length = len(alist)
#     if length <=1:
#         return alist
#     mid = int(length / 2)
#
#     left_alist = merge_sort(alist[:mid])
#     right_alist = merge_sort(alist[mid:])
#
#     left_point ,right_point = 0,0
#     result = []
#
#     while left_point < len(left_alist) and right_point < len(right_alist):
#         if left_alist[left_point] < right_alist[right_point]:
#             result.append(left_alist[left_point])
#             left_point+=1
#         else:
#             result.append(right_alist[right_point])
#             right_point+=1
#     # result += left_alist[left_point:]
#     # result += right_alist[right_point:]
#     return result
#
#
# alist = [2,1,6,3]
# merge_sort(alist)
# print(alist)


# def merge_sort(alist):
#     if len(alist) <= 1:
#         return alist
#     # 二分分解
#     num = int(len(alist)/2)
#     left = merge_sort(alist[:num])
#     right = merge_sort(alist[num:])
#     # 合并
#     return merge(left,right)
#
# def merge(left, right):
#     '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
#     #left与right的下标指针
#     l, r = 0, 0
#     result = []
#     while l<len(left) and r<len(right):
#         if left[l] < right[r]:
#             result.append(left[l])
#             l += 1
#         else:
#             result.append(right[r])
#             r += 1
#     result += left[l:]
#     result += right[r:]
#     return result
#
# alist = [54,26,93,17,77,31,44,55,20]
# # sorted_alist = merge_sort(alist)
# print(merge_sort(alist))
#
# # print(sorted_alist)
#

"""
希尔排序"""

def shell_sort(alist):
    n = len(alist)
    gap = int(n/2)
    while gap > 0:
        for i in range(gap,n):
            j = i
            while j >=gap and alist[j-gap] > alist[j]:
                alist[j-gap],alist[j] = alist[j],alist[j-gap]
                j -= gap
        gap = int(gap/2


alist = [54,25,43,23,11,55,75,22]
shell_sort(alist)
print(alist)









