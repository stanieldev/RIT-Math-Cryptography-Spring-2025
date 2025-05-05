from homework_3.assignment import LETTER_TO_NUMBER, NUMBER_TO_LETTER
import numpy as np

CIPHERTEXT = "CUSTDK"
PLAINTEXT = "warble"
DEBUG = False


def hill_encrypt(plaintext: str, matrix: np.ndarray):
    """
    Encrypts a plaintext using the Hill cipher with the given key.
    :param plaintext: The plaintext to encrypt.
    :param matrix: The key for the Hill cipher.
    :return: The encrypted ciphertext.
    """
    # Convert the plaintext to a list of numbers
    plaintext = [LETTER_TO_NUMBER[letter] for letter in plaintext]
    if DEBUG: print(f"{plaintext=}")

    # Pad the plaintext with zeros if it is not a multiple of the matrix size
    if len(plaintext) % matrix.shape[0] != 0:
        plaintext.extend([0] * (matrix.shape[0] - len(plaintext) % matrix.shape[0]))
    if DEBUG: print(f"{matrix=}")
    if DEBUG: print(f"{matrix.shape=}")

    # Convert the plaintext to a matrix
    plaintext = np.array(plaintext).reshape(-1, matrix.shape[0])
    if DEBUG: print(f"{plaintext=}")
    if DEBUG: print(f"{plaintext.shape=}")

    # Encrypt the plaintext using the matrix
    ciphertext = np.dot(plaintext, matrix) % 26
    if DEBUG: print(f"{ciphertext=}")

    # Convert the ciphertext to a string
    ciphertext = "".join(NUMBER_TO_LETTER[number] for number in ciphertext.flatten())
    if DEBUG: print(f"{ciphertext=}")

    # Return the encrypted ciphertext
    return ciphertext

def hill_decrypt(ciphertext: str, key: np.ndarray):
    """
    Decrypts a ciphertext using the Hill cipher with the given key.
    :param ciphertext: The ciphertext to decrypt.
    :param key: The key for the Hill cipher.
    :return: The decrypted plaintext.
    """
    # Convert the ciphertext to a list of numbers
    ciphertext = [LETTER_TO_NUMBER[letter.lower()] for letter in ciphertext]
    if DEBUG: print(f"{ciphertext=}")

    # Convert the ciphertext to a matrix
    ciphertext = np.array(ciphertext).reshape(-1, key.shape[0])
    if DEBUG: print(f"{ciphertext=}")

    # Calculate the inverse of the key matrix
    key_inverse = inverse_matrix(key)
    if DEBUG: print(f"{key_inverse=}")

    # Decrypt the ciphertext using the inverse of the key matrix
    plaintext = np.dot(ciphertext, key_inverse) % 26
    if DEBUG: print(f"{plaintext=}")

    # Convert the plaintext to a string
    plaintext = "".join(NUMBER_TO_LETTER[number] for number in plaintext.flatten())
    if DEBUG: print(f"{plaintext=}")

    # Return the decrypted plaintext
    return plaintext.lower()

def brute_force_2x2(plaintext: str, ciphertext: str):
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    # Calculate the determinant of the matrix
                    determinant = (a * d - b * c) % 26
                    if determinant % 2 == 0 or determinant % 13 == 0:
                        continue

                    matrix = np.array([[a, b], [c, d]])
                    guess = hill_encrypt(plaintext, matrix)
                    if guess == CIPHERTEXT.lower():
                        print(f"{matrix=}, {ciphertext=}")
                        break
                else:
                    continue
                break

def inverse_matrix(matrix, base=26):
    """
    Calculates the inverse of a matrix.
    :param matrix: The matrix to calculate the inverse of.
    :param base: The base to calculate the inverse in.
    :return: The inverse of the matrix.
    """
    # Calculate the determinant of the matrix
    determinant = np.linalg.det(matrix)
    if DEBUG: print(f"{determinant=}")

    # Calculate the inverse of the determinant
    determinant_inverse = pow(int(determinant), -1, base)
    if DEBUG: print(f"{determinant_inverse=}")

    # Calculate the adjugate of the matrix
    adjugate = np.round(np.linalg.inv(matrix) * determinant).astype(int)
    if DEBUG: print(f"{adjugate=}")

    # Calculate the inverse of the matrix
    matrix_inverse = (adjugate * determinant_inverse) % base
    if DEBUG: print(f"{matrix_inverse=}")

    return matrix_inverse



if __name__ == "__main__":
    key_matrix = np.array([[19, 8],[7, 13]])
    print(inverse_matrix(key_matrix))

    print(hill_decrypt("HYPNN IWVHE IOEOG OBDBT".replace(" ", ""), key_matrix))
