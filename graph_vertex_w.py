#weighted graph
#vertex insertion and deletion

import numpy as np
from graph_representation_w import mat,n,graph_vertices

def insert_vertex(mat,graph_vertices,particular_vertex_decision=False):
	if(particular_vertex_decision==True):
		particular_vertex=int(input("Enter the vertex to insert: "))
		if(particular_vertex in graph_vertices):
			print("Vertex already existed")
		else:
			mat=np.insert(mat,particular_vertex-1,0,axis=1)
			mat=np.insert(mat,particular_vertex-1,0,axis=0)
			return mat
	else:
		graph_vertices.append(len(graph_vertices))
		mat=np.append(mat,np.zeros((1,n),dtype=int),axis=0)
		mat=np.append(mat,np.zeros((n+1,1),dtype=int),axis=1)
		return mat	

def remove_vertex(mat,graph_vertices):
	remove_vertex=int(input("Enter vertex to remove: "))
	if(remove_vertex in graph_vertices):
		graph_vertices.remove(remove_vertex)
	mat=mat[:,list(np.array(graph_vertices)-1)]
	mat=mat[list(np.array(graph_vertices)-1),:]
	return mat
