
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.title('Hello Networkx')
st.markdown('Club Graph')


G = nx.Graph()
i = 1

G.add_node(i,pos=(i,i))
G.add_edge(3,4,weight=3.4)
G.add_node(2,pos=(2,3))
G.add_node(3,pos=(3,3))
G.add_node(4,pos=(4,1))
G.add_edge(1,2,weight="0.5 Km")
G.add_edge(1,3,weight=9.8)



fig, ax = plt.subplots()
pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos , with_labels = True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
st.pyplot(fig)