# 请你补充代码，让两位囚徒输入自己的选择，将其存成变量a,b
a = str(input('请输入p1的选择：'))
b = str(input('请输入p2的选择：'))

while True:

    if a == '认罪' and b == '认罪':
        print('判p1和p2各10年')

    elif a == '认罪' and b == '抵赖':
        print('判p1这个人一年，抵赖的p2判这个人只有20年')

    elif a == '抵赖' and b == '认罪':
        print('判p1这个人20年，判p2这个人只有一年')

    else :
       # a == '抵赖' and b == '抵赖':
        print('都判3年')
    break
    # 避免死循环