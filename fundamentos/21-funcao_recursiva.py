def fatorial(num):
    if num == 1:
        return 1
    else:
        return (num * fatorial(num - 1))


number = int(input("Digite um número para o fatorial: \n"))
print(f"O fatorial de {number} é {fatorial(number)}")


def totalSum(num):
    if num == 1:
        return 1
    else:
        return (num + totalSum(num - 1))

num = int(input("Digite um número para a soma total: \n"))
print(f"A soma total de {num} é {totalSum(num)}")