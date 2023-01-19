import streamlit as st
from pymongo.mongo_client import MongoClient
import blockchain as _blockchain
import requests
import json 
import base64

st.sidebar.title('Developer\'s Contact')
st.sidebar.markdown('[![Chethan-Reddy]'
                  '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                  '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)') 

st.sidebar.success("Guided By Vijaya Priay R")

st.title("🚀 You View the Whole block Chain Part By Part")

client = MongoClient("mongodb://chethanreddy123:1234@ac-wspz9tf-shard-00-00.dix8btt.mongodb.net:27017,ac-wspz9tf-shard-00-01.dix8btt.mongodb.net:27017,ac-wspz9tf-shard-00-02.dix8btt.mongodb.net:27017/?ssl=true&replicaSet=atlas-f8in3c-shard-0&authSource=admin&retryWrites=true&w=majority")
msg_collection = client['BlockChainData']['TestData']




col1, col2 = st.columns(2)

with col1:
    with st.form('Give The starting Block number'):
        start = int(st.number_input("Enter the Number of Blocks you want to view", min_value=1))
        submitted1 = st.form_submit_button('Start Block-Chain ID')
with col2:
    with st.form('Give the End Block number'):
        end = int(st.number_input("Enter the Number of Blocks you want to view", min_value=5))
        submitted2 = st.form_submit_button('End Block-Chain ID')


x = msg_collection.find()
ListOfData = []
for i in x:
    del i['_id']
    ListOfData.append(i)

if submitted2 == True or submitted1 == True:
    ListOfCol = st.columns(end - start)

    for i in range(len(ListOfCol)):
        col = ListOfCol[i]
        currData = ListOfData[i-1]
       
        st.header(currData['proof'])
        st.metric(label=currData["previous_hash"], value=currData['data'], delta="+1 Node")
        file_ = open("blockimage.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="Block Chain GIF">',
            unsafe_allow_html=True,
        )

        st.write("↓↓")
        st.write("↓↓")
        st.write("↓↓")


