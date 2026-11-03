class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        r = len(s1)

        count1 = dict()
        count2 = dict()
    

        for i in s1:
            count1[i] = 1 + count1.get(i,0)

        
        while(l < r):
            count2[s2[l]] = 1 + count2.get(s2[l],0)
            l += 1
        if count1 == count2:
            return True
        l = 0
        
        while(r < len(s2)):
            count2[s2[l]] = count2.get(s2[l],0) - 1
            if count2[s2[l]] == 0:
                del count2[s2[l]]
            count2[s2[r]] = count2.get(s2[r],0) + 1
            if count1 == count2:
                return True
            l += 1
            r += 1
        return False
                

            