class Game:
    total_games: int = 0 # Variavel de classe para verificar quantidade de jogos criados

    def __init__(self, name: str = "", year_launch: int = 0, multiplayer: bool = False, note: float = 0.0):
        self.name = name
        self.year_launch = year_launch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1
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

    def evaluate(self, note: float):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        self.note = self.totalEvaluation / self.evaluators
        print(f"A média do jogo {self.name} é de: {self.totalEvaluation / self.evaluators}")

class SinglePlayerGame(Game):
    def __init__(self, name: str = "", year_launch: int = 0, note: float = 0.0, story_line: str = ""):
        super().__init__(name, year_launch, multiplayer=False, note=note)
        self.story_line = story_line

    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.story_line}\n")


mult_game = Game("Fortnite", 2017, True, 8.3)
mult_game.technical_sheet()

sing_game = SinglePlayerGame("The Last of Us 2", 2020, 9.5, "Emocionante história de sobrevivência/ vingança")
sing_game.technical_sheet()