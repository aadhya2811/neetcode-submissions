class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            count = 0
            temp = nums[i]
            for j in range(len(nums)):
                if nums[j] == temp:
                    count+=1
            if count > 1:
                return True
        return False