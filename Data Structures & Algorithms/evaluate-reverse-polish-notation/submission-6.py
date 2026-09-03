class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                st.append(int(t))
            else:
                x = st.pop()
                y = st.pop()
                if t == '+':
                    res = x + y
                elif t == '-':
                    res = y - x
                elif t == '*':
                    res = x * y
                else:
                    res = int(y / x)
                st.append(res)
        return int((st.pop()))