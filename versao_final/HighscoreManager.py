import json

class HighscoreManager:
    def __init__(self, filename='highscores.json'):
        self.filename = filename
        self.highscores = self.load_highscores()

    def load_highscores(self):
        try:
            with open(self.filename, 'r') as file:
                highscores = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Se o arquivo não existir ou se houver um erro ao decodificar o JSON,
            # retorna um dicionário vazio para iniciar os highscores.
            highscores = {}
        return highscores

    def save_highscores(self):
        with open(self.filename, 'w') as file:
            json.dump(self.highscores, file, indent=4)

    def update_highscore(self, player_name, score):
        if player_name not in self.highscores or score > self.highscores[player_name]:
            self.highscores[player_name] = score
            self.save_highscores()

