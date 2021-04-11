# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0  # nums의 인덱스용
        for i in range(len(nums)):
            if nums[idx] == val:  # 같을 경우 nums에서 삭제 후 idx를 그대로
                del (nums[idx])
            else:
                idx += 1

        return len(nums)


# Test
solution = Solution()
print(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
