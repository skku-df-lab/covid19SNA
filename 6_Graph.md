## Graph : Weighted Graph

#### Add Modules
<pre>
<code>
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
</code>
</pre>

#### Create Graphs Per Hour
<pre>
<code>
df = pd.read_excel('../Weight/IDEweight.xlsx')

G = nx.Graph()

degree = 100

for i in range(0, degree):
    for j in range(0, degree):
        if df.iloc[i, j] != 0:
            if i != j:
                w = df.iloc[i, j]
                G.add_edge(i+1, j+1, weight=w)
                print("i: ", i, "j: ", j, "weight: ", df.iloc[i, j])

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.05]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.05]

 #infected = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.05]

pos = nx.spring_layout(G)  # positions for all nodes
 #nodes
nx.draw_networkx_nodes(G, pos, node_size=300, node_color='y')

 #edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=0.3)
nx.draw_networkx_edges(G, pos, edgelist=esmall, width=0.3, alpha=0.3, edge_color='b', style='dashed')
labels = nx.get_edge_attributes(G, 'weight')
 #nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=2)

 #labels
nx.draw_networkx_labels(G, pos, font_size=7, font_family='sans-serif')
plt.title('Extended Graph - 09:00 am')
plt.axis('off')
plt.show()
</code>
</pre>



