class Solution:
    def reverse(self, x: int) -> int:
        int_min=-2**31
        int_max=2**31-1
        result=0
        sign= 1 if x>0 else -1
        x=abs(x)
        while(x>0):
            digit=x%10
            x=x//10
            if (result>(int_max-digit)//10):
                return 0
            result=result*10+digit
        return result*sign

            
        