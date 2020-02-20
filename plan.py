
import numpy as np
#Node_State= np.array([[2,8,3], [1,6,4], [7,0,5]])
#Node_State= np.array([[1,2,3], [4,5,6], [7,0,8]])
#Node_State= np.array([[1,2,3], [4,6,5], [8,0,7]])
#Node_State=np.array([[1,0,3],[4,2,5],[7,8,6]])#very easy
Node_State=np.array([[6,3,0],[2,1,8],[5,4,7]]) #easy
#Node_State=np.array([[6,3,8],[2,4,1],[0,5,7]]) #med
#Node_State=np.array([[8,6,7],[2,5,4],[3,0,1]]) #hard
Nodes={0:Node_State}
Node_index=1
Parent_Node_index=0
Nodesinfo={}
Goal=np.array([[1,2,3], [4,5,6], [7,8,0]])
def BlankTileLocation(CurrentNode):
    for i in range (0,3): 
        for j in range (0,3):
              if(CurrentNode[i][j]==0):
                    return [i,j]
def checkgoal(a,b):
    for i in range(0,3):
        for j in range(0,3):
            if a[i][j] !=b[i][j]:
                return False
    return True
#// A utility function to count inversions in given array 'arr[]' 
#int getInvCount(int arr[]) 
#{ 
#    int inv_count = 0; 
#    for (int i = 0; i < 9 - 1; i++) 
#        for (int j = i+1; j < 9; j++) 
#             // Value 0 is used for empty space 
#             if (arr[j] && arr[i] &&  arr[i] > arr[j]) 
#                  inv_count++; 
#    return inv_count; 
#} 
#  
#// This function returns true if given 8 puzzle is solvable. 
#bool isSolvable(int puzzle[3][3]) 
#{ 
#    // Count inversions in given 8 puzzle 
#    int invCount = getInvCount((int *)puzzle); 
#  
#    // return true if inversion count is even. 
#    return (invCount%2 == 0); 
#} 
def ActionMoveLeft(CurrentNode):
    [i ,j] = BlankTileLocation(CurrentNode)
    s=0
    if (j>0):
        NewNode=np.copy(CurrentNode)
        NewNode[i][j-1],NewNode[i][j]=NewNode[i][j], NewNode[i][j-1]
        if checkgoal(NewNode,Goal):
            s=1  
        return [s,NewNode]
    else:
        return[2,0]
def ActionMoveRight(CurrentNode):
    [i ,j] = BlankTileLocation(CurrentNode)
    s=0
    if (j<2):
        NewNode=np.copy(CurrentNode)
        NewNode[i][j+1],NewNode[i][j]=NewNode[i][j], NewNode[i][j+1]
        if checkgoal(NewNode,Goal):
            s=1  
        return [s,NewNode]
    else:
        return[2,0]
def ActionMoveUp(CurrentNode):
    [i ,j] = BlankTileLocation(CurrentNode)
    s=0
    if (i>0):
        NewNode=np.copy(CurrentNode)
        NewNode[i-1][j],NewNode[i][j]=NewNode[i][j], NewNode[i-1][j]
        if checkgoal(NewNode,Goal):
            s=1
        return [s,NewNode]
    else:
        return[2,0]
def ActionMoveDown(CurrentNode):
    [i ,j] = BlankTileLocation(CurrentNode)
    s=0
    if (i<2):
        NewNode=np.copy(CurrentNode)
        NewNode[i+1][j],NewNode[i][j]=NewNode[i][j], NewNode[i+1][j]
        if checkgoal(NewNode,Goal):
            s=1  
        return [s,NewNode]
    else:
        return[2,0]
def AddNode(CurrentNode):
    flag=1
    global Node_index
    global Parent_Node_index
    global Nodes    
    global Nodesinfo
    st=1
    for i in Nodes.values():
        if checkgoal(CurrentNode,i):
            flag=0
            break
    if (flag==1):
             Nodes[Node_index]=CurrentNode
             Nodesinfo[Node_index]=Parent_Node_index
             Node_index+=1

def ReorderNode(Node):
    n=[]
    for j in range(Node_State.shape[0]):
       for i in range(Node_State.shape[0]):
                           n.append(Node[i][j])
    return n
def Backtrack():
    global Nodesinfo
    order=[]
    order.append((Nodesinfo.keys()).pop())
    order.append((Nodesinfo.values()).pop())
    while(order[len(order)-1]!=0):
          for key in Nodesinfo.keys():
                   if key==order[len(order)-1]:
                           order.append(Nodesinfo[key])
                           break          
    order.reverse()
    return order   
              
def reorder(arr):    
    temp = [0] * 9; 
    index=[0,3,6,1,4,7,2,5,8]
    # arr[i] should be 
        # present at index[i] index 
    for i in range(0,9): 
        temp[index[i]] = arr[i] 
    return temp
    

while (1):
     
   [stat,NewNode]=ActionMoveRight(Nodes[Parent_Node_index])
   if (stat==0):
       AddNode(NewNode)
       print("Right")
   if (stat==1):
       AddNode(NewNode)
       print("Goal found")
       break
     
   [stat,NewNode]=ActionMoveLeft(Nodes[Parent_Node_index])
   if (stat==0):
       AddNode(NewNode)
       print("Left")
   if (stat==1):
       AddNode(NewNode)
       print("Goal found")
       break
   
   [stat,NewNode]=ActionMoveUp(Nodes[Parent_Node_index])
   if (stat==0):
       AddNode(NewNode)
       print("Up")
   if (stat==1):
       AddNode(NewNode)
       print("Goal found")
       break


   [stat,NewNode]=ActionMoveDown(Nodes[Parent_Node_index])
   if (stat==0):
       AddNode(NewNode)
       print("Down")
   if (stat==1):
       AddNode(NewNode)
       print("Goal found")
       break
   Parent_Node_index+=1

order=Backtrack()
p= open("nodepath.txt","w+")      
for i in order:
    k=reorder(((Nodes.values())[i]).reshape(9,))
    str1 = " " .join(map(str, k)) 
    p.write(str1 +'\n')
p.close()
   
f= open("Nodes.txt","w+")      
for i in Nodes.values():
     k=ReorderNode(i)
     str1 = " " .join(map(str, k)) 
     f.write(str1 +'\n')
f.close()

c= open("Nodesinfo.txt","w+")      
for k,v in Nodesinfo.items():
    c.write(str(k))
    c.write(' ')
    c.write(str(v) +'\n')
c.close()




    