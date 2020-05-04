class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        prev = [[ele] for ele in nums]      # initially creating an array containing subset of size 1
        while  len(prev)>1:                #until we get a single merged list
            curr = []
            for i in range(0,len(prev),2):     # at each step taknig two subsets
                if i+1>=len(prev):
                    curr.append(prev[i])          # directly append to current
                else:
                    curr.append( self.merge(prev[i],prev[i+1]) )   # getting merged subsets of size 2,4,8...
            prev = curr                     # change prev to new merged subsets of array
            #print(prev)
        return prev[0]              # after merging all subsets we get sorted list
    def merge(self,l1,l2):
        merged = []
        i,j,k=0,0,0
        while i<len(l1) and j<len(l2):
            if l1[i]<=l2[j]:
                merged.append(l1[i])
                i+=1
            else:
                merged.append(l2[j])
                j+=1
        merged.extend(l1[i:])           # appending any remaining elements
        merged.extend(l2[j:])
        return merged 
    
