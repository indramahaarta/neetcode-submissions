class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for i in nums:
            if i in numsSet:
                return True
            
            numsSet.add(i)
        
        return False
        