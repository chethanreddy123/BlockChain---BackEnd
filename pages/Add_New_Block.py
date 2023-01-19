import streamlit as st
from pymongo.mongo_client import MongoClient
import requests
import json 

import time

st.sidebar.title('Developer\'s Contact')
st.sidebar.markdown('[![Chethan-Reddy]'
                  '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                  '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)') 

st.sidebar.success("Guided By Vijaya Priay R")

st.title("🆕 Adding new Block into the System - New Node to the chain")




form = st.form(key="my-form")
c1, c2, c3, c4 = st.columns(4)
with c1:
    Node_Name = form.text_input("Enter the name of node: ")
with c2:
    Node_Id = form.text_input("Enter the node ID: ")
with c3:
    x_cor = form.text_input("Enter the x - coordinate: ")
with c4:
    y_cor = form.text_input("Enter the y - coordinate: ")

check = form.form_submit_button("Add the Node to the Chain")

my_bar = st.progress(0)
my_bar.progress(10)
time.sleep(0.1)


if check == True:
    block = {
        "Node_Name" : Node_Name,
        "Node_Id" : Node_Id,
        "x_cor" : x_cor,
        "y_cor" : y_cor
    }
    my_bar.progress(10)
    my_bar.progress(60)
    time.sleep(1)
    my_bar.progress(100)
    if False:
        st.warning("The blockchain is invalid and there is some error!!")
    else:
        CurrData = {"data" : block}
        url = 'http://127.0.0.1:8000/add_new_block/'
        json_object = json.dumps(CurrData, indent = 4) 
        x = requests.post(url, data = json_object)
        print(x)
        print("Hello")
        st.success("Your Node has been successfully added to the chain")
        st.write("Below is the information of the block recently added:")
        st.json(block)

