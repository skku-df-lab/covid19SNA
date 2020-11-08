## Centrality

#### Add Modules
<pre>
<code>
import networkx as nx
import pandas as pd
</code>
</pre>

#### Centrality
<pre>
<code>

G = nx.Graph()

df = pd.read_excel('../Weight/IDEweight.xlsx')
degree = 100

for i in range(0, degree):
    for j in range(0, degree):
        if df.iloc[i, j] != 0:
            if i != j:
                w = df.iloc[i, j] / 100000000000000   # To normalize the weight, divided by 100000 billion.
                G.add_edge(i+1, j+1, weight=w)
                print("i: ", i, "j: ", j, "weight: ", df.iloc[i, j])

print("== DEGREE centrality with weight")
print(nx.degree_centrality(G))

print("== CLOSENESS centrality with weight")
print(nx.closeness_centrality(G, distance='weight'))

print("== BETWEENNESS centrality with weight")
print(nx.betweenness_centrality(G, weight='weight'))
</code>
</pre>


