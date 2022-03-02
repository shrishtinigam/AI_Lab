def get_start():
    print("Enter Start Position of 8 Puzzle: ")
    start_state = [[0,0,0,0,0,0,0,0,0], 0]
    i = 9
    while(i != 0):
        states = int(input(f"Number at {9 - i} place: "))
        if states < 0 or states > 8:
            print("Only enter states between 0 and 8")
        else:
            start_state[0][9 - i] = states
            i = i - 1
    return start_state

def checker(data):
    goal = [1,2,3,8,0,4,7,6,5]
    if(data[0] == goal):
        return True
    return False

# move up
def move_up(data, index):
    node = data[0].copy()
    exchange = node[index - 3]
    node[index] = exchange
    node[index - 3] = 0
    return [node, 1+data[1]]

# move down
def move_down(data, index):
    node = data[0].copy()
    exchange = node[index + 3]
    node[index] = exchange
    node[index + 3] = 0
    return [node, 1+data[1]]

# move left
def move_left(data, index):
    node = data[0].copy()
    exchange = node[index - 1]
    node[index] = exchange
    node[index - 1] = 0
    return [node, 1+data[1]]

# move right
def move_right(data, index):
    node = data[0].copy()
    exchange = node[index + 1]
    node[index] = exchange
    node[index + 1] = 0
    return [node, 1+data[1]]

def search_empty(data):
    for i in range(len(data[0])):
        if(data[0][i] == 0):
            return i


def node_search(data):
    final_data = []
    # check if data is the required result
    index = search_empty(data)

    down = [0,1,2,3,4,5]
    up = [3,4,5,6,7,8]
    right = [0,1,3,4,6,7]
    left = [1,2,4,5,7,8]

    
    if(index in down):
        #print("down")
        new_data_1 = move_down(data, index)   
        final_data.append(new_data_1)

    if(index in up):
        #print("up")
        new_data_2 = move_up(data, index)
        final_data.append(new_data_2)

    if(index in right):
        #print("right")
        new_data_3 = move_right(data, index)
        final_data.append(new_data_3)

    if(index in left):
        #print("left")
        new_data_4 = move_left(data, index)
        final_data.append(new_data_4)

    return final_data


def dls(data, depth):
    result = 0
    stack = [data] # stack of all positions explored
    nodes = [data]
    while(result == 0):
        if(len(stack) == 0):
            print("Not Found")
            return
        index = stack.pop()
        if(checker(index)):
            result = 1
            break
        new_nodes = node_search(index)

        for i in new_nodes:
            if(i not in nodes): # donot add in stack if already in queue (already explored)
                if(i[1] <= depth):
                    nodes.append(i)
                    stack.append(i)
        print(stack)
    print("Found via DLS, present at the end of the stack.")


data = get_start()
dls(data, 6)