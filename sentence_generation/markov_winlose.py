#incomplete as of 3/12/22
import random
chance_chain = {
    'heads': ['heads', 'heads', 'heads', 'heads', 'heads', 'heads', 'heads', 'heads', 'heads', 'tails'],
    'tails': ['heads', 'tails']
}

results = [random.choice(list(chance_chain.keys()))]

for i in range(10):
    results.append(random.choice(chance_chain[results[i]]))

print(results)