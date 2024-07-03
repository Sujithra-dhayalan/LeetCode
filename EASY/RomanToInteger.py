class Solution:
    def romanToInt(self, s: str) -> int:
        sum=0
        romans={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        while(i<len(s)):
        
            if s[i] in romans:
                if i+1<len(s) and romans[s[i]]<romans[s[i+1]]:
                    diff=romans[s[i+1]]-romans[s[i]]
                    sum+=diff
                    i+=2
                    
                else:
                    sum+=romans[s[i]] 
                    i+=1
        return sum