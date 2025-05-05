import numpy as np
from typing import Tuple

class PlayfairMode:
    ENCRYPT = 0
    DECRYPT = 1



# Generates a key table for the Playfair cipher from a given key
def _gen_key_table(key: str) -> np.ndarray:
    ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # Assert that the key is valid
    assert len(key) > 0, "Key must not be empty"
    assert all([char.isalpha() for char in key]), "Key must only contain alphabetic characters"

    # Rectify key to stardard format
    key = key.upper()
    key = key.replace("J", "I")  # Replace J with I
    assert all([char in ALPHABET for char in key])

    # Replace all duplicate characters with X
    key_string = ""
    for char in key:
        if char not in key_string:
            key_string += char
    key = key_string
    assert key.count("J") + key.count("I") <= 1, "Key must not contain both I and J"
    assert all([key.count(char) <= 1 for char in ALPHABET]), "Key must not contain duplicate characters"

    # Fill the rest of the table with the remaining characters
    for char in ALPHABET:
        if char not in key:
            key += char
    assert len(key) == 25
    assert key.count("J") + key.count("I") <= 1, "Key must not contain both I and J"
    assert all([key.count(char) <= 1 for char in ALPHABET]), "Key must not contain duplicate characters"
    print(f"{key=}")

    # Generate the key table
    return np.array(list(key)).reshape(5, 5)

val = _gen_key_table("CHARLES")
print(val)



def _decrypt_playfair(ciphertext: str, key: str) -> str:
    pass

def _encrypt_playfair(plaintext: str, key: str) -> str:
    table = _gen_key_table(key)
    print(f"{table=}")

    # Preprocess the plaintext
    plaintext = plaintext.upper()
    plaintext = plaintext.replace("J", "I")
    plaintext = plaintext.replace(" ", "")
    print(f"{plaintext=}")

    # Split into digraphs
    digraphs = []
    # If a digraph contains the same letter, insert an X between them
    for i in range(0, len(plaintext), 2):
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            digraphs.append(plaintext[i] + "X")
            digraphs.append(plaintext[i + 1] + "X")
        else:
            digraphs.append(plaintext[i:i + 2])
    print(f"{digraphs=}")


    return "temp"






def playfair(text, key, decrypt=False):
    if decrypt:
        return _decrypt_playfair(text, key)
    else:
        return _encrypt_playfair(text, key)