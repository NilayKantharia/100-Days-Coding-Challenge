def reverseLevelOrder(root):
    res = []
    st = []
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        st.append(node.data)
        
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)
            
    while st:
        res.append(st.pop())
        
    return res
