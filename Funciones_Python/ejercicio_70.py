# 70. Subset sum (¿existe subconjunto con suma target?)
def subset_sum_exists(nums, target):
    if target == 0:
        return True
    if not nums:
        return False
    if nums[0] > target:
        return subset_sum_exists(nums[1:], target)
    return subset_sum_exists(nums[1:], target - nums[0]) or subset_sum_exists(nums[1:], target)