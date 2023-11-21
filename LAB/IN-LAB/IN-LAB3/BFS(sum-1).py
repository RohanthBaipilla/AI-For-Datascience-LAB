graph = {
  '1' : ['2','3','4','5'],
  '2' : ['6'],
  '3' : ['6'],
  '4' : ['7'],
  '5' : ['7'],
  '6' : ['8'],
  '7' : ['8'],
  '8' : [],

}

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

print("Following is the Breadth-First Search")
bfs(visited, graph ,'1')