__author__ = 'Aface'


class Error(BaseException):
    @staticmethod
    def message():
        return "Недопустимый символ!"


class CaesarCrypter():
    def __init__(self, alphabet=None):
        if alphabet is None:
            self.alphabet = []
            for i in range(26):
                self.alphabet.append(chr(97 + i))
        else:
            self.alphabet = alphabet

    def encrypt(self, text, offset):
        encrypt_text = ""
        for i in range(len(text)):
            if text[i] not in self.alphabet:
                encrypt_text += text[i]
            else:
                current_number = ord(text[i]) + offset
                if current_number > 122:
                    current_number -= 26
                if current_number < 97:
                    current_number += 26
                encrypt_text += chr(current_number)
        return encrypt_text


class VigenereSquare():
    @staticmethod
    def __offset(chars):
        temp = chars[0]
        for i in range(len(chars) - 1):
            chars[i] = chars[i + 1]
        chars[len(chars) - 1] = temp

    def __init__(self, alphabet=None):
        from random import shuffle
        from copy import copy

        if alphabet is None:
            self.alphabet = []
            for i in range(26):
                self.alphabet.append(chr(97 + i))
        else:
            self.alphabet = alphabet

        shuffled_alphabet = copy(self.alphabet)
        shuffle(shuffled_alphabet)

        self.square = []
        for i in range(len(shuffled_alphabet)):
            self.square.append(copy(shuffled_alphabet))
            self.__offset(shuffled_alphabet)

    def __str__(self):
        result = ""
        for i in range(len(self.square)):
            for j in range(len(self.square[0])):
                result += str("'" + self.square[i][j] + "'" + ' ')
            result += '\n'
        return result

    def __getitem__(self, item):
        i, j = item
        return self.square[i][j]

    def find_index(self, c, number_of_str=None):
        return self.alphabet.index(c) if number_of_str is None else self.square[number_of_str].index(c)


class VigenereCrypter():
    def __init__(self, square=None):
        self.square = square if square is not None else VigenereSquare()

    def __get_equal_key(self, key, length):
        equal_key = ""
        for i in range(length):
            cur = i % len(key)
            equal_key += key[i % len(key)]
            if key[i % len(key)] not in self.square.alphabet:
                raise Error
        return equal_key

    def encrypt(self, text, key):
        equal_key = self.__get_equal_key(key, len(text))
        encoded_text = ""
        for i in range(len(text)):
            if text[i] not in self.square.alphabet:
                encoded_text += text[i]
            else:
                #current_index = self.square.find_index(text[i], 0)
                current_index = self.square.find_index(text[i])
                encoded_text += self.square.alphabet[self.square.find_index(equal_key[i], current_index)]
        return encoded_text


if __name__ == "__main__":
    vc = VigenereCrypter()



