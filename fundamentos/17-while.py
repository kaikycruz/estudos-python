moviesList = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "Forrest Gump"]

index = 0
while index < len(moviesList):
    print(moviesList[index])
    index += 1


index = 0
while index < len(moviesList):
    if moviesList[index] == "The Godfather":
        break
    print(moviesList[index])
    index += 1


index = 0
while index < len(moviesList):
    if moviesList[index] == "The Godfather":
        index += 1
        continue
    print(moviesList[index])
    index += 1


movieName = input("Digite o nome do filme: \n")
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))

total = 0
count = 0

while count < movieRating:
    note = float(input("Digite a nota para o filme: \n"))
    total += note
    count += 1

if movieRating > 0:
    average = total /movieRating
else:
    average = 0

print(f"A média de avaliação do filme {movieName} é: {average:.2f}")