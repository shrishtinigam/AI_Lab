"""
Missionaries and Cannibals is a problem in which 3 missionaries and 3 cannibals want to cross from 
the left bank of a river to the right bank of the river. There is a boat on the left bank, but it 
only carries at most two people at a time (and can never cross with zero people). If cannibals ever 
outnumber missionaries on either bank, the cannibals will eat the missionaries. 
A state can be represented by a triple, (M C B), where M is the number of missionaries on the left, 
C is the number of cannibals on the left, and B indicates whether the boat is on the left bank or 
right bank. For example, the initial state is (3 3 L) and the goal state is (0 0 R). 
"""
# Let left bank be 0, right bank be 1
n = 3
global ans
ans = []
open = []
closed = []
global index
index = [-1]
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
    if((node[0] < node[1] and node[0] != 0) or (n - node[0] < n - node[1] and node[0] != 3)):
        return [-1]
    if node in closed or node in open:
        return [-1]
    ans.append('C')
    return node


def M(data):
    node = data.copy()
    if(node[2] == 0):    
        node[2] = 1
        if(node[0] > 0):
            node[0] = node[0] - 1
        else:
            return [-1]
    else:
        node[2] = 0
        if(node[0] < n):
            node[0] = node[0] + 1
        else:
            return [-1]
    if((node[0] < node[1] and node[0] != 0) or (n - node[0] < n - node[1] and node[0] != 3)):
        return [-1]
    if node in closed or node in open:
        return [-1]
    ans.append('M')
    return node

def CC(data):
    node = data.copy()
    if(node[2] == 0):    
        node[2] = 1
        if(node[1] > 1):
            node[1] = node[1] - 2
        else:
            return [-1]
    else:
        node[2] = 0
        if(node[1] < n-1):
            node[1] = node[1] + 2
        else:
            return [-1]
    if((node[0] < node[1] and node[0] != 0) or (n - node[0] < n - node[1] and node[0] != 3)):
        return [-1]
    if node in closed or node in open:
        return [-1]
    ans.append('CC')
    return node

def MM(data):
    node = data.copy()
    if(node[2] == 0):    
        node[2] = 1
        if(node[0] > 1):
            node[0] = node[0] - 2
        else:
            return [-1]
    else:
        node[2] = 0
        if(node[0] < n-1):
            node[0] = node[0] + 2
        else:
            return [-1]
    if((node[0] < node[1] and node[0] != 0) or (n - node[0] < n - node[1] and node[0] != 3)):
        return [-1]
    if node in closed or node in open:
        return [-1]
    ans.append('MM')
    return node

def MC(data):
    node = data.copy()
    if(node[2] == 0):    
        node[2] = 1
        if(node[1] > 0 and node[0] > 0):
            node[1] = node[1] - 1
            node[0] = node[0] - 1
        else:
            return [-1]
    else:
        node[2] = 0
        if(node[1] < n and node[1] < n):
            node[1] = node[1] + 1
            node[0] = node[0] + 1
        else:
            return [-1]
    if((node[0] < node[1] and node[0] != 0) or (n - node[0] < n - node[1] and node[0] != 3)):
        return [-1]
    if node in closed or node in open:
        return [-1]
    ans.append('MC')
    return node

def generate_positions(data):
    node = data.copy()
    positions = []
    cc = CC(node)
    mc = MC(node)
    mm = MM(node)
    c = C(node)
    m = M(node)
    
    if cc[0] != -1:
        positions.append(cc)
    if mc[0] != -1:
        positions.append(mc)
    if mm[0] != -1:
        positions.append(mm)
    if c[0] != -1:
        positions.append(c)
    if m[0] != -1:
        positions.append(m)
    return positions



def bfs(cur):
    if(cur == [0,0,1]):
        return True
    # Adding new possibilities from current node to open
    if cur in closed:
        return
    positions = generate_positions(cur)
    # print(positions)
    print(ans)
    if len(positions) == 0:
        ans.pop(index[0])
    else:
        index[0] = index[0] + 1
    
    for position in positions:
        open.append(position)
    open.remove(cur)
    closed.insert(0,cur)
    print(f"Open:{open}")
    print(f"Closed:{closed}")
    bfs(open[0])

start = [3,3,0]
open.append(start)
print(f"Open:{open}")
print(f"Closed:{closed}")
bfs(start)

ans.pop()
print(ans)



