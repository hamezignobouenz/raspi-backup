import sys
import random

random.seed(1000)
probability = float(sys.argv[-1])

for line in sys.stdin:
    if random.random() <= probability:
        print(line.strip())
