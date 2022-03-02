# incremental formulation

def valid_state(n, s):
    row = [0 for i in range(n)]
    for i in s:
        if(i.count(1) > 1):
            return False
        row_no = i.index(1)
        if(row[row_no] == 1):
            return False
        row[row_no] = 1
        
    # 1 - blue
    for k in range(1,n):
        i = k
        j = 0
        d = []
        while(i >= 0):
            d.append(s[i][j])
            if(d.count(1) > 1):
                return False
            j = j + 1
            i = i - 1
    # 2 - green
    for k in range(0,n-1):
        i = k
        j = 0
        d = []
        while(i < 8):
            d.append(s[i][j])
            if(d.count(1) > 1):
                return False
            j = j + 1
            i = i + 1
    # 3 - red
    for k in range(1, n - 1):
        i = n - 1
        j = k
        d = []
        while(j < 8):
            d.append(s[i][j])
            if(d.count(1) > 1):
                return False
            j = j + 1
            i = i - 1
    # 4 - black
    for k in range(1, n-1):
        i = 0
        j = k
        d = []
        while(j < 8):
            x = s[i][j]
            d.append(x)
            if(d.count(1) > 1):
                return False
            j = j + 1
            i = i + 1
    return True


            
n1 = 8
s1 = [[0 for i in range(n1)] for i in range(n1)]
s1 = [[0,0,1,0,0,0,0,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,1,0],
        [0,0,0,0,0,1,0,0],
        [0,1,0,0,0,0,0,0]]
print(s1[0][7])
print(valid_state(n1, s1))