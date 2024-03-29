import fastapi as _fastapi 
import blockchain as _blockchain
from fastapi import Request


from pymongo.mongo_client import MongoClient
# comment

blockchain = _blockchain.Blockchain()
app = _fastapi.FastAPI()


# endpoint to mine a block
@app.post("/mine_block/")
async def mine_block(info : Request):
    req_info = await info.json()
    data1 = req_info['data']
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
    block = blockchain.mine_block(data=data1)

    with MongoClient("mongodb://chethanreddy123:1234@ac-wspz9tf-shard-00-00.dix8btt.mongodb.net:27017,ac-wspz9tf-shard-00-01.dix8btt.mongodb.net:27017,ac-wspz9tf-shard-00-02.dix8btt.mongodb.net:27017/?ssl=true&replicaSet=atlas-f8in3c-shard-0&authSource=admin&retryWrites=true&w=majority") as client:
        msg_collection = client['BlockChainData']['TestData']
        result = msg_collection.insert_one(dict(block))
        ack = result.acknowledged


    return block


# endpoint to return the blockchain
@app.get("/blockchain/")
def get_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
    chain = blockchain.chain
    with MongoClient("mongodb://chethanreddy123:1234@ac-wspz9tf-shard-00-00.dix8btt.mongodb.net:27017,ac-wspz9tf-shard-00-01.dix8btt.mongodb.net:27017,ac-wspz9tf-shard-00-02.dix8btt.mongodb.net:27017/?ssl=true&replicaSet=atlas-f8in3c-shard-0&authSource=admin&retryWrites=true&w=majority") as client:
        msg_collection = client['BlockChainData']['TestData']
        chain[0]['_id'] = 1
        result = msg_collection.insert_one(chain[0])
        ack = result.acknowledged
    return chain[0]

# endpoint to see if the chain is valid
@app.get("  ")
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