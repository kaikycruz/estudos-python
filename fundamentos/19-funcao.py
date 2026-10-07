def welcome():
    print("Bem vindo ao sistema de filmes")

welcome()


def calculateAverage():
    numRatings = int(input("Digite quantas avaliações deseja fazer para o filme: \n"))
    total = 0 
    for i in range(numRatings):
        note = float(input("Digite a nota para o filme: \n"))
        total += note

    if numRatings > 0:
        average = total / numRatings
    else:
        average = 0

    return average

print(f"A média de avaliações é: {calculateAverage():.2f}")


def createMovie():
    name = input("Digite o nome do filme: \n")
    yearLaunch = int(input("Digite o ano de lançamento do filme: \n"))
    rating = float(input("Digite a nota do filme: \n"))
    moviePrice = float(input("Digite o preço do filme: \n"))
    print(f"{name} ({yearLaunch}) - R$ {moviePrice:.2f}")


createMovie()