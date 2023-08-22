'''
Desenvolver um programa que leia um número n qualquer menor ou igual a 50 e apresente o valor obtido da multiplicação sucessiva de n por 3 enquanto o produto for menor que 250. (n x 3; n x 3 x 3; n x 3 x 3 x 3 etc...).
'''

conta = int(input("Insira aqui um número menor que 50:"))


if (conta <= 50):
    while ( conta < 250):
        print(f"O número {conta} multiplicado por 3 até que não seja menor do que 250 é: {conta * 3}")
        conta = conta * 3

else:
    print(f"{conta} não é menor ou igual a 50")
