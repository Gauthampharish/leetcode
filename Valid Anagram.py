class Solution(object):
    def isAnagram(self, s, t):
        if(len(s)==len(t)):
            for i in set(s):
                if s.count(i)!=t.count(i):
                        return False
            
            return True
        return False


        
