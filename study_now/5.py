
"""
URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，
并且知道字符串的“真实”长度。

"""


S = 'asdf  fd ' #9
length = 17
def rr(S,int):
    if len(S) == length:

      print(S[:length].replace(" ", "20%"))
    if len(S) != length:
        #print(S[:length].replace(" ", "20%"))
      print(S[:length].replace(" ", "20%") + "20%"*(length - len(S)))


rr(S,7)
print('~~~~~~~~~~~~~')
print(S)


def replaceSpaces(self, S: str, length: int) -> str:
    arr = list(S)
    for i in range(length):
        if arr[i] == " ":
            arr[i] = "%20"
    return "".join(arr[:length])