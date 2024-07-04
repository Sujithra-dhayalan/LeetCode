class Solution:
    def removeElement(self, nums, val: int) -> int:
        c=nums.count(val)
        for i in range(c):
            nums.remove(val)
        return len(nums)
        