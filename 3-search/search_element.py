from typing import List

class Solution():
    def search(self, nums: List[str], target: str) -> bool:

        my_set = set(nums)

        if target in my_set:
            return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.search([2, "apple", 980, "orange"], "cherry"))  # False
    print(s.search([2, "apple", 980, "orange"], 980))  # True
    print(s.search([""], ""))  # True
    print(s.search([" "], ""))  # True
    print(s.search([2, "apple", 980, 2, "orange"], 2))  # True
            