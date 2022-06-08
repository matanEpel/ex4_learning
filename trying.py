import numpy as np

def entropy(vals):
    return sum([i/sum(vals)*np.log2(i/sum(vals)) for i in vals])

print()