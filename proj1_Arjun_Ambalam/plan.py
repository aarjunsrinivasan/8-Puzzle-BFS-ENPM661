# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:20:03 2020

@author: arjun
"""

import numpy as np
#Node_State=np.array([[1,0,3],[4,2,5],[7,8,6]])#very easy
#Node_State=np.array([[1,0,3],[4,2,5],[7,8,6]])#very easy
#Node_State=np.array([[6,3,0],[2,1,8],[5,4,7]]) #easy
#Node_State=np.array([[6,3,8],[2,4,1],[0,5,7]]) #med
#Node_State=np.array([[8,6,7],[2,5,4],[3,0,1]]) #hard
#Node_State=np.array([[5,2,8],[4,1,7],[0,3,6]]) 
Nodes={0:Node_State}
Node_index=1
Parent_Node_index=0
Nodesinfo={}
Goal=np.array([[1,2,3], [4,5,6], [7,8,0]])
def Arr2Str(Node):
    s=Node.reshape(9,)
    str1 = ''.join(str(e) for e in s)
    return str1
snode={Arr2Str(Node_State):0}

def isSolvable(Node):
               sa=Node.reshape(9,)
               sa=list(sa)
               for k in sa:
                       if k==0:
                             sa.remove(k)
               s=0
               for i in range(0,len(sa)):
                       for j in range(i+1,len(sa)):
                                           if(sa[j]>sa[i]):
                                                        s+=1
               return(s%2==0)
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
    flag=0
    global Node_index
    global Parent_Node_index
    global Nodes    
    global Nodesinfo
    global snode
    if(snode.get(Arr2Str(CurrentNode),-1)==-1):
                                     flag=1
    if (flag==1):
             Nodes[Node_index]=CurrentNode
             snode[Arr2Str(CurrentNode)]=Node_index
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
    ke=list(Nodesinfo.keys())
    va=list(Nodesinfo.values())
    order.append(ke.pop())
    order.append(va.pop())
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
    for i in range(0,9): 
        temp[index[i]] = arr[i] 
    return temp

print("Enter the initial state of the puzzle row wise")
print("\n")
for i in range(0,3):
   for j in range(0,3):
       Node_State[i][j]=input()

print("The Initial Puzzle State is")
print(Node_State)
if(isSolvable(Node_State)):
    print("The Puzzle is Solvable")
    br=1
else:
    print("The Puzzle is not Solvable")
    br=0
    
while (br):
     
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
if(br==1):
 order=Backtrack()
 p= open("nodePath.txt","w+")      
 for i in order:
    va=list(Nodes.values())
    k=reorder((va[i]).reshape(9,))
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
 c.write(str(1))
 c.write(' ')
 c.write(str(0) +'\n')   
 for k,v in Nodesinfo.items():
    c.write(str(k+1))
    c.write(' ')
    c.write(str(v+1) +'\n')
 c.close()




    