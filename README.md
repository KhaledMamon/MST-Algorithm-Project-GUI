
Project Title: Minimum Spanning Tree (MST) Visualization
Course: CS315 - Algorithm Analysis and Design

Group Members:
1. Khaled Gamal - ID: [Your ID]
2. [Student Name] - ID: [ID]
3. [Student Name] - ID: [ID]


Files Description:
- algorithm1.py: Contains the Naive solution implementation (using DFS for cycle detection).
- algorithm2.py: Contains the Optimized solution implementation (using Union-Find data structure).
- main_gui.py: The main application file. It provides a Graphical User Interface (GUI) to visualize the buildings, execute both algorithms, and compare their performance in real-time.
- Final_Report.pdf: Comprehensive documentation of the project.
-----------------------------------------------------------------------------------------------

1. Pseudocode for Algorithm 1: Naive Approach
Description: This algorithm sorts all edges by weight and iterates through them. Before adding an edge to the MST, it performs a Depth First Search (DFS) traversal on the current tree to check if a path already exists between the two endpoints. If a path exists, the edge is discarded to prevent a cycle.

  FUNCTION HasPathDFS(Graph, CurrentNode, TargetNode, VisitedSet):
    IF CurrentNode == TargetNode:
        RETURN True
    
    Add CurrentNode to VisitedSet
    
    FOR each Neighbor in Graph[CurrentNode]:
        IF Neighbor is NOT in VisitedSet:
            IF HasPathDFS(Graph, Neighbor, TargetNode, VisitedSet):
                RETURN True
    
    RETURN False

FUNCTION NaiveMST(Vertices, Edges):
    // Step 1: Sort all edges in non-decreasing order of their weight
    Sort Edges by weight
    
    MST_Set = Empty List
    Current_Graph = Empty Adjacency List
    Edge_Count = 0
    
    // Step 2: Iterate through sorted edges
    FOR each edge (u, v, weight) in Edges:
        // Stop if we have selected V-1 edges
        IF Edge_Count == Total_Vertices - 1:
            BREAK
            
        // Step 3: Cycle Detection using DFS (The "Naive" part)
        Initialize VisitedSet as Empty
        HasCycle = HasPathDFS(Current_Graph, u, v, VisitedSet)
        
        IF HasCycle is False:
            Add (u, v, weight) to MST_Set
            Add v to Current_Graph[u]
            Add u to Current_Graph[v]
            Edge_Count = Edge_Count + 1
            
    RETURN MST_Set, CalculateTotalCost(MST_Set)

------------------------------------------------------------------------------------------------

2. Pseudocode for Algorithm 2: Optimized Approach
Description: This algorithm also sorts edges by weight but uses the Disjoint Set Union (DSU) or Union-Find data structure to detect cycles efficiently. It checks if the two endpoints of an edge belong to the same set. If they do not, it unions the sets and adds the edge. This reduces the cycle check complexity to nearly constant time.

STRUCTURE UnionFind:
    Parent Array
    Rank Array

    FUNCTION Initialize(N):
        FOR i from 0 to N-1:
            Parent[i] = i
            Rank[i] = 0

    FUNCTION Find(i):
        // Path Compression: Point node directly to root
        IF Parent[i] != i:
            Parent[i] = Find(Parent[i])
        RETURN Parent[i]

    FUNCTION Union(i, j):
        RootI = Find(i)
        RootJ = Find(j)
        
        IF RootI != RootJ:
            // Union by Rank: Attach smaller tree to larger tree
            IF Rank[RootI] > Rank[RootJ]:
                Parent[RootJ] = RootI
            ELSE IF Rank[RootI] < Rank[RootJ]:
                Parent[RootI] = RootJ
            ELSE:
                Parent[RootJ] = RootI
                Rank[RootI] = Rank[RootI] + 1
            RETURN True  // Successful union (No cycle)
        
        RETURN False // Cycle detected

FUNCTION OptimizedMST(Vertices, Edges):
    // Step 1: Sort all edges in non-decreasing order of their weight
    Sort Edges by weight
    
    MST_Set = Empty List
    DSU = Initialize UnionFind(Vertices)
    Edge_Count = 0
    
    // Step 2: Iterate through sorted edges
    FOR each edge (u, v, weight) in Edges:
        IF Edge_Count == Total_Vertices - 1:
            BREAK
            
        // Step 3: Cycle Detection using Union-Find (The "Optimized" part)
        IF DSU.Union(u, v) is True:
            Add (u, v, weight) to MST_Set
            Edge_Count = Edge_Count + 1
            
    RETURN MST_Set, CalculateTotalCost(MST_Set)




  
