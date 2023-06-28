numeros = [2,3,5,7,8,4,7,8,5,11]

# for item in numeros:
#     print(item)

# for idx, item in enumerate(numeros):
#    print(idx, item)

tags = {
    "Name": "wordpress",
    "Ambiente": "produção",
    "Terraform": True,
    "EBS": 30,
}
for item in tags:
    print(item, tags[item])

print("Fim do código")