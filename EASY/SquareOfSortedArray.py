class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        sq=[0]*n
        i=0
        j=0
        for i in nums:
            if(j<=n):
                sq[j]=i*i
                j+=1
        sq.sort()
        return sq

        