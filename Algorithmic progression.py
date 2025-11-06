"""    This algorithm finds the missing number
         in an arithmetic progression using
 the formula for the sum of an arithmetic progression     """

def find_missing_number(nums: list[int]) -> int:
    # formula - S = n/2 × (a₁ + aₙ)

    n = len(nums) + 1
    a1 = nums[0]
    an = nums[-1]

    S = (n / 2) * (a1 + an)

    actual_sum = sum(nums)

    return int(S - actual_sum)

print(find_missing_number([0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11]))