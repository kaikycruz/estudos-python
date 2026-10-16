class Game:
    def __init__(self, name: str = "", year_launch: int = 0, multiplayer: bool = False, note: float = 0.0):
        self.name = name
        self.year_launch = year_launch
        self.multiplayer = multiplayer
        self.note = note

    def __str__(self):
        return f"Game: {self.game}"


game1 = Game("GTA V", 2013, True, 9.9)

print("---------Dados do Jogo----------")
print(f"\nNome do jogo: {game1.name}\nAno de Lançamento: {game1.year_launch}")
# print(f"\nNome do jogo: {game2.name}\nAno de Lançamento: {game2.year_lanch}")
