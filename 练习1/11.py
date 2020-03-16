# def gen_next(s2):
#     k = -1
#     n = len(s2)
#     j = 0
#     next_list = [0 for i in range(n)]
#     next_list[0] = -1                           #next数组初始值为-1
#     while j < n-1:
#         if k == -1 or s2[k] == s2[j]:
#             k += 1
#             j += 1
#             next_list[j] = k                    #如果相等 则next[j+1] = k
#         else:
#             k = next_list[k]                    #如果不等，则将next[k]的值给k
#     return next_list
#
#
# def match(s1, s2, next_list):
#     ans = -1
#     i = 0
#     j = 0
#     while i < len(s1):
#         if s1[i] == s2[j] or j == -1:
#             i += 1
#             j += 1
#         else:
#             j = next_list[j]
#         if j == len(s2):
#             ans = i - len(s2)
#             break
#     return ans
#
#
# if __name__ == '__main__':
#     s1 = 'ababaabbababababc'
#     s2 = 'ababc'
#     next_list = gen_next(s2)
#     print(next_list)
#     print(match(s1, s2, next_list))

class KMP:
    def __init__(self,T:str):
        self.T ,self.n = T,len(T)
        self.next = [0] * (self.n+1)
        self.next[0],j = -1,-1

        for i in range(self.n):
            while j >=0 and T[i] != T[j]: j = self.next[j]
            j+=1
            self.next[i+1] = j

    def match(self,S:str):
        m,j,res = len(S),0,[]

        for i in range(m):
            while j > 0 and S[i] != self.T[i]: j = self.next[j]
            if S[i] == self.T[j]: j+=1
            if j == self.n:
                res.append(i-self.n +1)
                j = self.next[j]
        return res

kmp = KMP('asd')
kmp.match('assddssasd')


