class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        sum=0
        while(x>0):
            y=x%10
            sum=sum*10+y
            x=x//10
    
    
        if (sum==temp):
            return 1
        else:
           return 0