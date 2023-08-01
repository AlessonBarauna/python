inicio = int(input("Digite o número inicial do intervalo:"))
fim = int(input("Digite o número final do intervalo:"))

print(f"números primos no intervalo de {inicio} a {fim}:")
for numero in range(inicio, fim + 1):
    if numero > 1:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                break
        else:
            print(numero)

# nota = int(input("Entre com a nota:"))

# if nota >= 10:
#     print("Você tirou uma nota excelente!")
# elif nota >= 6:
#     print("Você passou!")
# else:
#     print("Você reprovou!")

# frutas = ["maça", "banana", "laranja"]

# for fruta in frutas:
#     print("fruta")

# contador = 0

# while contador < 10:
#     print("Contador ", contador)
#     contador += 1

# numeros = [1,2,3,4,5]

# for numero in numeros:
#     if numero == 3:
#         continue
#     print(numero)