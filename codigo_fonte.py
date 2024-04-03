secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")
n1 = int(input("Digite um numero: "))

while n1 != secret_number:
    print("Ha ha! Você está preso no meu loop!")
    secret_number == n1

print("Muito bem, trouxa! Você está livre agora.")