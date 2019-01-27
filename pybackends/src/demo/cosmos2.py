import azure.cosmos.cosmos_client as cosmos_client

'mongodb://dougfooaccount:v9OCE0pGtEhPtRmZFiviZt7iLQovOVpuf5Vtr0ZzxHD3z0mcjTM9aoo31Jdf1ayW8smVT5hdY24CmHwYoSEhcg==@dougfooaccount.documents.azure.com:10255/?ssl=true&replicaSet=globaldb'
config = {
    'ENDPOINT': 'https://dougfooaccount.documents.azure.com:443/',
    'PRIMARYKEY': 'v9OCE0pGtEhPtRmZFiviZt7iLQovOVpuf5Vtr0ZzxHD3z0mcjTM9aoo31Jdf1ayW8smVT5hdY24CmHwYoSEhcg==',
    'DATABASE': 'Test',
    'CONTAINER': 'T1'
}

# Initialize the Cosmos client
client = cosmos_client.CosmosClient(url_connection=config['ENDPOINT'], auth={
                                    'masterKey': config['PRIMARYKEY']})

# Create container options
options = {
    'offerThroughput': 400
}

container_definition = {
    'id': config['CONTAINER']
}


# Query these items in SQL
query = {'query': 'SELECT * FROM server s'}

options = {}
options['enableCrossPartitionQuery'] = True
options['maxItemCount'] = 2

dblink = 'https://dougfooaccount.documents.azure.com:443/'

result_iterable = client.QueryItems(dblink, query, options)
for item in iter(result_iterable):
    print(item['message'])
