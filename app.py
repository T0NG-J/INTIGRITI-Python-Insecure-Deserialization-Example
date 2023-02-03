import yaml, flask
from cryptography.fernet import Fernet
# import key from secret
key = '3o9JBsyxul26xLOk7ExfJZn-I-y90mxCsUcL9MObiQY='

class Game:
  def __init__(self):
    self.score = 0
  def save_game(self):
    sig = Fernet(key).encrypt(b'%d' % game.score)
    return f'{yaml.dump(self)}-{sig.decode()}'
  @staticmethod
  def load_save_game(save_game):
    game, signature = save_game.split('-', 1)
    pt = Fernet(key).decrypt(signature)
    game = yaml.load(game, yaml.Loader)
    return game.score if game.score == pt else None

app = flask.Flask(__name__)
game = Game()
@app.route('/loadSavedGame')
def load_saved_game():
  global game
  save_game = flask.request.args.get('game')
  game = Game.load_save_game(save_game)
  return 'Saved game loaded!'
@app.route('/saveGame')
def save_game():
  return game.save_game()
