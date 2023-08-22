'''
Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um expoente qualquer (Variável e), ou seja, de b^e. (Sem usar Math.pow();)
'''


b = float(input("Insira aqui a base:"))
e = float(input("Insira aqui a potência do número:"))

# usuário -> b = 3, e = 4
# no papel -> 3 * 3 * 3 * 3

conta = b**e

print(f"A conta da base {b:.0f} elevada a potência {e:.0f}  é: {conta:.0f}")