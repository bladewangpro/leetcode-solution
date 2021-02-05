## Unweighted Graph

### Breadth-first search

```pseudocode
"""Breadth-first search
G = (V, E) is represented using adjacency list
-------------------
G.Adj[u]: all the adjacent joints around joint 'u'
u.pi: the predecessor of u
u.d: the distance from the source s to vectex u
Q: a first-in first-out queue Q
-------------------
Gray: the frontier between discovered and undisconvered vertices
Black: all vertices adjacent to black vertices have been discovered
White: vertices that haven't been discovered
-------------------
Time Complexity: O(V+E)
"""

BFS(G, s)
	// except s point, the root point
    for each vertex u \in G.V - {s}
        u.color = WHITE
        u.d = \inf
        u.pi = NIL
    s.color = GRAY
    s.d = 0
    s.pi = NIL
    Q = \emptyset
    ENQUEUE(Q, s)
    while Q != \emptyset
        u = DEQUEUE(Q)
        for each v \in G.Adj[u]
            if v.color == WHITE
                v.color = GRAY
                v.d = u.d + 1
                v.pi = u
                ENQUEUE(Q, v)
        u.color = BLACK
```



### Depth-first search

```pseudocode
"""Depth-first search
G = (V, E) is represented using adjacency list
-------------------
G.Adj[u]: all the adjacent joints around joint 'u'
u.pi: the predecessor of u
u.d: discovery time, when the vertex has been discovered, it will has this timestamp
u.f: finishing time, when the vertex has been finished (the adjacent list has been searched), it will has this timestamp
Q: a first-in first-out queue Q
-------------------
Gray: the frontier between discovered and undisconvered vertices
Black: all vertices adjacent to black vertices have been discovered
White: vertices that haven't been discovered
-------------------
Time Complexity: O(V+E)
"""

DFS(G, s)
    for each vertex u \in G.V
        u.color = WHITE
        u.pi = NIL
    time = 0
    for each vertex u \in G.V
        if u.color == WHITE
            DFS-VISIT(G, u)
	
DFS-VISIT(G, u)
	time = time + 1 // white vertex u has just been discovered
	u.d = time
	u.color = GRAY
	for each v \in G.Adj[u] // explore edge(u, v)
		if v.color == WHITE
			v.pi = u
			DFS-VISIT(G, v)
	u.color = BLACK // blacken u; it is finished
	time = time + 1
	u.f = time
```

### Strongly connected component

```pseudocode
"""Procedule
1. call DFS(G) to compute finishing times u.f for each vertex u // u.f finishing time and u.d discovery time
2. compute GT // 比如说有向图G是从a到b，则GT就没有从a到b的线，有的是从b到a的线
3. call DFS(GT), but in the main loop of DFS, consider the vertices in order of decreasing u.f (as computed in line 1) // 这个可以想成用stack来存第一步的DFS(G)， 然后再用stack进行pop数据
4. output the vertices of each tree in the depth-first forest formed in line 3 as a separate strongly connected component
"""


# Python implementation of Kosaraju's algorithm to print all SCCs 

from collections import defaultdict 

#This class represents a directed graph using adjacency list representation 
class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #No. of vertices 
		self.graph = defaultdict(list) # default dictionary to store graph 

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	# A function used by DFS 
	def DFSUtil(self,v,visited): 
		# Mark the current node as visited and print it 
		visited[v]= True
		print (v) 
		#Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			if visited[i]==False: 
				self.DFSUtil(i,visited) 


	def fillOrder(self,v,visited, stack): 
		# Mark the current node as visited 
		visited[v]= True
		#Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			if visited[i]==False: 
				self.fillOrder(i, visited, stack) 
		stack = stack.append(v) 
	

	# Function that returns reverse (or transpose) of this graph 
	def getTranspose(self): 
		g = Graph(self.V) 

		# Recur for all the vertices adjacent to this vertex 
		for i in self.graph: 
			for j in self.graph[i]: 
				g.addEdge(j,i) 
		return g 



	# The main function that finds and prints all strongly 
	# connected components 
	def printSCCs(self): 
		
		stack = [] 
		# Mark all the vertices as not visited (For first DFS) 
		visited =[False]*(self.V) 
		# Fill vertices in stack according to their finishing 
		# times 
		for i in range(self.V): 
			if visited[i]==False: 
				self.fillOrder(i, visited, stack) 

		# Create a reversed graph 
		gr = self.getTranspose() 
		
		# Mark all the vertices as not visited (For second DFS) 
		visited =[False]*(self.V) 

		# Now process all vertices in order defined by Stack 
		while stack: 
			i = stack.pop() 
			print(f'--> poping {i}')
			if visited[i]==False: 
				gr.DFSUtil(i, visited) 
				print("")

# Create a graph given in the above diagram 
g = Graph(5) 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 1) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 


print ("Following are strongly connected components " +
						"in given graph") 
g.printSCCs() 
```





## Weighted Directed Graph

### Dijkstra 

```pseudocode
"""Components
G = (V, E)
w: weight function for edge, for example, w(u, v), 
the weight of the edges from u to v
s: source point
--------------------------------
The running time of Dijkstra due to the way to apply min-priority queue
	1. array (WORSE)
	2. binary min-heap (BEST)
	3. Fibonacci heap (BETTER)
"""


Dijkstra(G, w, s)
	INITIAL-SINGLE-SOURCE(G, s)
		for each vertex v \in G.V
			v.d = \inf
			v.pi = NIL
		s.d = 0
	S = \emptyset
	Q = G.V
	while Q != \emptyset
		u = EXTRACT-MIN(Q)
		S = S \cup {u}
		for each vertex v \in G.Adj[u]
			RELAX(u, v, w)
				if v.d > u.d + w(u, v)
					v.d = u.d + w(u, v)
					v.pi = u
```





## Dynamic Programming

```pseudocode
"""Procedure of Dynamic Programming
Characterize the structure of an optimal solution
Recusively define the value of an optimal solution
Compute the value of an optimal solution, typically in a bottom-up fashion
Construct an optimal solution from computed information
"""
```





