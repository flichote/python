"""
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
"""

class Solution(object):
    def isUnique(self,astr):
        """
        :type astr:str
        :rtype: bool
        :param astr:
        :return:
        """
        for i in range(0,(len(astr)-1)):
            if astr[i] in astr[i+1]:
                # break
                print("false")
            print('true')
            break

astr = 'aabv'
s = Solution()
s.isUnique(astr)

