#directed graph
#edge insertion and deletion

import numpy as np
from graph_representation_di import graph_vertices


def insert_edge(mat,from_vertex,to_vertex):
	print("Enter from_vertex and to_vertex:")
	from_vertex,to_vertex=map(int,input().split())
	if(from_vertex in graph_vertices and to_vertex in graph_vertices):
		if(mat[from_vertex-1,to_vertex-1]==0):
			mat[from_vertex-1,to_vertex-1]=1
		else:
			print("Edge already existed")
	else:
		if(from_vertex not in graph_vertices and to_vertex not in graph_vertices):
			print("No from_vertex and No to_vertex found")
		if(from_vertex not in graph_vertices):
			print("No from_vertex")
			temp=int(input("Want to insert from_vertex: "))
			if(temp==1):
				mat=insert_vertex(mat,graph_vertices,particular_vertex_decision=False)
				insert_edge(mat,from_vertex,to_vertex)
		if(to_vertex not in graph_vertices):
			print("No to_vertex")
			temp=int(input("Want to insert to_vertex: "))
			if(temp==1):
				mat=insert_vertex(mat,graph_vertices,particular_vertex_decision=False)
				insert_edge(mat,from_vertex,to_vertex)


def delete_edge(mat,from_vertex,to_vertex):
	print("Enter from_vertex and to_vertex: ")
	from_vertex,to_vertex=map(int,input().split())
	if(from_vertex in graph_vertices and to_vertex in graph_vertices):
		if(mat[from_vertex-1,to_vertex-1]==1):
			mat[from_vertex-1,to_vertex-1]=0
			print("Edge deleted")
		else:
			print("No edge is present")
	else:
		print("No vertices specified are present")
		
