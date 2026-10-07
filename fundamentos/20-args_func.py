def fullName(firstName, lastName):
    print(f"Nome: {firstName} {lastName}")

fullName("Kaiky", "Cruz")


def sum(a, b):
    return a + b

print(f"O resultado da soma é: {sum(15, 10)}")


def address(country="Brasil"):
    print(f"Eu moro em: {country}")

address()
address("Portugal")


def rateMovie(numRatings, movieName):
    total = 0
    for i in range(numRatings):
        note = float(input("Digite a avaliação do filme: \n"))
        total += note
    if numRatings > 0:
        average = total / numRatings
    else:
        average: 0

    print(f"Média de avaliação do filme {movieName} é: {average:.2f}")


rateMovie(2, "Sonic")