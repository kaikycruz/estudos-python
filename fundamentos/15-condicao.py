# name = input("Digite o nome do filme: \n")
# yearReleased = int(input("Digite o ano de lançamento do filme: \n"))
# rating = float(input("Digite a nota de avaliação do filme: \n"))

# if rating > 8.0 and yearReleased > 2015:
#     print(f"O filme {name} é um ótimo filme, lançado em {yearReleased} com nota {rating}.")
# else:
#     print(f"O filme {name} não é considerado ótimo, lançado em {yearReleased} com nota {rating}.")


num1 = float(input("Digite o primeiro número: \n"))
num2 = float(input("Digite o segundo número: \n"))
operation = input("Digite a operação desejada (+, -, *, /): \n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Erro: Divisão por zero não é permitida.")
        result = 0  
else:
    result = 0
    print("Operação inválida.")

print(f"O resultado da operação é: {result:.2f}")