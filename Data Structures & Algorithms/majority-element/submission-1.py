from collections import defaultdict
from typing import List 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer-moore

        candadite = None
        count = 0

        for n in nums:
            if count == 0:
                candadite = n
            if n == candadite:
                count += 1
            else:
                count -= 1
            
        return candadite
