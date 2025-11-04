""" This algorithm find next permutation, he uses pattern two pointers """

def nextPermutation(nums: list) -> list:
    i, j = len(nums) - 1, len(nums) - 1
    while i >= 0:
        if (i == len(nums) - 1) or (nums[i] >= nums[i + 1]):
            i -= 1
        else:
            while j >= 0:
                if nums[j] <= nums[i]:
                    j -= 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    left, right = i + 1, len(nums) - 1
                    while left < right:
                        nums[left], nums[right] = nums[right], nums[left]
                        left += 1
                        right -= 1
                    return nums
    else:
        nums.reverse()
        return nums


print(nextPermutation([1, 2, 3, 4]))