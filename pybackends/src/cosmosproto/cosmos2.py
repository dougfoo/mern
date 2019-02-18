import azure.cosmos.cosmos_client as cosmos_client
import sys

# if (len(sys.argv)) != 2:
#     print('need db/container name as arg')
#     sys.exit()
# name = sys.argv[1]

'mongodb://dougfooaccount:v9OCE0pGtEhPtRmZFiviZt7iLQovOVpuf5Vtr0ZzxHD3z0mcjTM9aoo31Jdf1ayW8smVT5hdY24CmHwYoSEhcg==@dougfooaccount.documents.azure.com:10255/?ssl=true&replicaSet=globaldb'

config = {
    'ENDPOINT': 'https://dougfooaccount.documents.azure.com:443/Test',
    'PRIMARYKEY': 'v9OCE0pGtEhPtRmZFiviZt7iLQovOVpuf5Vtr0ZzxHD3z0mcjTM9aoo31Jdf1ayW8smVT5hdY24CmHwYoSEhcg==',
    'DATABASE': 'Test',
    'CONTAINER': 'T1'
}

# Initialize the Cosmos client
client = cosmos_client.CosmosClient(url_connection=config['ENDPOINT'], auth={
                                    'masterKey': config['PRIMARYKEY']})

# Query these items in SQL
query = {'query': 'SELECT * FROM server s'}

options = {}
options['enableCrossPartitionQuery'] = True
options['maxItemCount'] = 2
options['offerThroughput'] = 400


dblink = 'https://dougfooaccount.documents.azure.com:443/Test'

result_iterable = client.QueryItems('dbs/T1', query, options)
for item in iter(result_iterable):
    print(item['message'])
