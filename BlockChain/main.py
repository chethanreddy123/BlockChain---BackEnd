import fastapi as _fastapi
import blockchain as _blockchain

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

blockchain = _blockchain.Blockchain()
app = _fastapi.FastAPI()


#client = MongoClient("localhost:27017")


# endpoint to mine a block
@app.post("/mine_block/")
def mine_block(data: str):
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
    block = blockchain.mine_block(data=data)
    with MongoClient("localhost:27017") as client:
        msg_collection = client['Test']['Test']
        result = msg_collection.insert_one(dict(block))
        ack = result.acknowledged
    return block


# endpoint to return the blockchain
@app.get("/blockchain/")
def get_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
    chain = blockchain.chain
    #print(chain[0])

    
    with MongoClient("localhost:27017") as client:
        msg_collection = client['Test']['Test']
        result = msg_collection.insert_one(chain[0])
        ack = result.acknowledged
    return chain


# endpoint to see if the chain is valid
@app.get("/validate/")
def is_blockchain_valid():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")

    return blockchain.is_chain_valid()


# endpoint to return the last block
@app.get("/blockchain/last/")
def previous_block():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
        
    return blockchain.get_previous_block()