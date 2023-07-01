import boto3


# sessao = boto3.Session(
# 	profile_name='python-cloud-prod', 
# 	region_name='us-east-1'
# )
# s3_client = sessao.client('s3')

s3_client = boto3.client('s3')
lista = s3_client.list_buckets()

# print(lista)
# print(lista['Buckets'][6]['Name'])

print('-------------')

# resposta = s3_client.create_bucket(Bucket='ct-cloud-prod-exemplo-s3')
# print(resposta)

for item in lista['Buckets']:
	print(item['Name'])