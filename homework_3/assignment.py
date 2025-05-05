# Notes for Cipher:
# Key repeats for each letter in the plaintext by modulus |keys|


# Mappings
LETTER_TO_NUMBER = {chr(i): i - 97 for i in range(97, 123)}
NUMBER_TO_LETTER = {i - 97: chr(i) for i in range(97, 123)}

# Encryption
def encrypt(plaintext: str, key: str):
    ciphertext = ""
    for i, c in enumerate(plaintext):
        key_index = i % len(key)
        key_char = key[key_index]
        shift = LETTER_TO_NUMBER[key_char]
        new_char = NUMBER_TO_LETTER[(LETTER_TO_NUMBER[c] + shift) % 26]
        ciphertext += new_char.upper()
        if i % 5 == 4: ciphertext += " "
    return ciphertext

# Decryption
def decrypt(ciphertext: str, key: str):
    plaintext = ""
    ciphertext = ciphertext.replace(" ", "")
    for i, c in enumerate(ciphertext):
        key_index = i % len(key)
        key_char = key[key_index]
        shift = LETTER_TO_NUMBER[key_char]
        new_char = NUMBER_TO_LETTER[(LETTER_TO_NUMBER[c.lower()] - shift) % 26]
        plaintext += new_char
    return plaintext





def testing_encrypt_decrypt():
    plaintext = "mathisawesome"
    key = "tiger"
    ciphertext = encrypt(plaintext, key)
    print(ciphertext)
    decrypted = decrypt(ciphertext, key)
    print(decrypted)
    assert decrypted == plaintext

def question_1():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count_1 = 0
    count_2 = 0
    for c2 in alphabet:
        for c3 in alphabet:
            for c4 in alphabet:
                key = "w" + c2 + c3 + c4
                val = decrypt("SSEMA DPTLZ PTBHS JQBTY ARDYW HPX", key)
                if "the" in val:
                    print(val)
                    print(key)
    return None


def question_2():
    ciphertext = "SMMPFYPTMOHJ"
    plaintext = "hellofriends"

    for c, p in zip(ciphertext, plaintext):
        print(NUMBER_TO_LETTER[(LETTER_TO_NUMBER[c.lower()] - LETTER_TO_NUMBER[p]) % 26])

    plain = decrypt("SMMPF YPTMO HJNFZ PNEKV FPLQP RBLEM YXXBT PABAR RYWWU SWBLQ WSQRM GZV", "liberty")
    print(plain)
    return None


def question_3D():
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = "HJFMR VHLIL VSPTC JESIP PSOVO PBHWD IRHAS WWSOC MCHLI PIXYB BSJIV ICTOV AWSRX WSGPD IHWWI RKDDT VTGWM KSPCA CAMCH LIWSE ZTBWM WOHFT SRTPG WMCUE PDBIS CVSVH SFERY XLGCY KWOWM CUYPP FPCSF IEGMX VPQXS UQSYC HVCPB HEIZI RVHLJ DIRHB MWIAT EWIVI WWOHI HCJXW SIZTB MRVRV ILCRA XHLMC JMILC JXWSQ IAORG WCPCW CYWTC JYHVI V".replace(
        " ", "")

    amounts = [ciphertext.count(c) for c in ALPHABET]
    contribution = [a * (a - 1) for a in amounts]
    I_c = sum(contribution) / (len(ciphertext) * (len(ciphertext) - 1))
    I_e = 0.0656
    I_r = 0.0385

    print(f"{I_c=}")
    print(f"{I_e=}")
    print(f"{I_r=}")

    k_approx = (I_e - I_r) / (I_c - I_r)
    print(f"{k_approx=}")


if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = "HJFMR VHLIL VSPTC JESIP PSOVO PBHWD IRHAS WWSOC MCHLI PIXYB BSJIV ICTOV AWSRX WSGPD IHWWI RKDDT VTGWM KSPCA CAMCH LIWSE ZTBWM WOHFT SRTPG WMCUE PDBIS CVSVH SFERY XLGCY KWOWM CUYPP FPCSF IEGMX VPQXS UQSYC HVCPB HEIZI RVHLJ DIRHB MWIAT EWIVI WWOHI HCJXW SIZTB MRVRV ILCRA XHLMC JMILC JXWSQ IAORG WCPCW CYWTC JYHVI V".replace(
        " ", "")

    SEARCH = "the"
    for c1 in alphabet:
        for c2 in alphabet:
            for c3 in alphabet:
                key = c1 + c2 + c3 + c1
                val = decrypt(ciphertext, key)
                if val.count(SEARCH) > 3:
                    print(val)
                    print(key)

    val = decrypt(ciphertext, "epoe")
    print(val)