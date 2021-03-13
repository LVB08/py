"""
整数反转
给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
"""

def reverse(x):
    arr = []
    negative = False
    if x > -10 and x < 10:
        return x
    if x < 0:
        x = 0 - x
        negative = True
    while (1):
        if x == 0:
            break
        arr.append(x%10)
        x = int(x / 10)
    m = 1
    n = 0
    for num in reversed(arr):
        n = n + m * num
        m = m * 10
    if negative:
        n = 0 - n
    if n < -2**31 or n > (2**31)-1:
        return 0
    return n

if __name__ == '__main__':
    print(reverse(1235))

"""
    print(1234 % 10)  # 求个位数
    print(int(1234/10) % 10)  # 求十位数
    print(int(1234/100) % 10)  # 求百位数
    print(int(10234/1000) % 10)  # 求千位数
    print(int(10234 /10000) % 10)  # 求万位数
    print(int(10234 / 100000) % 10)  # 求十万位数
"""

