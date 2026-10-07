power = lambda num: num ** 2
print(power(5))

is_even = lambda x: x % 2 == 0
print(is_even(27))

division = lambda x, y: x / y
print(division(10, 5))

reverseString = lambda s: s[::-1]
print(reverseString("JavaScript"))

moviesList = ["The Shawshank Redemption", "The Godfather", "The Dark Knight"]
ratings = {
    "The Shawshank Redemption": [9.2, 8.5, 8.8],
    "The Godfather": [9.9, 9.8, 10],
    "The Dark Knight": [9.5, 9.0, 8.9]
}

averageRating = lambda movieName: sum(ratings[movieName]) / len(ratings[movieName])

checkMovie = lambda movieName: movieName in moviesList

recommendMovie = lambda movieName: f"Recomendo assitir {movieName} com media de {averageRating(movieName):.2f}"

print(f"Média de avaliação do filme The Godfather: {averageRating('The Godfather')}")
print(f"The Godfather está na lista? {checkMovie('The Godfather')}")
print(f"{recommendMovie('The Godfather')}")

