class Solution:
    def insertAtBottom(self,st,x):
        temp = []
        for i in range(len(st)):
            temp.append(st.pop())
        st.append(x)
        for i in range(len(temp)-1,-1,-1):
            st.append(temp[i])
        return st
