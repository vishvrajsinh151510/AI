#Name: Vishvrajsinh zala
#Eno : 92600584082
#6. Write a program to implement Single Player Game (Using Heuristic Function)

goal=(1,2,3,
      4,5,6,
      7,8,0)

#print puzzle
def print_board(state):
    for i in range(0,9,3):
        print(state[i:i+3])
    print()
    
    
    
#heuristic function
#count how many tiles are in the wrong postion 

def heuristic(state):
    count=0
    
    for i in range(9):
        if state[i]!=0 and state[i]!= goal[i]:
            count +=1
    return count

def get_neighbors(state):
    neighbors=[]
    zero=state.index(0)
    row,col =divmod(zero,3)
    
    moves=[(-1,0),(1,0),(0,-1),(0,1)]
    
    for dr,dc in moves:
        new_row=row+dr
        new_col=col+dc       
        
        if 0<=new_row<3 and 0<=new_col<3:
            new_zero=new_row*3+new_col
            
            new_state=list(state)
            new_state[zero],new_state[new_zero]=\
                new_state[new_zero],new_state[zero]
                
                
            neighbors.append(tuple(new_state))
            
    return neighbors

#heuristic search
def heuristic_search(start):
    current =start
    path =[current]
    visited=set()
    
    while current!=goal:
        visited.add(current)
        
        neighbors=get_neighbors(current)
        
        new_neighbors=[]
        
        for n in neighbors:
            if n not in visited:
                new_neighbors.append(n)
                
        neighbors=new_neighbors
        if not neighbors:
            return None
        
        
        current=min(neighbors,key=heuristic)
        
        path.append(current)
        
    return path


start=(1,2,3,
       4,0,6,
       7,5,8)

solution=heuristic_search(start)


if solution:
    print("solution found in",len(solution)-1,"moves:\n") 
    
    for step in solution:
        print_board(step)
else:
    print("No solution fund.")               
    
