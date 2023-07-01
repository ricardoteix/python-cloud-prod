import boto3

def criar_instancia_ec2():
   
   # Defina a região em que deseja criar a instância
    regiao = 'us-east-1'
    
    # Crie uma sessão do Boto3 usando suas credenciais
    session = boto3.Session(
        region_name=regiao
    )
    
    # Crie um cliente EC2 usando a sessão
    ec2_client = session.client('ec2')
    
    # Crie a instância EC2
    instancia = ec2_client.run_instances(
        ImageId='ami-0dba2cb6798deb6d8',
        InstanceType='t3a.micro',
        MinCount=1,
        MaxCount=1
    )
    
    # Obtenha o ID da instância criada
    instancia_id = instancia['Instances'][0]['InstanceId']
    
    print(f'Instância EC2 criada com sucesso. ID: {instancia_id}')

# Chame a função para criar a instância EC2
criar_instancia_ec2()
