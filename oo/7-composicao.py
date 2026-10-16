class Game:
    def __init__(self, name: str = "", year_launch: int = 0, multiplayer: bool = False, note: float = 0.0):
        self.name = name
        self.year_launch = year_launch
        self.multiplayer = multiplayer
        self.note = note
        self.totalEvaluation = 0.0
        self.evaluators = 0

    def __str__(self):
        return f"Game: {self.game}"

    def technical_sheet(self):
        print("---------Dados do Jogo----------")
        print(f"\nNome do jogo: {self.name}")
        print(f"Ano de Lançamento: {self.year_launch}")
        print(f"Multiplayer? {self.multiplayer}")
        print(f"Nota: {self.note}\n")


class Game_studio:
    def __init__(self, name: str = ""):
        self.name = name
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def evaluate_studio_quality(self):
        total_notes = sum(game.note for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print(f"O estúdio {self.name} ainda não lançou jogos")
        else:
            average_note = total_notes / num_games
            print(f"Avaliação média dos jogos do estúdio {self.name}: {average_note:.2f}")

game1 = Game("GTA V", 2013, True, 9.9)
game2 = Game("Fortnite", 2017, True, 8.4)
game3 = Game("The Last of Us 2", 2020, False, 9.5)

studio = Game_studio("Awesome Games")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.evaluate_studio_quality()

for game in studio.games:
    game.technical_sheet()