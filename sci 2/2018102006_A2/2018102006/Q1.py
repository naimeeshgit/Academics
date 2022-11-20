import random

p = 0.25
n = 1000
simulations = 10000

c_240A = 0
for _ in range(simulations):
    X = [1 if random.random() < p else 0 for _ in range(n)]
    if (sum(X) >= 240):
        c_240A += 1

print("Probability of at least 240 A's in the sequence: ",c_240A/simulations )
