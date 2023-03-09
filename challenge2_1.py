def solution(src, dest):
    if src == dest:
        return  0
    else:
        adj_list = gen_graph()
        prev_list = bfs(src,adj_list)
        min_jumps = reconstructPath(src,dest,prev_list)
        return min_jumps

def bfs(src,graph):
    queue = [src] #queue 
    prev = [] #remember previous node for path reconstruction
    for i in range(64):
        prev.append(None)
    head_of_queue = 0 #point to first element in queue
    skip_flag = 0 
    while(head_of_queue != len(queue)):
        node = queue[head_of_queue] #get node
        neighbors = graph[node] #get neighbors of node from adjecency list
        for neighbor in neighbors: #loop through neighbors
            for i in range(len(queue)): #skip already visited neighbors
                if(queue[i] == neighbor):
                    skip_flag = 1
            if skip_flag == 0: #not visited previously
                queue.append(neighbor) #enqueue
                prev[neighbor] = node #remember predecessor node
            skip_flag = 0 #reset skip flag
        head_of_queue += 1 #dequeue  
    return prev 

def reconstructPath(src,dest,prev):
    path = [dest] #reconstruct path from end to start
    predecessor = prev[dest] #get predecessor of dest
    path.append(predecessor) #add to path
    if predecessor == src:
        return len(path)-1
    while True: #recursively get predecessor until predecessor == src     
        predecessor = prev[predecessor]
        path.append(predecessor)  
        if predecessor == src:
            break

    return len(path)-1 #-1 because we want the number of jumps not the number of visited nodes

def gen_graph(): #turn chess field into a computer readable graph representation (adjacency list)
    chess_board = [[],[],[],[],[],[],[],[]]

    for row in range(8): #reconstruct chess board
        for column in range(8):
            chess_board[row].append(column+(row * 8))
    
    adj_list = []
    for i in range(64): #generate adjacency list
        adj_list.append([])
    
    for row in range(8):
        for column in range(8):
            for j in range(8): #check possible neighbors (max 8)

                if j == 0:
                    x = row + 2
                    y = column + 1
                    if((x > -1 and x < 8) and (y > -1 and y < 8)): #check if possible
                        neighbor = chess_board[x][y]
                    else: #check next possible neighbor
                        continue
                if j == 1:
                    x = row + 2
                    y = column - 1
                    if((x > -1 and x < 8) and (y > -1 and y < 8)):
                        neighbor = chess_board[x][y]
                    else:
                        continue
                if j == 2:
                    x = row - 2
                    y = column + 1
                    if((x > -1 and x < 8) and (y > -1 and y < 8)):
                        neighbor = chess_board[x][y]
                    else:
                        continue
                if j == 3:
                    x = row - 2
                    y = column - 1
                    if((x > -1 and x < 8) and (y > -1 and y < 8)):
                        neighbor = chess_board[x][y]
                    else:
                        continue
                if j == 4:
                    x = row - 1
                    y = column + 2
                    if((x > -1 and x < 8) and (y > -1 and y < 8)):
                        neighbor = chess_board[x][y]
                    else:
                        continue
                if j == 5:
                    x = row + 1
                    y = column + 2
                    if((x > -1 and x < 8) and (y > -1 and y < 8)):
                        neighbor = chess_board[x][y]
                    else:
                        continue
                if j == 6:
                    x = row - 1
                    y = column - 2
                    if((x > -1 and x < 8) and (y > -1 and y < 8)):
                        neighbor = chess_board[x][y]
                    else:
                        continue
                if j == 7:
                    x = row + 1
                    y = column - 2
                    if((x > -1 and x < 8) and (y > -1 and y < 8)):
                        neighbor = chess_board[x][y]
                    else:
                        continue

                if(neighbor > -1 and neighbor < 64):
                    adj_list[column + (row * 8)].append(neighbor) #append neighbor to adjacency list

    return adj_list

print(solution(36,21))