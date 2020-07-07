## Graph : Weighted Graph

#### 필요한 모듈 추가
<pre>
<code>
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
</code>
</pre>

#### 시간별 최단 경로 그래프를 만드는 작업
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

"""
G.add_edge('a', 'b', weight=0.6)
G.add_edge('a', 'c', weight=0.2)
G.add_edge('c', 'd', weight=0.1)
G.add_edge('c', 'e', weight=0.7)
G.add_edge('c', 'f', weight=0.9)
G.add_edge('a', 'd', weight=0.3)
"""

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

### 시간별 그래프 생성 결과 예시
issue에 그림들 올린 후, 링크들 가져오기
###### Initial Graph, 13:00
사진1
###### Extended Graph, 12:30
사진2
###### Extended Graph, 12:00
사진3
###### Extended Graph, 11:30
사진4
###### Extended Graph, 11:00
사진5
###### Extended Graph, 10:30
사진6
###### Extended Graph, 10:00
사진7
###### Extended Graph, 09:30
사진8
###### Extended Graph, 09:00
사진9
