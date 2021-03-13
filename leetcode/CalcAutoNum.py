"""
https://www.nowcoder.com/practice/88ddd31618f04514ae3a689e83f3ab8e?tpId=37&tqId=21322&rp=1&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking&tab=answerKey
自守数
"""

def CalcAutomorphicNumbers(x):
    """判断自守数的个数"""
    a = 0
    for i in range(1,x+1):
        imod = i % 10
        if imod == 0 or imod == 1 or imod ==5 or imod == 6:
            j = i**2
            if str(i) in str(j)[-len(str(i)):]:
                a += 1
    return a+1

if __name__ == '__main__':
    """
        while (True):
        num = input()
        if num == 'n':
            break
        print(CalcAutomorphicNumbers(int(num)))

    """

    while True:
        try:
            n = int(input())
            num = 0
            for i in range(n+1):
                b = str(i ** 2)
                if b.endswith(str(i)):
                    print(i)
                    num += 1
            print(num)
        except:
            break
