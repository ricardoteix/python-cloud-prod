tags = {
    "Name": "wordpress",
    "Ambiente": "produção",
    "Terraform": True,
    "EBS": 30,
    "meta": []
}
print(tags['Name'])
tags['Name'] = 'NGINX'
print(tags['Name'])
# Forçar extrair uma lista
print( list(tags) )
print( list(tags)[1] )
# print( tags[ list(tags)[1] ] )