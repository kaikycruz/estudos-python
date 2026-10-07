num1 = int(input("Enter the first number: \n"))
num2 = int(input("Enter the second number: \n"))

sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"Soma de {num1} e {num2}: {sum} \n")
print(f"Subtração de {num1} e {num2}: {sub} \n")
print(f"Divisão de {num1} e {num2}: {div} \n")
print(f"Multiplicação de {num1} e {num2}: {mult} \n")
print(f"Resto da divisão de {num1} e {num2}: {mod} \n")
print(f"Exponenciação de {num1} e {num2}: {exp} \n")


bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
biggerEqual = num1 >= num2
smallerEqual = num1 <= num2

print(f"{num1} é maior que {num2}? {bigger} \n")
print(f"{num1} é menor que {num2}? {smaller} \n")
print(f"{num1} é igual a {num2}? {equal} \n")
print(f"{num1} é diferente de {num2}? {different} \n")
print(f"{num1} é maior ou igual a {num2}? {biggerEqual} \n")
print(f"{num1} é menor ou igual a {num2}? {smallerEqual} \n")

num1 += 1
num1 -= 1
num1 *= 1
num1 /= 1