"""
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。
"""

class String(object):

    def theSome(self,s1,s2):
        if len(s1) == len(s2) and sorted(s1) == sorted(s2):
            print("true")
        else:
            print("false")


s = String()

s1 = 'adsdf'
s2 = 'saddf'

s.theSome(s1,s2)