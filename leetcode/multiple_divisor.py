"""求两个数的最小公倍数和最大公约数"""
def max_com_divisor(a,b):
    """求两个数的最大公约数"""
    while(1):
        if a>b:
            a -= b
        elif a<b:
            b -= a
        else:
            return a


def min_com_multiple(a,b,c):
    """求两个数的最小公倍数"""
    x = a / c
    return  b * x


if __name__ == '__main__':
    """主函数"""
    a = 24
    b = 26
    c = max_com_divisor(a,b)
    print(min_com_multiple(a,b,c))