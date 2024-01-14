class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = []
        max_length=0
        for i in s:
            if i in string:
                string=string[string.index(i)+1:]
            string.append(i)
            max_length=max(max_length,len(string))

       
        return max_length
