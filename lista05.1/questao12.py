'''
Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem como maior, nem como menor, e nem na contagem da média.
'''

a = float(input("Insira aqui o primeiro número (-1 encerra a inserção.):"))
maior = a
menor = a
tot_resp = 0
acumulador = 0


while (a != -1):
    tot_resp = tot_resp + 1
    acumulador = acumulador + a
    if (maior < a):
        maior = a

    if (menor > a):
        menor = a
    a = float(input("Insira aqui mais um número (-1 encerra a inserção.):"))

media = acumulador / tot_resp

if (maior == -1):
    print(f"O número inserido não permite a continuação do programa.\nPrograma encerrado!")

else:
    print(f"Maior valor inserido: {maior}")
    print(f"Menor valor inserido: {menor}")
    print(f"Total de respostas: {tot_resp}")
    print(f"Média: {media}")
    print("FIM DO PROGRAMA")

