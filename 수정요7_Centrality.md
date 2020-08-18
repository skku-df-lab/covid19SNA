## Centrality

#### 필요한 모듈 추가
<pre>
<code>
import networkx as nx
import pandas as pd
</code>
</pre>

#### 중심성
<pre>
<code>
"""
- graph로부터 다음 세 가지 centrality와 pagerank를 계산하여 딕셔너리로 리턴해주는 함수
    - weighted degree centrality
    - closeness centrality
    - betweenness centrality
    - pagerank
"""

def return_centralities_as_dict(input_g):
    # weighted degree centrality를 딕셔너리로 리턴
    def return_weighted_degree_centrality(input_g, normalized=False):
        w_d_centrality = {n:0.0 for n in input_g.nodes()}
        for u, v, d in input_g.edges(data=True):
            w_d_centrality[u]+=d['weight']
            w_d_centrality[v]+=d['weight']
        if normalized==True:
            weighted_sum = sum(w_d_centrality.values())
            return {k:v/weighted_sum for k, v in w_d_centrality.items()}
        else:
            return w_d_centrality
    def return_closeness_centrality(input_g):
        new_g_with_distance = input_g.copy()
        for u,v,d in new_g_with_distance.edges(data=True):
            if 'distance' not in d:
                d['distance'] = 1.0/d['weight']
        return nx.closeness_centrality(new_g_with_distance, distance='distance')
    def return_betweenness_centrality(input_g):
        return nx.betweenness_centrality(input_g, weight='weight')
    def return_pagerank(input_g):
        return nx.pagerank(input_g, weight='weight')
    return {
        'weighted_deg':return_weighted_degree_centrality(input_g),
        'closeness_cent':return_closeness_centrality(input_g),
        'betweeness_cent':return_betweenness_centrality(input_g),
        'pagerank':return_pagerank(input_g)
    }

"""
main code, 나중에 사용할 때 아래 부분은 삭제하는 것이 좋음. 
"""
G = nx.Graph()

df = pd.read_excel('../Weight/IDEweight.xlsx')
degree = 100

for i in range(0, degree):
    for j in range(0, degree):
        if df.iloc[i, j] != 0:
            if i != j:
                w = df.iloc[i, j]
                G.add_edge(i+1, j+1, weight=w)
                print("i: ", i, "j: ", j, "weight: ", df.iloc[i, j])

nx.draw_networkx(G)
 #plt.axis('off')
 #plt.savefig('sample_graph_for_centrality.svg')

result = []
for k, v in return_centralities_as_dict(G).items():
    result.append("{}: {}".format(k, v))


output = pd.DataFrame(result)
output.to_excel('Centrality.xlsx', index=False)
</code>
</pre>

#### 결과 예시

