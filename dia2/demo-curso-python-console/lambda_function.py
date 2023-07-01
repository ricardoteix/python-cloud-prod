import json
import boto3
import io

from PIL import Image

def lambda_handler(event, context):
    # TODO implement

    image = Image.open('exemplo1.jpg')
    nova = image.resize((500, 175))
    # nova.save("novo_exemplo1.jpg")
    print(image.size)
    print(nova.size)

    # print(event)
    
    s3_client = boto3.client('s3')
    # resposta = s3_client.create_bucket(Bucket='ct-cloud-prod-exemplo-s3-demo2')
    # print(resposta)
        
    # Transforma a nova imagem em bytes
    arquivo = io.BytesIO()
    nova.save(arquivo, format='JPEG')
    arquivo.seek(0)
    
    # Envia a nova imagem para o bucket
    s3_client.upload_fileobj(
        arquivo, 
        Bucket='ct-cloud-prod-exemplo-s3-demo2',
        Key='arquivos/novo_exemplo3.jpg'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Olá do curso Python!')
    }
