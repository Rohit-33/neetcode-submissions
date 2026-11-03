class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for i in range (len(s)) :
            if s[i] == '(' or s[i] == '{' or s[i] == '[' :
                st.append(s[i])
            else:
                if len(st) == 0 :
                    return False
                if s[i] == ')':
                    if st[-1] == '(':
                        st.pop()
                    else :
                        return False
                elif s[i] == '}':
                    if st[-1] == '{':
                        st.pop()
                    else :
                        return False
                elif s[i] == ']':
                    if st[-1] == '[':
                        st.pop()
                    else :
                        return False
            
        return len(st) == 0