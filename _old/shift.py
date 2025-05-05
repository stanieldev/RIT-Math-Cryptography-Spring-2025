import random



VALID_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

CIPHER_TEXT = """
MSUYB YQKMJ PSIFN OOYCM ZYGKM NYZOS PWINF IHBUW KWBSK MHMZJ
SPMKS WWZUM ZBSFZ BXMSP PMBIP MZZLT TNWOM ZSFPM BQKWY BSMZY
ZWEEF KSSFW BIYGW SPWVM NWUMZ OBNMG GWOAL MIHNC SPKFL JPSPW
JNYBB OFFKB FEVMI SFKCX YZBMF ZBSPF LJPZF SALMI HNCWZ FLJPS
FGKWV WZSYB UMKNF EJKMS SCOLB SEKFX WZSWK MZJYN FZJUM SPPMX
MECFL KWYNN CUYZS SFPWY KYQFL SMSSP WEMKB SSPMZ JCFLN NGKFQ
YQNCU YZSSF HZFUM BUPWK WMUYB QFKZY ZOUPY SXCNF LBCIP MNOPF
FOUYB NMHWY ZOPFU XCGYK WZSBU WKWFI ILGMW OYZOY NNQWE FKWSP
WCPYO XWYZO YNNSP YSOYV MOIFG GWKEM WNOHM ZOFEI KYGQL SMOFZ
SEWWN NMHWJ FMZJM ZSFMS MECFL UYZSS FHZFU SPWSK LSP
""".upper()




ENGLISH_CHAR_FREQUENCY = {
    "E": 21912,
    "T": 16587,
    "A": 14810,
    "O": 14003,
    "I": 13318,
    "N": 12666,
    "S": 11450,
    "R": 10977,
    "H": 10795,
    "D": 7874,
    "L": 7253,
    "U": 5246,
    "C": 4943,
    "M": 4761,
    "F": 4200,
    "Y": 3853,
    "W": 3819,
    "G": 3693,
    "P": 3316,
    "B": 2715,
    "V": 2019,
    "K": 1257,
    "X": 315,
    "Q": 205,
    "J": 188,
    "Z": 128
}


class SubstitutionCipherText:
    def __init__(self, ciphertext: str):

        # Cipher text characteristics
        self.ciphertext: str = ciphertext
        self.ciphertext_length: int = sum((1 for char in self.ciphertext if char in VALID_CHARACTERS))

        # Frequency analysis
        self.frequency_map: dict = self._frequency_map()
        self.ordered_frequency: list = self._order_letter_frequency()
        self.ordered_frequency_string: str = self._order_letter_frequency_string()

    def __str__(self):
        return self.ciphertext

    def __repr__(self):
        return self.ciphertext

    def _frequency_map(self) -> dict:
        return {char: self.ciphertext.count(char) for char in VALID_CHARACTERS}

    def _order_letter_frequency(self) -> list:
        ordered_list = [(k, v) for k, v in self.frequency_map.items()]
        ordered_list.sort(key=lambda x: x[1], reverse=True)
        return ordered_list

    def _order_letter_frequency_string(self) -> str:
        return "".join([x[0] for x in self.ordered_frequency]).upper()





def relative_frequency_chance(data: dict, keys: str):
    subset = {k: data[k] for k in VALID_CHARACTERS if k in keys}
    if sum(subset.values()) == 0:
        return {k: 1 / len(subset) for k in subset.keys()}
    else:
        return {k: v / sum(subset.values()) for k, v in subset.items()}

def choose_random_letter_weighted(data: dict):
    random_number = random.random()
    for k, v in data.items():
        if random_number < v:
            return k
        random_number -= v
    return None






while True:
    CIPHER = SubstitutionCipherText(CIPHER_TEXT)
    available_english_chars = VALID_CHARACTERS
    available_cipher_chars = CIPHER.ordered_frequency_string
    while available_english_chars:
        # Get a weighted map of the english and cipher characters
        english_weighted = relative_frequency_chance(ENGLISH_CHAR_FREQUENCY, available_english_chars)
        cipher_weighted = relative_frequency_chance(CIPHER.frequency_map, available_cipher_chars)

        # Choose a random letter from the weighted map
        english_char = choose_random_letter_weighted(english_weighted).lower()
        cipher_char = choose_random_letter_weighted(cipher_weighted)

        # Remove the chosen characters from the available characters
        available_english_chars = available_english_chars.replace(english_char.upper(), "")
        available_cipher_chars = available_cipher_chars.replace(cipher_char, "")

        # Replace the cipher character with the english character
        CIPHER.ciphertext = CIPHER.ciphertext.replace(cipher_char, english_char)
        print(CIPHER.ciphertext)
        print(f"Substituting {english_char} for {cipher_char}...")

    input("Waiting for input...")





















#
# class SubstitutionCipherSolver:
#     def __init__(self, cipher: SubstitutionCipherText):
#         self.cipher = cipher
#
#     def start(self):
#         while True:
#             english: str = ENGLISH_FREQUENCY
#             attempt: str = self.cipher.ciphertext
#
#     def pick_letter(self):
#         pass






        #
        #
        # global ENGLISH_FREQUENCY
        # while True:
        #     # Clear console screen
        #     os.system("cls" if os.name == "nt" else "clear")
        #
        #     # Print the cipher text
        #     print(self.cipher.ciphertext)
        #
        #     # Replace all valid characters with "_"
        #     print("".join([char if char not in VALID_CHARACTERS else "_" for char in self.cipher.ciphertext]))
        #
        #     # Print top 10 most frequent letters in the cipher text
        #     print(ENGLISH_FREQUENCY)
        #     for i in range(min(10, len(self.cipher.ordered_frequency))):
        #         print(f"{self.cipher.ordered_frequency[i][0]}: {self.cipher.ordered_frequency[i][1]}")
        #
        #     # Ask for input to decipher the text
        #     user = input("> ")
        #     if user == "":
        #         ci = self.cipher.ordered_frequency[0][0]
        #         pt = ENGLISH_FREQUENCY[0]
        #     else:
        #         ci, pt = user.split("=")
        #     self.cipher.ciphertext = self.cipher.ciphertext.replace(ci.upper(), pt.lower())
        #
        #     # Remove the letters used from the ordered frequency list
        #     self.cipher.ordered_frequency = [(k, v) for k, v in self.cipher.ordered_frequency if k != ci.upper()]
        #
        #     ENGLISH_FREQUENCY = ENGLISH_FREQUENCY.replace(pt.upper(), "")


    # def _decipher_text(self) -> str:
    #     for char in self.cipher.ordered_frequency_string:
    #         self.cipher.ciphertext = self.cipher.ciphertext.replace(char, ENGLISH_FREQUENCY[self.cipher.ordered_frequency_string.index(char)].lower())
    #     return self.cipher.ciphertext


#
# text = SubstitutionCipherText(CIPHER_TEXT)
# print(text.frequency_map)
# print(text.ordered_frequency)
# print(text.ordered_frequency_string)
#
# solver = SubstitutionCipherSolver(text)
#
#
# solver.start()
