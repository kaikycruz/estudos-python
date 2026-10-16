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


game1 = Game("GTA V", 2013, True, 9.8)
game2 = Game("Fortnite", 2017, True, 7.9)
game3 = Game("Red Dead Redemption 2", 2018, False, 10.0)
game1.evaluate(9.0)
game1.evaluate(9.7)
game1.average()
game1.technical_sheet()

print(f"Exibindo total de jogos criados: {Game.total_games}")
