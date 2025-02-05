from queue import PriorityQueue
v=14
graph=[[] for i in range(v)]
def Best_first_search(intial_state,Goal_state,n):
  visited=[False]*n
  pq=PriorityQueue()
  pq.put((0,intial_state))
  visited[intial_state]=True
  while not pq.empty():
    u=pq.get()[1]
    print(u,end=" ")
    if u==Goal_state:
      break
    for v,c in graph[u]:
      if visited[v]==False:
        visited[v]=True
        pq.put((v,c))
  print()

def addedge(x,y,cost):
  graph[x].append((y,cost))
  graph[y].append((x,cost))
  
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

intial_state=0
Goal_state=9
n=v

Best_first_search(intial_state,Goal_state,n)
