class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        fin = False
        cnt = 0
        while not fin:
            try:
                nums.remove(val)
                cnt += 1
            except ValueError:
                fin = True
        
        return len(nums)

