class Solution:
    def removeOuterParentheses(self, S:str) -> str:
        #output string
        output = ""
        #initialize the stack
        st = []
        for i in range(len(S)):
            if S[i] == '(':
                st.append(i)
            else:
                if st:
                    pop_str_index = st.pop()
                    
                    if len(st) == 0:
                        istr = S[pop_str_index+1:i]
                        output += istr
                        
        return output
if __name__ == '__main__':
    s = Solution()
    print(s.removeOuterParentheses("(()())(())"))


