from collections import defaultdict
from typing import List 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        oc = defaultdict(int)

        for n in nums:
            oc[n] += 1

        return max(oc, key=oc.get)