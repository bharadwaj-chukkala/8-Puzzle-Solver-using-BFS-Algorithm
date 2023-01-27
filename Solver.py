import numpy as np
import argparse

#####   To read the user input   #####

def read(configuration):
	initial_state = []
	data = configuration.split(",")
	for element in data:
		initial_state.append(int(element))
	return np.reshape(initial_state,(3,3))


#####   Blank Tile Position      #####
def zeropos(Initial_state):
    index = np.argwhere(Initial_state == 0)  #we get the position of zero in initial state
    return index


#####   Action set : Move UP     #####
def move_up(Curr_state):
    A = np.copy(Curr_state)
    loc = zeropos(A)                 #moving the slider up if possible 
    i = loc[:,0]
    j= loc[:,1] 
    if i-1<0:
        status = False 
        return A, status
    else:
        #print("UP")        
        A[i,j]= A[i-1, j]
        A[i-1, j] = 0
        status = True
        #print(A)
        return A, status
    
#####   Action set : Move Down    #####    
def move_down(Curr_state):
    A = np.copy(Curr_state)
    loc = zeropos(A)                 
    
    i = loc[:,0]
    j= loc[:,1]                     #moving the slider down if possible
    if i+1>2:
        status = False
        return A, status
    else:
        #print("DOWN")       
        A[i,j]= A[i+1, j]
        A[i+1, j] = 0
        status = True
        #print(A)
        return A, status
    
#####   Action set : Move Left    #####
def move_left(Curr_state):
    A = np.copy(Curr_state)
    loc = zeropos(A)                 
    
    i = loc[:,0]
    j= loc[:,1]                     #moving the slider left if possible
    if j-1<0:
        status = False 
        return A, status
    else:
        #print("Left")        
        A[i,j]= A[i, j-1]
        A[i, j-1] = 0
        status = True
        #print(A)
        return A, status
    
#####   Action set : Move Right    #####
def move_right(Curr_state):
    A = np.copy(Curr_state)
    loc = zeropos(A)                
    
    i = loc[:,0]
    j= loc[:,1]                    #moving the slider right if possible
    if j+1>2:
        status = False 
        return A, status
    else:
        #print("Right")        
        A[i,j]= A[i, j+1]
        A[i, j+1] = 0
        status = True
        #print(A)
        return A, status
  
#####    A logic to compare states   #####
def set_conversion(A):
	i = j = 0
	for iter1 in A:
		for iter2 in iter1:
			j+=iter2*(10**i)
			i+=1
	return j
    
    
#####   To see if the current state is already existing   #####
def check_if_visited(Current_state, exist_states):
    a = set_conversion(Current_state)
    return a in exist_states
        

##### To see if the current state mathes with goal state  #####
def check_goal(A, goal_state):
    status = np.array_equal(A,goal_state)
    #print(status)
    return status


#####  Initializing a default Goal state   #####
goal_state = np.array([[1,2,3],[4,5,6],[7,8,0]])

#####  Innitializing a state list   #####
state_list =[]
exist_states = set([])

#####   To get user input of initial state from Terminal   #####
parser = argparse.ArgumentParser()
parser.add_argument('Initial_state')
args = parser.parse_args()
initial_state = read(args.Initial_state)
state_list.append(initial_state)
exist_states.add(set_conversion(initial_state))


#####   Initializing container lists for bactracking and calculating cost  #####
child_state_index = []
child_state_index.append(0)
temp_index = []              ### A temporary list for copying new child states indices to child state index 
cost = 0
count = 0
child_state_number = 0

state_info = []
reached = False


#####   An iterative loop to perform an action set on parent states to create child states   #####
#####          Also checks if any state that was created is possibly a goal state            #####

while len(child_state_index)>0:

	temp_index = []
	for i in child_state_index:

		new_state, status = move_up(state_list[i])
		if status == True and not check_if_visited(new_state, exist_states):
			child_state_number += 1
			temp_index.append(child_state_number)
			state_list.append(new_state)
			temp_node_info = np.array([child_state_number,i,cost])
			state_info.append(temp_node_info)
			exist_states.add(set_conversion(new_state))

			if check_goal(new_state,goal_state):
				reached = True
				goal_state_index = child_state_number
				break

		new_state, status = move_down(state_list[i])
		if status == True and not check_if_visited(new_state, exist_states):
			child_state_number += 1
			temp_index.append(child_state_number)
			state_list.append(new_state)
			temp_node_info = np.array([child_state_number,i,cost])
			state_info.append(temp_node_info)
			exist_states.add(set_conversion(new_state))

			if check_goal(new_state,goal_state):
				reached = True
				goal_state_index = child_state_number
				break

		new_state, status = move_right(state_list[i])
		if status == True and not check_if_visited(new_state, exist_states):
			child_state_number += 1
			temp_index.append(child_state_number)
			state_list.append(new_state)
			temp_node_info = np.array([child_state_number,i,cost])
			state_info.append(temp_node_info)
			exist_states.add(set_conversion(new_state))

			if check_goal(new_state,goal_state):
				reached = True
				goal_state_index = child_state_number
				break

		new_state, status = move_left(state_list[i])
		if status == True and not check_if_visited(new_state, exist_states):
			child_state_number += 1
			temp_index.append(child_state_number)
			state_list.append(new_state)
			temp_node_info = np.array([child_state_number,i,cost])
			state_info.append(temp_node_info)
			exist_states.add(set_conversion(new_state))
            
			if check_goal(new_state,goal_state):
				reached = True
				goal_state_index = child_state_number
				break
            
#####  When the goal state is reached, we need to back track to find the shortest path   ####
	if reached == True:
		###  Generating the path to reach the goal state   ###
		generate_path = []
		gl_temp = goal_state_index-1
		generate_path.append(state_list[goal_state_index])
		print(generate_path)

        #writing the output(generated path) to a file
		while gl_temp>0:
			x = state_info[gl_temp]
			gl_temp = x[1]
			generate_path.append(state_list[gl_temp])
		print('Goal state reached =',reached)
		generate_path.reverse()
		generate_path_t = np.asarray(generate_path)
		

		with open('nodePath.txt', 'w') as node_path_file:
			for i in generate_path_t:
				t = np.empty([1,9])
				count = 0
				for j in i.T:
					for k in j:
						t[0,count] = k
						count+=1
				np.savetxt(node_path_file,t,delimiter='\t')
		break

	child_state_index = temp_index
	cost+=10
    
state_info_t = np.asarray(state_info)

#writing the output(Information of all states CHILD | PARENT | COST2COME) to the file
with open('NodesInfo.txt', 'w') as node_info_file:
	for i in state_info_t:
		t = np.empty([1,3])
		t[0,:]=i
		np.savetxt(node_info_file,t,delimiter='\t')

state_list_t = np.asarray(state_list)

#writing the output(All states possible) to the file
with open('Nodes.txt', 'w') as node_list_file:
	for i in state_list_t:
		t = np.empty([1,9])
		count = 0
		for j in i.T:
			for k in j:
				t[0,count] = k
				count+=1
		np.savetxt(node_list_file,t,delimiter='\t')

# If the goal node is not reached
if reached==False:
	print('Goal state cannot be achieved')
