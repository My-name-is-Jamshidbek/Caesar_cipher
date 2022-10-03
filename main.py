class Ceaser_cipher():
    def __init__(self,n):
        self.n= n
        self.e_t = False
        self.d_t = False
        self.harflar = \
            [
                'a',
                'b',
                'c',
                'd',
                'e',
                'f',
                'g',
                'h',
                'i',
                'j',
                'k',
                'l',
                'm',
                'n',
                'o',
                'p',
                'q',
                'r',
                's',
                't',
                'u',
                'v',
                'w',
                'x',
                'y',
                'z',
            ]

    def decoder_alphabet(self):
        n = self.n
        harflar = self.harflar
        m = {}
        m1 = harflar[n:]
        m1+=harflar[:n]
        for i in range(26):
            m[harflar[i]]=m1[i]
        self.d_alphabet = m
        return m

    def encoder_alphabet(self):
        n = self.n
        harflar = self.harflar
        m = {}
        m1 = harflar[n:]
        m1+=harflar[:n]
        for i in range(26):
            m[m1[i]]=harflar[i]
        self.e_alphabet = m
        return m
    def encod(self,text):
        if self.e_t is not True:
            self.encoder_alphabet()
            self.e_t = True
        n = 0
        text1 = ''
        for i in text:
            try:
                if i.isalpha():
                    if i.isupper():
                        text1 += str(self.e_alphabet[i.lower()]).upper()
                    else:
                        text1 += self.e_alphabet[i]
                else:
                    text1 += i
            except:
                text1+=i
            n += 1
        self.result_encode = text1
        return text1

    def decod(self, text):
        if self.d_t is not True:
            self.decoder_alphabet()
            self.d_t = True
        n = 0
        text1 = ''
        for i in text:
            try:
                if i.isalpha():
                    if i.isupper():
                        text1 += str(self.d_alphabet[i.lower()]).upper()
                    else:
                        text1 += self.d_alphabet[i]
                else:
                    text1 += i
            except:
                text1+=i
            n += 1
        self.result_decode = text1
        return text1

