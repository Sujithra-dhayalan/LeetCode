class Solution:
    def sumBase(self, n: int, k: int) -> int:
        base_k=0
        sum1=0
        while(n!=0):
            digit=n%k
            base_k=base_k*10+digit
            n=n//k
        num=(base_k)
        while(num!=0):
            rem=num%10
            sum1+=rem
            num=num//10
        return sum1
        