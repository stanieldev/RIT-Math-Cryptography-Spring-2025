# Define the parameters for the Miller-Rabin test
import math
N = 8976397  # Composite number
S = 2    # Highest power of 2 that divides N-1
D = 2244099   # Odd number such that N-1 = 2^S * D

# Function to check if a base 'a' is a witness
def miller_rabin_test(a):
    x = pow(a, D, N)
    if x == 1 or x == N - 1:
        return False      # Not a witness
    for i in range(1, S):
        x = pow(x, 2, N)
        if x == N - 1:
            return False  # Not a witness
    return True           # Is a witness

# Loop through all bases
k = 512 + 1
for a in range(2, k):
    WITNESS = True
    TEST = miller_rabin_test(a)
    if TEST and WITNESS:
        print(f"{a} is a witness to the compositeness of {N}.")
    elif not TEST and not WITNESS:
        print(f"{a} is not a witness (N might be prime for this base).")

