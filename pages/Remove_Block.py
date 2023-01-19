import streamlit as st
from pymongo.mongo_client import MongoClient
import blockchain as _blockchain
import requests
import json 

st.sidebar.title('Developer\'s Contact')
st.sidebar.markdown('[![Chethan-Reddy]'
                  '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                  '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)') 

st.sidebar.success("Guided By Vijaya Priay R")

st.title("📈 You can remove your Exsisting Block from the chain")



client = MongoClient("mongodb://chethanreddy123:1234@ac-wspz9tf-shard-00-00.dix8btt.mongodb.net:27017,ac-wspz9tf-shard-00-01.dix8btt.mongodb.net:27017,ac-wspz9tf-shard-00-02.dix8btt.mongodb.net:27017/?ssl=true&replicaSet=atlas-f8in3c-shard-0&authSource=admin&retryWrites=true&w=majority") 
msg_collection = client['BlockChainData']['BlockData']

x = msg_collection.find()

ListOfNode = []
ListOfId = []

ListOfData = []

for i in x:
    del i['_id']
    ListOfNode.append(i["Node_Name"])
    ListOfId.append(i["Node_Id"])



col1, col2 = st.columns(2)

with col1:
    with st.form('Form1'):
        ans1 = st.selectbox('Search by Node Name', ListOfNode)
        submitted1 = st.form_submit_button('Search Name')

with col2:
    with st.form('Form2'):
        ans2 = st.selectbox('Search by Node ID', ListOfId)
        submitted2 = st.form_submit_button('Search ID')

if submitted1 == True:
    data = msg_collection.delete_one({"Node_Name" : ans1})
    st.success("Your Node has been successfully added to the chain")
    st.write("Below is the information of the block recently added:")
    st.json(data)

elif submitted2 == True:
    data = msg_collection.delete_one({"Node_Id" : ans2})
    print(data.raw_result)
    st.success("Your Node has been successfully added to the chain")
    st.write("Below is the information of the block recently added:")
    st.json(data.raw_result)

