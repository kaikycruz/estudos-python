import pprint

filmsDict = {
    "Inception": {
        "yearReleased": 2010,
        "imdbRating": 8.8,
        "genre": ["Sci-Fi", "Action", "Thriller"]
    },
    "The Dark Knight": {
        "yearReleased": 2008,
        "imdbRating": 9.0,
        "genre": ["Action", "Crime", "Drama"]
    },
    "Interstellar": {
        "yearReleased": 2014,
        "imdbRating": 8.6,
        "genre": ["Adventure", "Drama", "Sci-Fi"]
    },
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

print(filmsDict["Interstellar"]["genre"])
filmsDict["Interstellar"]["director"] = "Christopher Nolan"

print(filmsDict["Interstellar"])

del filmsDict["The Dark Knight"]
pp.pprint(filmsDict)