from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = len(nums) - 1
        while i > 0:
            if nums[i-1] == nums[i]:
                nums.pop(i)
            i-=1
        return len(nums)

print(Solution.removeDuplicates(Solution, [1, 1, 2]))