__author__ = 'Aface'

class CaesarAnalyzer():
    def __init__(self, alphabet=None, standard_stats=None):
        self.stats = {}
        if standard_stats is None:
            self.standard_stats = {
                'a': 8.369698473393854,
                'b': 1.6206051694445256,
                'c': 1.6495209288070287,
                'd': 5.236352126448525,
                'e': 12.455942234157448,
                'f': 2.4463006071397295,
                'g': 2.4199845296126563,
                'h': 6.6077983157710385,
                'i': 6.229886672115357,
                'j': 0.04989564785895677,
                'k': 0.8869931988674509,
                'l': 4.371479027408856,
                'm': 2.4191179690008466,
                'n': 7.026575133541551,
                'o': 7.807255027875887,
                'p': 1.279864415190169,
                'q': 0.05523183688957646,
                'r': 6.00836641466476,
                's': 6.033861540033276,
                't': 8.924844566391313,
                'u': 2.6098981289588137,
                'v': 0.8050348083715229,
                'w': 2.691628477188476,
                'x': 0.05135511836305788,
                'y': 1.9004586386059137,
                'z': 0.042050993899413296 }
        else:
            self.standard_stats = standard_stats

        self.counter = 0
        if alphabet is not None:
            self.alphabet = alphabet
        else:
            self.alphabet = []
            for i in range(26):
                self.alphabet.append(chr(97 + i))
        self.stats = {c: 0.0 for c in self.alphabet}
        self.replacement_table = {c: c for c in self.alphabet}

    def __lshift__(self, text):
        for i in range(len(text)):
            if text[i] in self.alphabet:
                self.stats[text[i]] += 1
                self.counter += 1

    def analyze(self):
        for key in self.alphabet:
            if self.stats[key] != 0:
                self.stats[key] = 100 * self.stats[key] / self.counter
        for key in self.alphabet:
            index = 0
            dif = 100
            for i in range(len(self.alphabet)):
                current_dif = abs(self.stats[key] - self.standard_stats[self.alphabet[i]])
                if current_dif < dif:
                    dif = current_dif
                    index = i
            self.replacement_table[key] = self.alphabet[index]

    def find_key(self):
        shifts = []
        for key in self.replacement_table:
            shifts.append(ord(key) - ord(self.replacement_table[key]))
        import collections
        c = collections.Counter(shifts)
        return c.most_common(1)[0][0]


    def replace(self, text):
        decrypted_text = ""
        for i in range(len(text)):
            if text[i] in self.replacement_table:
                decrypted_text += self.replacement_table[text[i]]
            else:
                decrypted_text += text[i]
        return decrypted_text


class VigenereAnalyzer():
    @staticmethod
    def __offset(text):
        chars = []
        result = ""
        for i in range(len(text)):
            chars.append(text[i])
        for i in range(len(text) - 1):
            result += chars[i + 1]
        result += text[0]
        return result

    def __init__(self):
        self.standard_index1 = 0.06440
        self.standard_index2 = 0.0667

    def make_matches_table(self, text):
        table = [text, ]
        for i in range(12):
            text = self.__offset(text)
            table.append(text)
        matches = []
        matches_sum = 0
        for i in range(1, len(table)):
            current_matches = 0
            for j in range(len(text)):
                if table[0][j] == table[i][j]:
                    current_matches += 1
                    matches_sum += 1
            matches.append(current_matches)
        for i in range(len(matches)):
            if matches[i] > 0:
                matches[i] /= matches_sum
        return matches

if __name__ == "__main__":
    a = VigenereAnalyzer()
    print(a.make_matches_table("sdfjjsdldlsllkdfjsd"))


