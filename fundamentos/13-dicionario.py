filmInception = {
    "title": "Inception",
    "yearReleased": 2010,
    "imdbRating": 8.8,
    "genre": ["Sci-Fi", "Action", "Thriller"]
}

print(filmInception)
print(len(filmInception))

print(filmInception["genre"])
print(filmInception.get("imdbRating"))

print(filmInception.keys()) 

print(filmInception.values())

print(filmInception.items())

filmInception["director"] = "Christopher Nolan"
print(filmInception)

filmInception.update({"imdbRating": 9.0})
print(filmInception)

filmInception.pop("yearReleased")


