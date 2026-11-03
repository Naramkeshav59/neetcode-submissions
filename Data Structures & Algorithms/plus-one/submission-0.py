class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = [0]*(len(digits)+1)
        result[-1] = 1
        for i in range(len(digits)):
            tot = result[- i - 1] + digits[-i - 1]
            result[- i - 1] = (tot)%10
            result[- i - 2] += (tot)//10
    
        return result[1:] if result[0] == 0 else result


