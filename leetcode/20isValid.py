"""
有效的括号
https://leetcode-cn.com/problems/valid-parentheses/
"""
def isValid(s):
    """
    判断字符串括号是否有效
    """
    list1 = list(s)
    str1 = [')','}',']']
    str2 = {')':'(','}':'{',']':'['}
    if s[0] in str1 or len(s) % 2 != 0:
        return False
    for i in range(1,len(s)):
        if list1[i] in str1:
            if list1[i-1] == str2[list1[i]]:
                if len(s) == 2:
                    return True
                del list1[i]
                del list1[i-1]
                str3 = "".join(list1)
                return isValid(str3)
            else:
                return False
    return False


if __name__ == '__main__':
    s = '(('
    print(isValid(s))
