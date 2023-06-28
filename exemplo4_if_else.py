tamanho_ebs = 8 
espaco_livre = 5

# or => ou
# if espaco_livre < 4 or tamanho_ebs < 10:
#     print("Espaço acabando.")
#     print("Temos que aumentar o EBS.")

# and => e
# if espaco_livre == 5 and tamanho_ebs < 10:
#     print("Espaço acabando.")
#     print("Temos que aumentar o EBS.")

# not => negação
print("not True:", not True)
print("not False:", not False)

if not espaco_livre == 5: # se
    print("Espaço acabando.")
    print("Temos que aumentar o EBS.")
else: # senão
    print("O espaço está ok.")

print("Fim do programa")
