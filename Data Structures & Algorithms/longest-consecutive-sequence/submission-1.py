class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nume=set(nums)
        longest=0
        for i in nume:
            if (i-1) not in nume:
                length=1
                while(i+length) in nume:
                    length+=1
                longest=max(longest,length)
        return longest