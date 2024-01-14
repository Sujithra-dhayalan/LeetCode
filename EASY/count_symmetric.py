class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
       
        for i in range(low,high+1):
            sum1=0
            sum2=0
            num_str=str(i)
            length=len(num_str)
            if length%2==0:
                half=length//2
                num1=int(num_str[:half])
                num2=int(num_str[half:])
                while(num1>0):
                    y=num1%10
                    sum1+=y
                    num1=num1//10
                while(num2>0):
                    y=num2%10
                    sum2+=y
                    num2=num2//10
                if (sum1==sum2):
                    count+=1
        return count


        