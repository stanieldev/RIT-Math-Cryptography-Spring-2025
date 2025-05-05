# This file contains the data types used in the cipher solver
VALID_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".upper()




class LetterFrequency:
    def __init__(self, data: dict):
        self.weight = {k: v/sum(data.values()) for k, v in data.items()}

    def __iter__(self):
        return iter(sorted(self.weight.items(), key=lambda item: item[1], reverse=True))

    def __getitem__(self, key):
        return self.weight[key]

    def __repr__(self):
        return f"{__class__.__name__}({self.weight})"

    def __len__(self):
        return len(self.weight.items())

class LetterMapping:
    def __init__(self, *, plain_key: str, cipher_key: str):
        self.mapping = {cipher: plain for plain, cipher in zip(plain_key, cipher_key)}

    def __iter__(self):
        return iter(self.mapping.items())

    def __getitem__(self, key):
        return self.mapping[key]

    def __repr__(self):
        return f"{__class__.__name__}({self.mapping})"

    def inverse(self):
        return LetterMapping(plain_key="".join(self.mapping.values()), cipher_key="".join(self.mapping.keys()))

class CipherText:
    def __init__(self, text: str):
        self._text = text.upper().replace(" ", "").replace("\n", "")
        self._letter_frequency: LetterFrequency = LetterFrequency({char: text.count(char) for char in VALID_CHARACTERS})

    @property
    def text(self):
        return self._text

    @property
    def monographs(self):
        mapping = {char: self._text.count(char) for char in VALID_CHARACTERS}
        return LetterFrequency(mapping)

    @property
    def digraphs(self):
        mapping = {self._text[i:i+2]: self._text.count(self._text[i:i+2]) for i in range(len(self._text) - 1)}
        return LetterFrequency(mapping)

    @property
    def trigraphs(self):
        mapping = {self._text[i:i+3]: self._text.count(self._text[i:i+3]) for i in range(len(self._text) - 2)}
        return LetterFrequency(mapping)

    @property
    def doubles(self):
        mapping = {self._text[i:i+2]: self._text.count(self._text[i:i+2]) for i in range(len(self._text) - 1) if self._text[i] == self._text[i+1]}
        return LetterFrequency(mapping)

    def decrypt(self, key: LetterMapping) -> str:
        plaintext = self._text
        for cipher, plain in key:
            plaintext = plaintext.replace(cipher, plain)
        return plaintext







# Internal Graph Letter Frequencies
class EnglishInternalMonographFrequency(LetterFrequency):
    def __init__(self):
        mapping = {
            "a": 0.082,
            "b": 0.015,
            "c": 0.028,
            "d": 0.043,
            "e": 0.127,
            "f": 0.022,
            "g": 0.020,
            "h": 0.061,
            "i": 0.070,
            "j": 0.0015,
            "k": 0.0077,
            "l": 0.040,
            "m": 0.024,
            "n": 0.067,
            "o": 0.075,
            "p": 0.019,
            "q": 0.0009,
            "r": 0.060,
            "s": 0.063,
            "t": 0.091,
            "u": 0.028,
            "v": 0.0098,
            "w": 0.024,
            "x": 0.0015,
            "y": 0.020,
            "z": 0.00074
        }
        super().__init__(mapping)
class EnglishInternalDigraphFrequency(LetterFrequency):
    def __init__(self):
        mapping = {
            "th": 5532,
            "he": 4657,
            "in": 3429,
            "er": 3420,
            "an": 3005,
            "re": 2465,
            "nd": 2281,
            "at": 2155,
            "on": 2086,
            "nt": 2058,
            "ha": 2040,
            "es": 2033,
            "st": 2009,
            "en": 2005,
            "ed": 1942,
            "to": 1904,
            "it": 1822,
            "ou": 1820,
            "ea": 1720,
            "hi": 1690,
            "is": 1660,
            "or": 1556,
            "ti": 1231,
            "as": 1211,
            "te": 985,
            "et": 704,
            "ng": 668,
            "of": 569,
            "al": 341,
            "de": 332,
            "se": 300,
            "le": 298,
            "sa": 215,
            "si": 186,
            "ar": 157,
            "ve": 148,
            "ra": 137,
            "ld": 64,
            "ur": 60
        }
        super().__init__(mapping)
