import json
import boto3

from PIL import Image

def lambda_handler(event, context):
    # TODO implement

    image = Image.open('exemplo1.jpg')
    nova = image.resize((500, 175))
    nova.save("novo_exemplo1.jpg")
    
    # print(event)
    
    # s3_client = boto3.client('s3')
    # resposta = s3_client.create_bucket(Bucket='ct-cloud-prod-exemplo-s3-demo2')
    # print(resposta)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Olá do curso Python!')
    }
