# METHOD 1  Backtracking  O(2^(h+1)-1) -> O(2^n)        # h is depth of tree

def backtrack(s="",left =0 ,right = 0):
    if len(s)==2*n:
        ans.append(s)
        return 
    if left<n:              # valid only when opening bracket <= N
        backtrack(s+'(',left+1,right)
    if right<left:          # valid when closing bracket <= opening bracket
        backtrack(s+')',left,right+1)
ans = []
backtrack()
return ans


#METHOD 2       Iterative

def generateParenthesis(self, n: int) -> List[str]:
    ans = []
    stack = [('(',1,0)]
    while stack:
        s,left,right = stack.pop()
        if len(s) == 2*n:
            ans.append(s)
            continue
        if left < n:
            stack.append(( s+'(', left+1, right))
        if right < left:
            stack.append(( s+')', left, right+1))
    return ans
