def first_missing_positive(nums):
    n = len(nums)
    # Place each number in its correct position if possible
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            correct_pos = nums[i] - 1
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    # If all positions are correct, the missing number is n + 1
    return n + 1
nums = [1, 2, 0]
print(first_missing_positive(nums))  
