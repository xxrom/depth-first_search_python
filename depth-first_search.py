# меньше памяти потребляет чем bfs , по скорости тоже самое
# LIFO, разница между Dfs и Bfs => в dfs используем STACK, а bfs - queue

class Node(object):
  def __init__(self, name):
    self.name = name
    self.adjacenciesList = []
    self.visited = False
    self.predecessor = None

class DepthFirstSearch(object): # BFS -> queue  DFS -> stack
  def dfs(self, node):
    node.visited = True
    print('%s ' % node.name)

    for n in node.adjacenciesList:
      if not n.visited:
        self.dfs(n) # идем дальше в глубь

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjacenciesList.append(node2)
node1.adjacenciesList.append(node3)
node2.adjacenciesList.append(node4)
node4.adjacenciesList.append(node5)

dfs = DepthFirstSearch()

dfs.dfs(node1) # A B D E C
