class Solution:
    def twoSum(self, nums, target: int):
        visited={}
        for index,value in enumerate(nums):
            remaining=target-value
            if remaining in visited:
                return [visited[remaining],index]
            visited[value]=index