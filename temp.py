def MC(data):
    node = data.copy()
    if(node[2] == 1):
        node[2] = 0
    else:
        node[2] = 1
    if(node[1] > 0 and node[0] > 0):
        node[1] = node[1] - 1
        node[0] = node[0] - 1
        if(node[0] < node[1]):
            return [-1]
        if(n - node[0] < n - node[1]):
            return [-1]
        if node in closed and node in open:
            return [-1]
        ans.append('MC')
        return node
    return [-1]
    
def C(data):
    node = data.copy()
    if(node[2] == 0):    
        node[2] = 1
        if(node[1] > 0):
            node[1] = node[1] - 1
        else:
            return [-1]
    else:
        node[2] = 0
        if(node[1] < n):
            node[1] = node[1] + 1
        else:
            return [-1]
    if((node[0] < node[1]) or (n - node[0] < n - node[1] and node[0] != 3)):
        return [-1]
    if node in closed and node in open:
        return [-1]
    ans.append('C')
    return node