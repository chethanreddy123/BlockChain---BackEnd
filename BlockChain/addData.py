from pymongo.mongo_client import MongoClient

client = MongoClient('mongodb+srv://chethanreddy2002:12345@cluster0.xihwp.mongodb.net/?retryWrites=true&w=majority')

Data = client['SampleApp']
myData = Data['userData']

myData.insert_one({
    "Name" : "A Chethan"
})


