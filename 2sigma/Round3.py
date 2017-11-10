#Two Sigma's mission is to uncover value in the world's data, and as part of that
#it's necessary to download massive amounts of information on a regular basis.' \
 # ' Naturally, this data should be transferred as quickly and efficiently as possible.

#A new data resource was recently added to the network, and your job is to establish a connection between it
#and Two Sigma's server. Due to security reasons, all connections in Two Sigma's network are unidirectional (i.e.
## only have a one-way connection), and no data can be stored on any node of the network. This means that every second
## the amount of data a node receives should be equal to the amount of data it forwards. The only exceptions to this
## rule are resource and server, since the former only sends data while the latter only receives it.

#Unfortunately, some segments of the network are slower than is ideal due to limitations with legacy telecommunication
# operators around the world. This complicates finding the optimal route through the network significantly, which is why
#  your help is required.

#Find a route between the resource and the server that maximizes the amount of data downloaded in a second,
#and return this maximum value.

#Example

#For resource = 4, server = 5 and

'''network = [[0, 2, 4, 8, 0, 0],
           [0, 0, 0, 9, 0, 0],
           [0, 0, 0, 0, 0, 10],
           [0, 0, 6, 0, 0, 10],
           [10, 10, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]
the output should be dataRoute(resource, server, network) = 19.'''



resource = 4
server = 5

network = [[0, 2, 4, 8, 0, 0],
           [0, 0, 0, 9, 0, 0],
           [0, 0, 0, 0, 0, 10],
           [0, 0, 6, 0, 0, 10],
           [10, 10, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]



class Edge(object):
  def __init__(self, u, v, w):
    self.source = u
    self.target = v
    self.capacity = w

  def __repr__(self):
    return "%s->%s:%s" % (self.source, self.target, self.capacity)


class FlowNetwork(object):
  def  __init__(self):
    self.adj = {}
    self.flow = {}

  def AddVertex(self, vertex):
    for key in vertex:
        self.adj[key] = []

  def GetEdges(self, v):
    return self.adj[v]

  def AddEdge(self, u, v, w = 0):
    if u == v:
      raise ValueError("u == v")
    edge = Edge(u, v, w)
    redge = Edge(v, u, 0)
    edge.redge = redge
    redge.redge = edge
    self.adj[u].append(edge)
    self.adj[v].append(redge)
    # Intialize all flows to zero
    self.flow[edge] = 0
    self.flow[redge] = 0

  def FindPath(self, source, target, path):
    if source == target:
      return path
    for edge in self.GetEdges(source):
      residual = edge.capacity - self.flow[edge]
      if residual > 0 and not (edge, residual) in path:
        result = self.FindPath(edge.target, target, path + [(edge, residual)])
        if result != None:
          return result

  def MaxFlow(self, source, target):
    path = self.FindPath(source, target, [])
    while path != None:
      flow = min(res for edge, res in path)
      for edge, res in path:
        self.flow[edge] += flow
        self.flow[edge.redge] -= flow
      path = self.FindPath(source, target, [])
    return sum(self.flow[edge] for edge in self.GetEdges(source))


def dataRoute(resource, server, network):
    g = FlowNetwork()
    lst = []
    for l in range(0,len(network)):
        lst.append(l)
    g.AddVertex(lst)
    for i in range(len(network)):
        for j in range(len(network)):
            if j != i:
                g.AddEdge(i, j,network[i][j])
    print(g.MaxFlow(resource, server))


dataRoute(resource, server, network)
