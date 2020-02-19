# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:02:54 2020

@author: arjun
"""
import numpy as np
#Node_State= np.array([[2,8,3], [1,6,4], [7,0,5]])
#Node_State= np.array([[1,2,3], [4,5,6], [7,0,8]])
Node_State= np.array([[1,2,3], [4,6,5], [8,0,7]])

Nodes={0:Node_State}
Node_index=1
Parent_Node_index=0
Nodesinfo=[]
Goal=np.array([[1,2,3], [4,5,6], [7,8,0]])
def BlankTileLocation(CurrentNode):
    for i in range (0,Node_State.shape[0]): 
        for j in range (0,Node_State.shape[1]):
              if(CurrentNode[i][j]==0):
                    return [i,j]
def ActionMoveLeft(CurrentNode):
    [i ,j] = BlankTileLocation(CurrentNode)
    s=0
    if (j>0):
        NewNode=np.copy(CurrentNode)
        temp=NewNode[i][j-1]
        NewNode[i][j-1]=NewNode[i][j]
        NewNode[i][j]=temp
        if np.all(NewNode==Goal):
            s=1  
        return [s,NewNode]
    else:
        return[s,CurrentNode]
def ActionMoveRight(CurrentNode):
    [i ,j] = BlankTileLocation(CurrentNode)
    s=0
    if (j<2):
        NewNode=np.copy(CurrentNode)
        temp=NewNode[i][j+1]
        NewNode[i][j+1]=NewNode[i][j]
        NewNode[i][j]=temp
        if np.all(NewNode==Goal):
            s=1  
        return [s,NewNode]
    else:
        return[s,CurrentNode]
def ActionMoveUp(CurrentNode):
    [i ,j] = BlankTileLocation(CurrentNode)
    s=0
    if (i>0):
        NewNode=np.copy(CurrentNode)
        temp=NewNode[i-1][j]
        NewNode[i-1][j]=NewNode[i][j]
        NewNode[i][j]=temp
        if np.all(NewNode==Goal):
            s=1
        return [s,NewNode]
    else:
        return[s,CurrentNode]
def ActionMoveDown(CurrentNode):
    [i ,j] = BlankTileLocation(CurrentNode)
    s=0
    print(i)
    if (i<2):
        NewNode=np.copy(CurrentNode)
        temp=NewNode[i+1][j]
        NewNode[i+1][j]=NewNode[i][j]
        NewNode[i][j]=temp
        if np.all(NewNode==Goal):
            s=1  
        return [s,NewNode]
    else:
        return[s,CurrentNode]
def AddNode(CurrentNode):
    flag=1
    global Node_index
    global Parent_Node_index
    global Nodes    
    global Nodesinfo
    st=1
    for i in Nodes.values():
        if np.all(CurrentNode==i):
            flag=0
            break
    if (flag==1):
             Nodes[Node_index]=CurrentNode
             Node_index+=1
             
if __name__ == "__main__":
 while (1):
   [stat,NewNode]=ActionMoveLeft(Nodes[Parent_Node_index])
   AddNode(NewNode)
   print("Left")
   if (stat==1):
       print("Goal found")
       break
   [stat,NewNode]=ActionMoveRight(Nodes[Parent_Node_index])
   AddNode(NewNode)
   print("Right")
   if (stat==1):
       print("Goal found")
       break
   [stat,NewNode]=ActionMoveUp(Nodes[Parent_Node_index])
   AddNode(NewNode)
   print("Up")
   if (stat==1):
       print("Goal found")
       break
   [stat,NewNode]=ActionMoveDown(Nodes[Parent_Node_index])
   AddNode(NewNode)
   print("Down")
   if (stat==1):
       print("Goal found")
       break
   Parent_Node_index+=1
