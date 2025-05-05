from shared.datatypes import *


# Declare the ciphertext to find the key for
CIPHER_TEXT = CipherText("""
BXOPI CQOIL RZZIA FYOPQ OGIQA UICBV IWBXQ PFRLI BXQVB CCQTI OPQOC FFHIW QSAFL LOPIA
BVIAQ XWOPI NCQBX OFOPI ZFRXO QBXLB XOPIE IWFYO PIABV IAOPI AIUIA INIEE CILQX WEFRC
WIALW AGQXW UPBOI BXOPI LRXQX WOPIU QOIAU QLSCI QAQXW LUBYO CGZFV BXTQX WECRI BXOPI
SPQXX ICLOA FFNLU IXOEG OPIPF RLIQX WWFUX OPIAF QWQXW OPIWR LOOPI GAQBL IWNFU WIAIW
OPICI QVILF YOPIO AIIL """)






# TODO: Temporary Functions to remove later
def most_common_key(text: LetterFrequency):
    return "".join([char for char, _ in text])





# Generate a key based on the most common letters in the ciphertext
def generate_keys(ciphertext: CipherText) -> LetterMapping:

    # english_monographs = EnglishInternalMonographFrequency()
    # print(most_common_key(english_monographs))
    # print(most_common_key(ciphertext.monographs))

    # english_digraphs = EnglishInternalDigraphFrequency()
    # print(most_common_key(english_digraphs))
    # print(most_common_key(ciphertext.digraphs))

    # english_trigraphs = EnglishInternalTrigraphFrequency()
    # print(most_common_key(english_trigraphs))
    # print(most_common_key(ciphertext.trigraphs))

    english_double = EnglishInternalDoubleLetterFrequency()
    print(most_common_key(english_double))
    print(most_common_key(ciphertext.doubles))


# new_mappings = generate_keys(CIPHER_TEXT)


knowns = LetterMapping(
    plain_key= "abcdefghijklmnopqrstuvwxyz",
    cipher_key="QESWIYTPB_HCZXFN_ALORVU_G_"
)
print(knowns)


guess = CIPHER_TEXT.decrypt(knowns)
print(guess)









# def calculate_chi_squared(ciphertext: LetterFrequency, english: LetterFrequency) -> float:
#     chi_squared = 0
#     for char in VALID_CHARACTERS.lower():
#         observed = ciphertext.get_frequency(char.lower())
#         expected = english.get_frequency(char.lower())
#         chi_squared += (observed - expected)**2 / expected
#     return chi_squared


# # Make guess of the key
# def key_guesser(ciphertext: LetterFrequency) -> str:
#     # For now, just make a string in the order of the most common letters in English
#     return "".join([char for char, _ in ciphertext.ordered_list])
#
# CIPHER_GUESS = key_guesser(CIPHERTEXT)
# ENGLISH_KEY = key_guesser(ENGLISH_LETTER_FREQUENCY)
# print(f"{CIPHER_GUESS=}")
# print(f"{ENGLISH_KEY=}")







