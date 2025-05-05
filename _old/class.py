A = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
B = list(range(1, 26+1))

# Create a map that maps A->0 and Z->25
mapping = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25
}
import numpy as np

CIPHER_TEXT = "XA LSUFS OL QLSP N PLSF WFSQFJO ZAXLA".replace(" ", "_")
X = []
for char in CIPHER_TEXT:
    if char != "_":
        X.append(mapping[char])
print(X)
X = np.array(X)

for alpha in A:
    for beta in B:
        result = (alpha * X + beta) % 26
        # Inverse map the result
        result = [list(mapping.keys())[list(mapping.values()).index(x)] for x in result]
        output = ""
        for char in CIPHER_TEXT:
            if char != "_":
                output += result.pop(0)
            else:
                output += " "
        print(f"{alpha=}, {beta=}, {output=}")