class EnglishInternalTrigraphFrequency(LetterFrequency):
    def __init__(self):
        mapping = {
            "the": 23135851162,
            "and": 12997637966,
            "tha": 10145008397,
            "ent": 9842209243,
            "ion": 9733958986,
            "tio": 8693305113,
            "for": 7577474496,
            "nde": 6842214457,
            "has": 6636915075,
            "nce": 6309134620,
            "edt": 6096607422,
            "tis": 5933321709,
            "oft": 5609594409,
            "sth": 5349762197
        }
        super().__init__(mapping)
class EnglishInternalDoubleLetterFrequency(LetterFrequency):
    def __init__(self):
        mapping = {
            "aa": 1,
            "bb": 1,
            "cc": 4,
            "dd": 13,
            "ee": 48,
            "ff": 11,
            "gg": 4,
            "hh": 6,
            "ii": 1,
            "jj": 0,
            "kk": 0,
            "ll": 56,
            "mm": 5,
            "nn": 8,
            "oo": 36,
            "pp": 10,
            "qq": 0,
            "rr": 14,
            "ss": 43,
            "tt": 56,
            "uu": 0,
            "vv": 0,
            "ww": 2,
            "xx": 0,
            "yy": 2,
            "zz": 0
        }
        super().__init__(mapping)

# Starting Monograph Frequencies
class EnglishStartingMonographFrequency(LetterFrequency):
    def __init__(self):
        mapping = {
            "a": 0.117,
            "b": 0.044,
            "c": 0.052,
            "d": 0.032,
            "e": 0.028,
            "f": 0.040,
            "g": 0.016,
            "h": 0.042,
            "i": 0.073,
            "j": 0.0051,
            "k": 0.0086,
            "l": 0.024,
            "m": 0.038,
            "n": 0.023,
            "o": 0.076,
            "p": 0.043,
            "q": 0.0022,
            "r": 0.028,
            "s": 0.067,
            "t": 0.160,
            "u": 0.012,
            "v": 0.0082,
            "w": 0.055,
            "x": 0.00045,
            "y": 0.0076,
            "z": 0.00045
        }
        super().__init__(mapping)

# Internal Word Frequencies
class EnglishInternalWordFrequency(LetterFrequency):
    def __init__(self):
        mapping = {
            "the": 23135851162,
            "of": 13151942776,
            "and": 12997637966,
            "to": 12136980858,
            "a": 9081174698,
            "in": 8469404971,
            "for": 5933321709,
            "is": 4705743816,
            "on": 3750423199,
            "that": 3400031103,
            "by": 3350048871,
            "this": 3228469771,
            "with": 3183110675,
            "you": 2996181025,
            "it": 2813163874,
            "not": 2633487141,
            "or": 2590739907,
            "be": 2398724162,
            "are": 2393614870,
            "from": 2275595356,
            "at": 2272272772,
            "as": 2247431740,
            "your": 2062066547,
            "all": 2022459848,
            "have": 1564202750,
            "new": 1551258643,
            "more": 1544771673,
            "an": 1518266684,
            "was": 1483428678,
            "we": 1390661912,
            "will": 1356293641,
            "home": 1276852170,
            "can": 1242323499,
            "us": 1229112622,
            "about": 1226734006,
            "if": 1134987907,
            "page": 1082121730,
            "my": 1059793441,
            "has": 1046319984,
            "search": 1024093118,
            "free": 1014107316,
            "but": 999899654,
            "our": 998757982,
            "one": 993536631,
            "other": 978481319,
            "do": 950751722,
            "no": 937112320,
            "information": 932594387,
            "time": 908705570,
            "they": 883223816,
            "site": 844310242,
            "he": 842847219,
            "up": 829969374,
            "may": 827822032,
            "what": 812395582,
            "which": 810514085,
            "their": 782849411,
            "news": 755424983,
            "out": 741601852,
            "use": 719980257,
            "any": 710741293,
            "there": 701170205,
            "see": 681410380,
            "only": 661844114,
            "so": 661809559,
            "his": 660177731
        }
        super().__init__(mapping)

# Starting Word Frequencies
class EnglishStartingWordFrequency(LetterFrequency):
    def __init__(self):
        raise NotImplementedError
        mapping = {}
        super().__init__(mapping)


