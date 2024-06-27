
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m
            else:
                return m
            
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([2, 687, 980, 1111], 1111)) # 3