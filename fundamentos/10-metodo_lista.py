filmsList = ["Inception", "The Dark Knight", "Interstellar", "Parasite", "Joker"]

print(len(filmsList))  # retorna o número de elementos da lista
print(filmsList.index("Interstellar"))  # retorna o índice do elemento
filmsList.append("The Godfather")  # adiciona um elemento no final da lista
print(filmsList)

filmsList.sort()  # ordena a lista em ordem alfabética
print(filmsList)

filmsCopy = filmsList.copy()  # cria uma cópia da lista
filmsCopy.remove("Parasite")  # remove o elemento da lista
print(filmsCopy)

filmsList.clear()  # limpa a lista
print(filmsList)