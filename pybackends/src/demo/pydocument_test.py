import pydocumentdb
import pydocumentdb.document_client as document_client


url = "mongodb://dougfooaccount:v9OCE0pGtEhPtRmZFiviZt7iLQovOVpuf5Vtr0ZzxHD3z0mcjTM9aoo31Jdf1ayW8smVT5hdY24CmHwYoSEhcg==@dougfooaccount.documents.azure.com:10255/Test?ssl=true&replicaSet=globaldb"

# Initialize the Python Azure Cosmos DB client
client = document_client.DocumentClient(url, {'masterKey': "v9OCE0pGtEhPtRmZFiviZt7iLQovOVpuf5Vtr0ZzxHD3z0mcjTM9aoo31Jdf1ayW8smVT5hdY24CmHwYoSEhcg=="})

# Query them in SQL
query = {'query': 'SELECT * FROM server s'}

options = {}
options['enableCrossPartitionQuery'] = True
options['maxItemCount'] = 2

result_iterable = client.QueryDocuments("T1", query, options)
results = list(result_iterable)

print(results)
