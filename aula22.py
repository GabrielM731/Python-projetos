# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada
# naquele valor
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor
entrada = input ('[E]ntrar [S]air: ')
senha_digitada =  input('Senha: ')

senha_permitida = '123456'
# O if checa a primeira condição 'entrada' -> Se for True ele passa para a outra
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
     print('Entrar')
else:
     print('Sair')

# Avaliação de 'CURTO CIRCUITO' - O Python finaliza e retorna o ultimo valor VERDADEIRO/True
'''print (0 or False or 0 or 'abc' or True)'''
senha = input ('Senha: ') or 'Sem senha'

print (senha)