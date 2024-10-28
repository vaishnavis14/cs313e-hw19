class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex(object):
  def __init__(self, label):
    self.label = label
    self.visited = False

  def was_visited(self):
    return self.visited

  def get_label(self):
    return self.label

  def __str__(self):
    return str(self.label)

class Graph(object):
  def __init__(self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex(self, label):
    nVert = len(self.Vertices)
    for i in range(nVert):
        if label == self.Vertices[i].get_label():
            return True
    return False

  def get_index(self, label):
    nVert = len(self.Vertices)
    for i in range(nVert):
      if label == self.Vertices[i].get_label():
        return i
    return -1

  # add a vertex with a given label to the graph
  def add_vertex(self, label):
    if self.has_vertex(label):
      return
    # add a vertex to the list of vertices
    self.Vertices.append(Vertex(label))

    # add a column to the adjacency matrix
    nVert = len(self.Vertices)
    for i in range(nVert - 1):
      (self.adjMat[i]).append(0)

    # add a new row for the new vertex
    new_row = []
    for i in range(nVert):
      new_row.append(0)
    self.adjMat.append(new_row)

  # add weighted directed edge to the graph
  # start and finish are indexes
  def add_directed_edge(self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  def add_undirected_edge(self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an univisited vertex adjacent to vertex v (which is an index)
  def get_adj_unvisited_vertex(self, v):
    nVert = len(self.Vertices)
    for i in range(nVert):
      if self.adjMat[v][i] > 0 and (not self.Vertices[i].was_visted()):
        return i
    return -1

  def dfs(self, v):
    theStack = Stack()

    # mark the vartex v as visited and push to the Stack
    self.Vertices[v].visited = True
    print(self.Vertices[v])
    theStack.push(v)

    # if all the other vertices according to depth
    while not theStack.isEmpty():
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex(theStack.peek())
      if u == -1:
        u = theStack.pop()
      else:
        self.Vertices[u].visited = True
        print(self.Vertices[u])
        theStack.push(u)
    nVert = len(self.Vertices)
    for i in range(nVert):
      self.Vertices[i].visited = False