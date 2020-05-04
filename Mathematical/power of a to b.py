#METHOD 1

def myPow(self, X, n) :
        if n==0:
            return 1
        if n<1:
            return 1/(self.myPow(x,-n))     # take reciprocal and change sign to positive and calculate for 1/(result)
        if n%2!=0: #odd
            return x*self.myPow(x*x,n//2) #decrease n to half and multiply odd term with result
        else:
            return self.myPow(x*x,n//2)


#METHOD 2
        
def myPow(self,x,n):
        ans=1
        if n==0:
            return 1
        if n<0:
            n=-n    #reverse sign
            x=1/x     #take reciprocal
        while (n!=0):
            if n%2!=0:       # if odd mulptiply ans with x
                ans*=x
            x*=x             # take square of x
            n>>=1            # n//2
        return ans
