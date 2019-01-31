import pymongo
# version 2.8.1 !!??

url = "mongodb://dougfooaccount:v9OCE0pGtEhPtRmZFiviZt7iLQovOVpuf5Vtr0ZzxHD3z0mcjTM9aoo31Jdf1ayW8smVT5hdY24CmHwYoSEhcg==@dougfooaccount.documents.azure.com:10255/Test?ssl=true&replicaSet=globaldb"

client = pymongo.MongoClient(url)

db = client.Test 
col = db.T1

print(db)
print (col)

import pprint
for c in col.find():
    pprint.pprint(c)

c1 = {'id':'my id 3','content':'my lame content'}

posts = db.posts
post = posts.insert_one(c1)
print(post)
for c in posts.find():
    pprint.pprint(c)

    
