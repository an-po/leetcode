class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = list()
        for c in s:
            if c == '(':
                st.append(c)
            elif c == '[':
                st.append('[')
            elif c == '{':
                st.append('{')
            elif c == ')':
                if (st == []) or (st.pop() != '('):
                    return False
            elif c == ']':
                if (st == []) or (st.pop() != '['):
                    return False
            elif c == '}':
                if (st == []) or (st.pop() != '{'):
                    return False
        if st != []:
            return False
        else:
            return True