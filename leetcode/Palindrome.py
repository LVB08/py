"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
链接：https://leetcode-cn.com/problems/palindrome-number
"""
def isPalindrome(x):
    str_x = str_y = ''
    str_x = str(x)
    for y in reversed(str_x):
        str_y = str_y + y
    if str_x == str_y:
        return True
    return False


if __name__ == '__main__':
    print(isPalindrome(-1221))
