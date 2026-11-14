class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for n in nums: 
            freq[n] += 1

        sort_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        res = list(sort_freq)[:k]

        return res
