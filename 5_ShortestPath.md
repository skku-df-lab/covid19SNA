## Shortest Path : Dijistra algorithm

#### Add Modules
<pre>
<code>
#dijkstra implementation from MIT 6006 course lesson #16
from collections import defaultdict
import math
from heapq import heapify, heappush, heappop
import pandas as pd
</code>
</pre>

#### utility: priority queue
<pre>
<code>
class Pq:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def insert(self, item):
        heappush(self.queue, item)

    def extract_min(self):
        return heappop(self.queue)[1]

    def update_priority(self, key, priority):
        for v in self.queue:
            if v[1] == key:
                v[0] = priority
        heapify(self.queue)

    def empty(self):
        return len(self.queue) == 0
</code>
</pre>

#### utility: Graph
<pre>
<code>
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(lambda: [])

    def add_edge(self, v, u, w):
        self.graph[v].append((u, w))

    def __str__(self):
        result = ''
        for v in self.V:
            result += f'{v}: {str(self.graph[v])}, \n'
        return result
</code>
</pre>

#### Dijstra algorithm to find the shortest path
<pre>
<code>
def dijkstra(graph, s):
    Q = Pq()  # priority queue of vertices
    # [ [distance, vertex], ... ]
    d = dict.fromkeys(graph.V, math.inf)  # distance pair
    # will have default value of Infinity
    pi = dict.fromkeys(graph.V, None)  # map of parent vertex
    # useful for finding shortest path

    # initialize
    d[s] = 0

    # update priority if prior path has larger distance
    def relax(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            Q.update_priority(v, d[v])
            pi[v] = u

    # initialize queue
    for v in graph.V:
        Q.insert([d[v], v])

    while not Q.empty():
        u = Q.extract_min()
        for v, w in graph.graph[u]:
            relax(u, v, w)

    return d, pi


def shortest_path(s, t):
    d, pi = dijkstra(g, s)
    path = [t]
    current = t

    # if parent pointer is None,
    # then it's the source vertex
    while pi[current]:
        path.insert(0, pi[current])
        # set current to parent
        current = pi[current]

    if s not in path:
        return f'unable to find shortest path staring from "{s}" to "{t}"'

    return f'{" > ".join(path)}'

df = pd.read_excel('../Weight/IDW.xlsx')

degree = 100

snapshot = []
for i in range(degree):
    snapshot.append(str(i+1))

g = Graph(snapshot)

for i in range(0, degree):
    for j in range(0, degree):
        if df.iloc[i, j] != 0:
            if i != j:
                w = df.iloc[i, j]
                g.add_edge(str(i+1), str(j+1), w)
                #print("i: ", i, "j: ", j, "weight: ", df.iloc[i, j])

print(g)
#print(shortest_path('1', '99'))
</code>
</pre>

#### Print shortest path
<pre>
<code>
result = []
for i in range(0, degree):
    for j in range(0, degree):
        if i != j:
            result.append(shortest_path(str(i+1), str(j+1)))
            #print(shortest_path(str(i+1), str(j+1)))

output = pd.DataFrame(result)
output.to_excel('SPresult.xlsx', index=False)
</code>
</pre>

### Results
![shortestPath_SPresult](https://user-images.githubusercontent.com/66988643/86545550-9a09e600-bf6a-11ea-8a87-ebcc0ae60eb9.PNG)


###### From : https://velog.io/@leejh3224/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%BD%94%EB%93%9C-%EC%A0%95%EB%A6%AC-Dijkstra-in-python3-cajoi4a9c3
