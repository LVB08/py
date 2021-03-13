"""
最长公共前缀
https://leetcode-cn.com/problems/longest-common-prefix/
"""
def longestCommonPrefix(strs):
    """
    查找字符串数组中的最长公共前缀
    """
    str_Pre = ''
    if not strs:
        return ''
    for j in range(0,len(strs[0])):
        for i in range(1, len(strs)):
            if j > len(strs[i]) or j == len(strs[i]):
                return str_Pre
            if strs[i][j] != strs[0][j]:
                return str_Pre
        str_Pre = str_Pre + strs[0][j]
    return str_Pre
if __name__ == '__main__':
    strs = ["flower","flowet","flow"]
    print(longestCommonPrefix(strs))