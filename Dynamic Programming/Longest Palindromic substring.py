# METHOD 1   time -> O(n^2)  space O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 1
        start = 0
        for i in range(len(s)):
            # handle even (abba) and odd (aba) length palindrome 
            start,maxLength = self.helper(s,i,i,start,maxLength)      # odd length palin
            
            start,maxLength = self.helper(s,i,i+1,start,maxLength)     # even length palin
            
        return s[start: start+maxLength]
            
    
    def helper(self,arr,start,end, beg,maxLength):
        while start>=0 and end<len(arr) and arr[start] == arr[end]:
            if end-start+1 > maxLength:
                maxLength = end-start+1
                beg = start
            start -= 1              # expand outwards
            end += 1
        return beg,maxLength
    
#2 METHOD 2 time -> space O(n)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result =''
        for i in range(len(s)):
            # handle even (abba) and odd (aba) length palindrome 
            temp = self.helper(s,i,i)      # odd length palin
            if len(temp)> len(result):
                result = temp
            
            temp = self.helper(s,i,i+1)     # even length palin
            if len(temp) > len(result):
                result  = temp
        return result
            
    
    def helper(self,arr,start,end):
        while start>=0 and end<len(arr) and arr[start] == arr[end]:
            start -= 1              # expand outwards
            end += 1
        temp = arr[start+1 : end]
        return temp
    
