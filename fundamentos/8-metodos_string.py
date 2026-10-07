movieName = "top gun"
movieDescription = """
       jkasjdalks jdlkfklsadjfla kjdflkadsfjlasdfjlaksfj
jadslfjlasdflajsdflafjlafj
"""

print(movieName.upper())
print(movieName.lower())
print(movieName.title())
print(movieName.capitalize())
print(movieName.center(10, "-")) #retorna a string centralizada com o tamanho definido e o caracter de preenchimento
print(movieName.find("u"))  # retorna o índice da primeira ocorrência da substring
print(movieName.count("u"))  # retorna o número de ocorrências da substring
print(movieName.replace("gun", "Maverick"))  # substitui a substring por outra
print(movieName.split(" "))  # divide a string em uma lista de substrings