listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

moviesList = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "Forrest Gump"]

moviesWithE = [movie for movie in moviesList if 'e' in movie.lower()]
print(moviesWithE)

moviesWatched = [movie for movie in moviesList if movie != "Pulp Fiction"]
print(moviesWatched)

while True:
    searchName = input("Digite o nome do filme para buscar na lista (ou sair para encerrar): \n")
    if searchName.lower() == "sair":
        print("Programa encerrado")
        break

    foundMovies = [movie for movie in moviesList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filme(s) encontrado(s) com o nome: {searchName}")
        for foundMovie in foundMovies:
            print(foundMovie)
    else:
        print(f"Nenhum filme foi encontrado com o nome {searchName}, Tente novamente!")