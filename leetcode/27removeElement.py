def removeElement(self, nums, val):
    n = len(nums)
    j = 0
    for i in range(n):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j


if __name__ == '__main__':
    x = range(0, 5)
    y = range(5)
    print(x)
    print(y)