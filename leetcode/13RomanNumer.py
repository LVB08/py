"""
罗马数字转整数
https://leetcode-cn.com/problems/roman-to-integer/
"""

def romanToInt(s):
    """
    罗马数字转整数
    """
    int_num = 0
    str_num = len(s)
    str1 = ''
    clogo = False
    for i in range(0,str_num):
        if clogo:
            clogo = False
            continue
        if i < str_num - 1:
            str_detect = s[i] + s[i+1]
            if esp_str(str_detect):
                int_num += esp_str(str_detect)
                clogo = True
                continue
            int_num += con_str(s[i])
        else:
            int_num += con_str(s[i])
    return int_num

def con_str(s):
    """
    检测常规字符
    ('I'(1), 'V'(5), 'X'(10), 'L'(50), 'C'(100), 'D'(500), 'M'(1000))
    """
    if s == 'I':
        return 1
    elif s == 'V':
        return 5
    elif s == 'X':
        return 10
    elif s == 'L':
        return 50
    elif s == 'C':
        return 100
    elif s == 'D':
        return 500
    elif s == 'M':
        return 1000

def esp_str(s):
    """
    检测特殊字符
    IV(4),IX(9),XL(40),XC(90),CD(400),CM(900)
    """
    if s == 'IV':
        return 4
    elif s == 'IX':
        return 9
    elif s == 'XL':
        return 40
    elif s == 'XC':
        return 90
    elif s == 'CD':
        return 400
    elif s == 'CM':
        return 900
    else:
        return False
if __name__ == '__main__':
    print(romanToInt('MCMXCIV'))