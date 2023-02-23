from cube import Cube
from rotAlgos import RotAlgos, num_to_chars

# cubes, where func returns 1
L = set()
with open('L.txt', 'r') as file:
    [L.add(Cube(line.replace('\n', ''))) for line in file]

# undefined cubes
N = set()
with open('N.txt', 'r') as file:
    [N.add(Cube(line.replace('\n', ''))) for line in file]

alg = RotAlgos(L, N)
alg.run()


