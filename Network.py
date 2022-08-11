import GraphData
import streamlit as st
import matplotlib.pyplot as plt

N1 = GraphData.Node(1 , "None" , 1 , [(2,"1 Km") , (3,"1 Km")] , (1,1))
N2 = GraphData.Node(2 , "None" , 2 , [(1,"1 Km") , (3,"1 Km")] , (2,1))
N3 = GraphData.Node(3 , "None" , 3 , [(2,"1 Km") , (1,"1 Km")] , (3,3))



Connections = GraphData.Conncetions([N1,N2,N3])


st.title('Triggering Power Switches')




fig, ax = plt.subplots()
pos=GraphData.nx.get_node_attributes(GraphData.G,'pos')
GraphData.nx.draw(GraphData.G,pos , with_labels = True)
labels = GraphData.nx.get_edge_attributes(GraphData.G,'weight')
GraphData.nx.draw_networkx_edge_labels(GraphData.G,pos,edge_labels=labels)
st.pyplot(fig)

Connections.Loop()
