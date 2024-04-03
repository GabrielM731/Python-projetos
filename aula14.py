a = 'AAAAA'
b = 'BBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
    ) 
# isto é um parâmetro nomeado - Quando se tem a variavel com nome
print(formato)