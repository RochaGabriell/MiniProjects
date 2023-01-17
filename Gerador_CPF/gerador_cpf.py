from random import randint

str_cpf = str(randint(100000000, 999999999))

# Faz a separação dos "." e "-".
cpf = list(map(int, str_cpf))

# Validação do primeiro dígito
soma_01 = 0
desc_01 = 10

for i in range(0, 9):
    soma_01 += cpf[i] * desc_01
    desc_01 -= 1

verificar_01 = (soma_01 * 10) % 11
cpf.append(verificar_01)

# Se o resto da divisão for igual a 10, nós o consideramos como 0.
if verificar_01 == 10:
    #verificar_01 = 0
    cpf[9] = 0
    

# Validação do segundo dígito
if verificar_01 == cpf[9] or verificar_01 == 10:
    soma_02 = 0
    desc_02 = 11

    for i in range(0, 10):
        soma_02 += cpf[i] * desc_02
        desc_02 -= 1
    
    verificar_02 = (soma_02 * 10) % 11
    cpf.append(verificar_02)
    cpf_str = "".join(map(str, cpf))

def converte_str(cpf:list) -> str:
    cpf_n = ''
    for i in cpf:
        cpf_n += str(i)
    return cpf_n

cpf_str = converte_str(cpf)

cpf_new = cpf_str[0:3] + "." + cpf_str[3:6] + "." + cpf_str[6:9] + "-" + cpf_str[9:11]

print(f"CPF - {cpf_new}")