import numpy as np
import math
from graph_representation_w import mat,graph_vertices,graph_edge
from graph_traversal_w import possible_vertices
temp=[]
dijkstra_visited=[]
dijkstra_distance=[math.inf]*len(graph_vertices)
dijkstra_distance[0]=0

def dijkstra(dijkstra_source,dijkstra_destination,mat):
	if(dijkstra_source in dijkstra_visited):
		return dijkstra_distance
	else:
		dijkstra_visited.append(dijkstra_source)
		dist_possible=[]
		temp_list=[]
		temp_possible=possible_vertices(dijkstra_source,graph_vertices,mat)

		for i in temp_possible:
			dist_possible.append([i,mat[dijkstra_source-1,i-1]])
			dijkstra_distance[i-1]=mat[dijkstra_source-1,i-1]
		temp_list=min(dist_possible,key=lambda x:x[1])

		if(temp_list[0]==dijkstra_destination):
			return dijkstra_distance

		
		temp_possible.remove(temp_list[0])

		for j in temp_possible:
			if(dijkstra_distance[temp_list[0]-1]+mat[temp_list[0]-1,j-1]<dijkstra_distance[j-1] and temp_list[0] not in dijkstra_visited):
				dijkstra_distance[j-1]=temp_list[1]+mat[temp_list[1]-1,j-1]

		return dijkstra(temp_list[0],dijkstra_destination,mat)

temp=dijkstra(1,3,mat)
print(temp)









