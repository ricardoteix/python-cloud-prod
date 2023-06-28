import boto3

sessao = boto3.Session(
	profile_name='python-cloud-prod', 
	region_name='us-east-1'
)
s3_client = sessao.client('s3')
lista = s3_client.list_buckets()
print(lista)
