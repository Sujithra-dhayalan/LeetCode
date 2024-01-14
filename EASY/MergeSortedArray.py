class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        k=len(nums1)-1
        while k>=m:
            if nums1[k]==0:
                nums1.pop(k)
            k-=1

        x=nums1.copy()
        print(x)
        nums1.clear()
        while i<len(x) and j<len(nums2):
            if (x[i]<nums2[j]):
                nums1.append(x[i])
                i+=1
            else:
                nums1.append(nums2[j])
                j+=1
        nums1+=x[i:]
        nums1+=nums2[j:]
       