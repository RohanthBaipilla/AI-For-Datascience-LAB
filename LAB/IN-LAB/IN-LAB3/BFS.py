graph = {
  'A' : ['B','C','D'],
  'B' : ['E', 'F'],
  'C' : [],
  'D' : ['G','H','I'],
  'E' : ['J'],
  'F' : ['K'],
  'G' : ['L'],
  'H' : [],
  'I' : [],
  'J' : [],
  'K' : [],
  'L' : []
}
print("BFS Follows the Queue -- FIFO")
visited = []
queue = []
def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Breadth-First Search order is : ")
bfs(visited, graph ,'A')