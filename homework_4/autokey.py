from homework_3.assignment import LETTER_TO_NUMBER, NUMBER_TO_LETTER
AVAILABLE_CHAR = "abcdefghijklmnopqrstuvwxyz"





def encrypt_autokey(plaintext: str, keyword: str) -> str:
    key = keyword + plaintext
    key = key.upper()
    key = key[:len(plaintext)]
    ciphertext = ""
    for i in range(len(plaintext)):
        plaintext_letter = plaintext[i]
        key_letter = key[i].lower()
        plaintext_number = LETTER_TO_NUMBER[plaintext_letter]
        key_number = LETTER_TO_NUMBER[key_letter]
        ciphertext_number = (plaintext_number + key_number) % 26
        ciphertext_letter = NUMBER_TO_LETTER[ciphertext_number]
        ciphertext += ciphertext_letter
    return ciphertext

def decrypt_autokey(ciphertext: str, keyword: str) -> str:
    key = keyword
    plaintext = ""
    for i in range(len(ciphertext)):
        ciphertext_letter = ciphertext[i].lower()
        key_letter = key[i].lower()
        ciphertext_number = LETTER_TO_NUMBER[ciphertext_letter]
        key_number = LETTER_TO_NUMBER[key_letter]
        plaintext_number = (ciphertext_number - key_number) % 26
        plaintext_letter = NUMBER_TO_LETTER[plaintext_number]
        plaintext += plaintext_letter
        key += plaintext_letter
    return plaintext

# print(decrypt_autokey("qnxepvytwtwp", "queenly"))






CIPHERTEXT = "UOGRK QSXNK ACPTK ACCEN I".replace(" ", "")



with open("words.tsv", "w") as f:
    for c1 in AVAILABLE_CHAR:
        for c2 in AVAILABLE_CHAR:
            for c3 in AVAILABLE_CHAR:
                for c4 in AVAILABLE_CHAR:
                    for c5 in AVAILABLE_CHAR:
                        keyword = c1+c2+c3+c4+c5
                        plaintext = decrypt_autokey(CIPHERTEXT, keyword)
                        if "the" in plaintext:
                            f.write(f"{keyword}\t{plaintext}\n")
                            break
                        else:
                            continue