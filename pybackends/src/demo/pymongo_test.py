from pymongo import MongoClient

url = "mongodb://dougfooaccount:v9OCE0pGtEhPtRmZFiviZt7iLQovOVpuf5Vtr0ZzxHD3z0mcjTM9aoo31Jdf1ayW8smVT5hdY24CmHwYoSEhcg==@dougfooaccount.documents.azure.com:10255/Test?ssl=true&replicaSet=globaldb"

client = MongoClient(url)

db = client.Test 
col = db.T1

import pprint
pprint.pprint(col.find_one())
