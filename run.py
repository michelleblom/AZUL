from model import GameRunner,Player
from iplayer import InteractivePlayer
from naive_player import NaivePlayer


players = [InteractivePlayer(0), NaivePlayer(1)]

gr = GameRunner(players, 1384754856864)

scores = gr.Run(True)

print("Player 0 score is {}".format(scores[0]))
print("Player 1 score is {}".format(scores[1]))
