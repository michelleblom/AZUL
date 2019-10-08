# Written by Michelle Blom, 2019
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
from model import GameRunner,Player
from iplayer import InteractivePlayer
from naive_player import NaivePlayer


players = [InteractivePlayer(0), NaivePlayer(1), NaivePlayer(2),NaivePlayer(3)]

gr = GameRunner(players, 1384754856864)

scores = gr.Run(True)

print("Player 0 score is {}".format(scores[0]))
print("Player 1 score is {}".format(scores[1]))
print("Player 2 score is {}".format(scores[2]))
print("Player 3 score is {}".format(scores[3]))
