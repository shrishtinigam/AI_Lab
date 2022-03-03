def get_start():
    print("Enter Start Position of 8 Puzzle: ")
    start_state = [0,0,0,0,0,0,0,0,0]
    i = 9
    while(i != 0):
        states = int(input(f"Number at {9 - i} place: "))
        if states < 0 or states > 8:
            print("Only enter states between 0 and 8")
        else:
            start_state[9 - i] = states
            i = i - 1
    return start_state

def checker(data):
    goal = [1,2,3,4,5,6,7,8,0]
    if(data == goal):
        return True
    return False

# move up
def move_up(data, index):
    node = data.copy()
    exchange = node[index - 3]
    node[index] = exchange
    node[index - 3] = 0
    return node

# move down
def move_down(data, index):
    node = data.copy()
    exchange = node[index + 3]
    node[index] = exchange
    node[index + 3] = 0
    return node

# move left
def move_left(data, index):
    node = data.copy()
    exchange = node[index - 1]
    node[index] = exchange
    node[index - 1] = 0
    return node

# move right
def move_right(data, index):
    node = data.copy()
    exchange = node[index + 1]
    node[index] = exchange
    node[index + 1] = 0
    return node

def search_empty(data):
    for i in range(len(data)):
        if(data[i] == 0):
            return i


def node_search(data):
    final_data = []
    # check if data is the required result
    if(checker(data)):
        return 1, final_data
    index = search_empty(data)

    down = [0,1,2,3,4,5]
    up = [3,4,5,6,7,8]
    right = [0,1,3,4,6,7]
    left = [1,2,4,5,7,8]

    
    if(index in down):
        print("down")
        new_data_1 = move_down(data, index)   
        final_data.append(new_data_1)
        if(checker(new_data_1)):
            return 1, final_data

    if(index in up):
        print("up")
        new_data_2 = move_up(data, index)
        final_data.append(new_data_2)
        if(checker(new_data_2)):
            return 1, final_data

    if(index in right):
        print("right")
        new_data_3 = move_right(data, index)
        final_data.append(new_data_3)
        if(checker(new_data_3)):
            return 1, final_data

    if(index in left):
        print("left")
        new_data_4 = move_left(data, index)
        final_data.append(new_data_4)
        if(checker(new_data_4)):
            return 1, final_data

    return 0, final_data

def bfs(data):
    result = 0
    queue = [data] # queue of all positions explored
    while(result == 0):
        result, new_nodes = node_search(queue[0])
        
        for i in new_nodes:
            if(i not in queue): # donot add in queue if already in queue (already explored)
                print("Found a new node")
                queue.append(i)
        queue.remove(queue[0]) # equivalent to a dequeue operation
        # print(queue)
    print(f"Found via BFS, present at the end of the queue.")

data = get_start()
bfs(data)