from homework_3.assignment import LETTER_TO_NUMBER, NUMBER_TO_LETTER

MOD_INVERSE_26 = {
    1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23, 19: 11, 21: 5, 23: 17, 25: 25
}

def affine_encrypt(plaintext, a, b):
    """
    Encrypts a plaintext using the Affine cipher with the given key.
    :param plaintext: The plaintext to encrypt.
    :param a: The first key for the Affine cipher.
    :param b: The second key for the Affine cipher.
    :return: The encrypted ciphertext.
    """
    ciphertext = ""
    for letter in plaintext:
        if letter in LETTER_TO_NUMBER:
            number = LETTER_TO_NUMBER[letter]
            number = (a * number + b) % 26
            ciphertext += NUMBER_TO_LETTER[number]
        else:
            ciphertext += letter
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    """
    Decrypts a ciphertext using the Affine cipher with the given key.
    :param ciphertext: The ciphertext to decrypt.
    :param a: The first key for the Affine cipher.
    :param b: The second key for the Affine cipher.
    :return: The decrypted plaintext.
    """
    plaintext = ""
    a_inverse = MOD_INVERSE_26.get(a)
    if a_inverse is None: raise ValueError("The key 'a' is not invertible.")
    for letter in ciphertext:
        number = LETTER_TO_NUMBER[letter.lower()]
        number = (a_inverse * (number - b)) % 26
        plaintext += NUMBER_TO_LETTER[number]
    return plaintext.lower()

def affine_brute_force(ciphertext: str, *, known_string: str|None=None) -> None:
    """
    Brute forces the decryption of a ciphertext using the Affine cipher.
    :param ciphertext: The ciphertext to decrypt.
    :param known_string: A known string that is expected to be in the decrypted plaintext.
    """
    # \gcd(\alpha,26)=1, b is all possible values from 0 to 25
    ALPHA: list[int] = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    BETA:  list[int] = list(range(26))

    # Brute force all possible combinations of a and b
    for a in ALPHA:
        for b in BETA:
            plaintext = affine_decrypt(ciphertext, a, b)
            if known_string is not None and known_string not in plaintext:
                continue
            print(f"{a=}, {b=}, {plaintext=}")

if __name__ == "__main__":
    CIPHERTEXT = "A GCRB BK ICC BHC JKQBKP KV DHAFKIKDHS".replace(" ", "")
    affine_brute_force(CIPHERTEXT, known_string="the")
