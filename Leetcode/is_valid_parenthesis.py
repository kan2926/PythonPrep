def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        d = {'(': ')', '[':']', '{':'}'}
        st = []
        for i in range(n):
            if s[i] in d.keys():
                st.append(d[s[i]])
            else:
                if st:
                        tmp = st[-1]
                        if s[i] == tmp:
                            st.pop()
                        else:
                            st.append(s[i])
                else:
                        st.append(s[i])
        
        if not st:
            return True
        else:
            return False

s = input("enter string:")
print(isValid(s))
