class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            tot=numbers[l]+numbers[r]
            if tot<target:
                l+=1
            if tot>target:
                r-=1
            if tot==target:
                return [l+1,r+1]
                
            

            