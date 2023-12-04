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
            # retorna uma lista vazia para iniciar os highscores.
            highscores = []
        return highscores

    def save_highscores(self):
        with open(self.filename, 'w') as file:
            json.dump(self.highscores, file, indent=4)

    def add_score(self, name, score):
        self.highscores.append({'name': name, 'score': score})
        self.highscores.sort(key=lambda x: x['score'], reverse=True)
        self.highscores = self.highscores[:5]  # Manter apenas os top 5
        self.save_highscores()  # Salvar os scores após adicionar um novo

    def update_highscore(self, name, score):
        self.add_score(name, score)

    def get_leaderboard(self, limit=5):
        return self.highscores[:limit]
