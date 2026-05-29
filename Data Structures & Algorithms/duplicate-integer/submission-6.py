from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_count = Counter(nums)
        print(nums_count)
        for v in nums_count.values():
            if v > 1:
                return True
        return False
        