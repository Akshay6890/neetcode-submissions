from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element
        count = Counter(nums)
        
        # Sort the elements by frequency and return the top k
        return sorted(count, key=count.get, reverse=True)[:k]