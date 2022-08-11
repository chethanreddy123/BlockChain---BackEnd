import time
import random
import networkx as nx
import streamlit as st
import requests
import json 

G = nx.Graph()


information = ""



st.set_page_config(layout="wide")
st.title('Logging in Text Box')
logtxtbox = st.empty()
logtxt = 'start'
logtxtbox.text_area("Logs Display: ",logtxt, height = 500)

end_of_loop = False
counter = 1



class Node:

    def __init__(self, name, information , Pointer , Connections, Position):
        self.name = name
        self.information = information
        self.Pointer = Pointer
        self.Connections = Conncetions
        self.Position = Position

        G.add_node(self.name , pos = self.Position)

        for nodes in Connections:
            G.add_edge(self.name , nodes[0], weight = nodes[1])


    def RandomPointer(self):
        return random.randint(1,3)
        

class Conncetions:
    def __init__(self, NodeList = None, ConncetionsList = None):
        self.NodeList = NodeList
        self.ConncetionsList = ConncetionsList

    def Loop(self):
        while True:
            CurrPointers = []

            global information


            for Node in self.NodeList:
                CurrTrigger = Node.RandomPointer()
                Node.information = "Node " +  str(Node.name) + " Triggering " + str(CurrTrigger) + " Node"
                Node.Pointer = CurrTrigger
                information += (str(Node.information) + "\n")
                print(Node.information)
                logtxtbox.text_area("Logging: ", information, height=500)
                CurrPointers.append(CurrTrigger)
            


            FreqDict = {}
            for i in CurrPointers:
                if i in FreqDict:
                    FreqDict[i] += 1
                else:
                    FreqDict[i] = 0

            print(FreqDict)

            if len(FreqDict) == 1:
                information += (str("All Nodes triggered Adding Data To Block Chain") + "\n")
                logtxtbox.text_area("Logging: ", information, height=500)
                url = 'http://127.0.0.1:8000/mine_block/'

                myobj = {'data': str(time.ctime(time.time())) +" " + str(FreqDict) }
                json_object = json.dumps(myobj, indent = 4) 
                x = requests.post(url, data = json_object)
                
                print(x.text)
                print("yes")
                time.sleep(5)


'''

Node1 = Node("Frist")
Node2 = Node("Second")
Node3 = Node("Thrid")
Node4 = Node("Four")
Node5 = Node("Five")


L = [Node1,Node2,Node3,Node4,Node5]

MainConnection = Conncetions(L)

MainConnection.Loop()

'''