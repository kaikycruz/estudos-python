filmsSet = {"Inception", "The Dark Knight", "Interstellar", "Parasite", "Joker"}

print(type(filmsSet))  # Output: <class 'set'>

print(len(filmsSet))  # Output: 5

exampleSet = {"The Matrix", "Pulp Fiction", "Fight Club"}
filmsSet.update(exampleSet)

print(filmsSet)

filmsSet.remove("Joker")
print(filmsSet)