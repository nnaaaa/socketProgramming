import sys
from game.game import createMap
import ast
map = []
createMap(map)
# for i in range(0, 20):
#     print(map[i])


print(sys.getsizeof(str(map)))