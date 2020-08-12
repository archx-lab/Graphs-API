import numpy as np
from collections import deque
from graph_representation_w import graph_vertices,mat,graph_edge,n,weight

#variables 
bfs_path=[]
dfs_path=[]
visited=[]
dq=deque()

def possible_vertices(vertex,graph_vertices,mat):
	temp=[]
	for i in range(len(graph_vertices)):
		if(mat[vertex-1,i] or mat[i,vertex-1]):
			temp.append(i+1)
	return sorted(temp)

def bfs(root,mat,graph_vertices):
	if(len(visited)!=len(graph_vertices)):
		if(root not in visited):
			visited.append(root)
			bfs_path.append(root)
			for i in possible_vertices(root,graph_vertices,mat):
				if(i not in dq):
					dq.append(i)
			return bfs(dq.popleft(),mat,graph_vertices)
		else:
			return bfs(dq.popleft(),mat,graph_vertices)
	else:
		return bfs_path

def dfs(root,mat,graph_vertices):
	if(len(visited)!=len(graph_vertices)):
		if(root not in visited):
			visited.append(root)
			dfs_path.append(root)
			for i in sorted(possible_vertices(root,graph_vertices,mat),reverse=True):
				if(i not in dq):
					dq.append(i)
			return dfs(dq.pop(),mat,graph_vertices)
		else:
			return dfs(dq.pop(),mat,graph_vertices)
	else:
		return dfs_path
