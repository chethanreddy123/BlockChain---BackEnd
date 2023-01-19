import GraphData
import streamlit as st
import matplotlib.pyplot as plt



N1 = GraphData.Node(1 , "None" , 1 , [(2,"1 Km") , (3,"1 Km"), (4 , "1 Km")] , (4,4) , float('inf'))
N2 = GraphData.Node(2 , "None" , 2 , [(1,"1 Km") , (3,"1 Km"), (4 , "1 Km")] , (-4,4), 0)
N3 = GraphData.Node(3 , "None" , 3 , [(2,"1 Km") , (1,"1 Km"), (4 , "1 Km")] , (-4,-4), 0)
N4 = GraphData.Node(4 , "None" , 4 , [(2,"1 Km") , (1,"1 Km"),(3,"1 Km")] , (4,-4), 50)



st.subheader("Node 1 - Renewable Energy Generation System with ID = 4", anchor=None)
st.subheader("Node 2 - Smart Grid System", anchor=None)
st.subheader("Node 3 - Renewable Energy Generation System with ID = 3", anchor=None)
st.subheader("Node 4 - Power Distribution System", anchor=None)


Connections = GraphData.Conncetions([N1,N2,N3])


st.title('Basic Structure of Smart Grid system:')
image = "Grid-Image.png"

st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.warning("For now there only two Distribution Generation System are part of whole smart grid system :)")


fig, ax = plt.subplots()
pos=GraphData.nx.get_node_attributes(GraphData.G,'pos')
GraphData.nx.draw(GraphData.G,pos , with_labels = True)
labels = GraphData.nx.get_edge_attributes(GraphData.G,'weight')
GraphData.nx.draw_networkx_edge_labels(GraphData.G,pos,edge_labels=labels)
st.pyplot(fig)

Connections.Loop()
