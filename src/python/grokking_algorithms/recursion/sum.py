def sum_values(nums):
    if not nums:
        return 0
    return nums[0] + sum_values(nums[1:])


