# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for i in range(len(nums) - 1):  # idx와 뒷원소와 비교하므로 len(nums)-1만큼 반복
            if nums[idx] == nums[idx + 1]:
                del (nums[idx])
            else:
                idx += 1

        return len(nums)


solution = Solution()
print(solution.removeDuplicates([1, 3, 4, 4]))
