# METHOD 1 -> Recursion plus Memoization   time -> (m*n) space -> O(m*n)

class Solution:
    def edit(self,w1,w2,m,n,cache):
        if m==0:    # insert all character of second on first string
            return n
        if n==0:    # remove all charcter from first string
            return m
        if cache[m][n] != -1:
            return cache[m][n]
        if w1[m-1] == w2[n-1]:  # if last character match skip them
            cache[m][n] = self.edit(w1,w2,m-1,n-1,cache)
            return cache[m][n]
        #remove character m-1
        #insert character n-1
        #replace charecter m-1, n-1
        cache[m][n] = 1 + min( self.edit(w1,w2,m-1,n,cache), self.edit(w1,w2,m,n-1,cache) , self.edit(w1,w2,m-1,n-1,cache))
        return cache[m][n]
    
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        cache = [[-1]*(n+1) for i in range(m+1)]
        return self.edit(word1,word2,m,n,cache)
