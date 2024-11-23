from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    visited.add(start)

    while queue:
        vertex=queue.popleft()
        print(vertex,end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
if __name__=="__main__":
    graph={
        'a':['b','c'],
        'b':['c','a'],
        'c':['a','b']
        }
    print("bfs start from root node a")
    bfs(graph,'a')
