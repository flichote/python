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
        if len(astr) == len(set(astr)):
            print("true")
        else:
            print("false")

astr = 'asdf'
s = Solution()
s.isUnique(astr)
