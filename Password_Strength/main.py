def getPasswordStrength(passwords, common_words):
    strengths = []
    for password in passwords:
        if len(password) < 6:
            strengths.append("weak")
        # isdigit(): Retorna True se todos os caracteres na string são dígitos e existe pelo menos um caractere, False caso contrário. Ou seja, se for digitado “123”, isdigit() retorna True , mas se digitar “abc” ou “a23”, retorna False . É uma forma de verificar se a string só contém dígitos.
        # isalpha(): caractere é passado para a função. Internamente, o caractere é convertido em seu valor ASCII para a verificação. Retorna: 1 caso seja uma letra do alfabeto maiúscula, 2 caso seja minúscula, 0 caso não esteja no alfabeto.
        elif password.isdigit() or password.isalpha() and (password.isupper() or password.islower()):
            strengths.append("weak")
        else:
            weak = False
            for word in common_words:
                if word in password or word[::-1] in password:
                    weak = True
                    break
            if weak:
                strengths.append("weak")
            else:
                strengths.append("strong")
    return strengths

n = int(input())
passwords = []
for i in range(0, n):
    passwords.append(str(input()))

m = int(input())
dict_words = []
for i in range(0, m):
    dict_words.append(str(input()))

print('\n'.join(map(str, getPasswordStrength(passwords, dict_words))))