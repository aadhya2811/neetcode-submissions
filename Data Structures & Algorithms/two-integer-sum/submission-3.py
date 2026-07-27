class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range (0,len(nums)):
            sol=target-nums[i];
            if sol in seen:
                    return [seen[sol],i]
            seen[nums[i]]=i
        