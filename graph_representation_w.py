#weighted graph
#adjacency matrix and ordered pair representation
#directed_decision--> 1 for directed and 0  for un-directed

import numpy as np
directed_decision=int(input("Graph is directed? : "))
n=int(input("Number of vertices of Graph: "))
graph_vertices=[]
graph_vertices=list(range(1,n+1))
m=int(input("Number of edges of Graph:  "))
mat=np.zeros((n,n),dtype=int)
graph_edge=[]

for i in range(m):
	print("Enter edge between vertices and its weight: ")
	a,b,weight=map(int,input().split())
	if(a<n+1 and b<n+1):
		if(directed_decision==0):
			mat[a-1,b-1]=weight
			mat[b-1,a-1]=weight
			graph_edge.append([a,b,weight])
			graph_edge.append([b,a,weight])
		else:
			mat[a-1,b-1]=weight
			graph_edge.append([a,b,weight])






