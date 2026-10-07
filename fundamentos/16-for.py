moviesList = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "Forrest Gump"]

for movie in moviesList:
    print(movie)


for movie in moviesList:
    if movie == "The Godfather":
        break
    print(movie)


for movie in moviesList:
    if movie == "The Godfather":
        continue
    print(movie)


movieName = input("Digite o nome do filme: \n")
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))

total = 0

moviesList.append(movieName)

for i in range(movieRating):
    note = float(input("Digite a nota para o filme: \n"))
    total += note

if movieRating > 0:
    average = total / movieRating
else:
    average = 0

print(f"A média de avaliação do filme {movieName} é: {average:.2f}")

print(f"Lista de filmes atualizada: {moviesList}")