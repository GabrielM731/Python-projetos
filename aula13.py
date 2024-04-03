nome = 'Gabriel'
altura = 1.70
peso = 95
imc = peso / (altura * altura)
# f - strings = formatação de strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)