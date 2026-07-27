class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for ch in s:
            count[ch] = count.get(ch,0)+1              # increment; careful — first time you see
                                           # a char it's not in the dict yet
        for ch in t:
            if ch not in count or count[ch]==0:                 # the two failure conditions
                return False
            count[ch] -= 1
        
        return True