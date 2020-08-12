#undirected graph
#adjacency matrix and ordered pair representation

import numpy as np
n=int(input("Number of vertices of Graph: "))
graph_vertices=[]
graph_vertices=list(range(1,n+1))
m=int(input("Number of edges of Graph: "))
mat=np.zeros((n,n),dtype=int)
graph_edge=[]

for i in range(m):
	print("Enter edge between vertices: ")
	a,b=map(int,input().split())
	if(a<n+1 and b<n+1):
		mat[a-1,b-1]=1
		mat[b-1,a-1]=1
		graph_edge.append([a,b])
		graph_edge.append([b,a])





