class Game:
    name: str = ""
    year_lanch: int = 0
    multiplayer: bool = False
    note: float = 0.0

game1 = Game()
game1.name = "GTA V"
game1.year_lanch = 2013
game1.multiplayer = True
game1.note = 9.9

game2 = Game()
game2.name = "Fortnite"
game2.year_lanch = 2017
game2.multiplayer = True
game2.note = 9.0

print("---------Dados do Jogo----------")
print(f"\nNome do jogo: {game1.name}\nAno de Lançamento: {game1.year_lanch}")
print(f"\nNome do jogo: {game2.name}\nAno de Lançamento: {game2.year_lanch}")
