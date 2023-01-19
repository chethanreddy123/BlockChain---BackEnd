import streamlit as st
import base64
import requests
from pymongo.mongo_client import MongoClient

st.sidebar.title('Developer\'s Contact')
st.sidebar.markdown('[![Chethan-Reddy]'
                  '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                  '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)') 

st.sidebar.success("Guided By Dr.Vijaya Priya R")

URL = "http://127.0.0.1:8000/validate/"
r = requests.get(url = URL)

data1 = r.json()



URL = "http://127.0.0.1:8000/blockchain/last/"
r = requests.get(url = URL)

data2 = r.json()

print(data2)


st.title("Welcome to the Smart Grid Peer to Peer Energy ⚡ transaction with Blockchain security ⚛️")


st.markdown(
    """
    This is an open-source application framework built specifically for
    peer to peer energy transaction with super secure blockchain.
    **👈 Select a specific option from the sidebar** to see some of the features
    of what can do!
   
"""
)

st.subheader("The Block Chain Parameters:")

client = MongoClient("mongodb://chethanreddy123:1234@ac-wspz9tf-shard-00-00.dix8btt.mongodb.net:27017,ac-wspz9tf-shard-00-01.dix8btt.mongodb.net:27017,ac-wspz9tf-shard-00-02.dix8btt.mongodb.net:27017/?ssl=true&replicaSet=atlas-f8in3c-shard-0&authSource=admin&retryWrites=true&w=majority")
msg_collection = client['BlockChainData']['TestData']

x = msg_collection.find()
ListOfData = []
for i in x:
    del i['_id']
    ListOfData.append(i)

data3 = len(ListOfData)


col1, col2, col3 = st.columns(3)
col1.metric("Number of block:", str(data3), "+1 Node")
col2.metric("The Last Block:", str(data2['data']), "Added")
col3.metric("Validity of the chain:",str(data3), "Yes")

file_ = open("blockimage.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="Block Chain GIF">',
    unsafe_allow_html=True,
)