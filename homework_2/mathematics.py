from math import gcd, lcm





# Homework functions
def minimum_difference(a: int, b: int)-> tuple[int, int]:
    # Find the solution (x,y) for gcd(a,b) = ax + by
    x, y = 0, 1
    xr, yr = 1, 0
    while b:
        quotient, remainder = divmod(a, b)
        a, b = b, remainder
        x, xr = xr - quotient * x, x
        y, yr = yr - quotient * y, y
    return xr, yr

def modular_system(a: list[int], m: list[int]) -> int | None:
    for i in range(lcm(*m)):
        for j in range(len(a)):
            if i % m[j] != a[j]:
                break
        else:
            return i
    return None



def main():
    A, B = 22110, 3267
    x, y = minimum_difference(A, B)
    print(x,y)
    print(A*x + B*y)
    x = modular_system(a=[19,2,1], m=[21,10,13])
    print(x)

if __name__ == "__main__":
    main()