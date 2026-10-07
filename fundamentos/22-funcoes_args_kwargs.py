def sum(*num):
    sumTotal = 0 
    for n in num:
        sumTotal += n
    print(f"Soma é: {sumTotal}")

sum(7)
sum(7, 9)
sum(7, 9, 10, 8, 7, 6)


def presentation(**data):
     for key, value in data.items():
         print(f"{key} - {value}")
print("Lista de Cursos:")
presentation(name="Python", category="Backend", level="Iniciante")
presentation(name="Visão Computacional", category="IA", level="Avançado")
presentation(name="Dashboards com Dash", category="Data Science", level="Intermediário")
