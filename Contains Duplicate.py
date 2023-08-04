class Solution(object):
    def containsDuplicate(self, nums):
        n=set()
        for i in range(len(nums)):
            if nums[i] in n:  
                return True
            n.add(nums[i])
        return False
            
or 



from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        if(len(s)==len(t)):
            res = Counter(s)
            res1=Counter(t)
            if(res==res1):
                return True
        return False
