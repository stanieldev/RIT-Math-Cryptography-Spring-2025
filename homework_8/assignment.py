def point_add(P, Q, a, p):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 != y2:
        return None  # Point at infinity
    if P == Q: m = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    else:      m = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def scalar_mult(k, P, a, p):
    result = None
    addend = P
    while k:
        if k & 1:
            result = point_add(result, addend, a, p)
        addend = point_add(addend, addend, a, p)
        k >>= 1
    return result



a = 1
b = 3
p = 8779
P = (8089,6538)
k = 256



result = scalar_mult(k, P, a, p)
print("k * P =", result)



print(point_add((201,478),(1406, 470), a, p))