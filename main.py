__author__ = 'Aface'

from encryption.crypters import *
from encryption.analyzers import *

cc = CaesarCrypter()
vc = VigenereCrypter()
ca = CaesarAnalyzer()
va = VigenereAnalyzer()

ans = None
while True:
    while ans not in ['1', '2', '3', '4']:
        ans = input("""
0) Выход
1) Шифр Цезаря
2) Шифр Виженера
3) Анализ шифра Цезаря
4) Анализ шифра Виженера
""")
    file_name = input("\nВведите название файла:\n")
    input_file = open(file_name, 'r')
    if ans == '0':
        break
    elif ans == '1':
        output_file = open("enc_" + file_name, 'w')
        offset = int(input("\nВыберите смещение:\n"))
        for line in input_file:
            output_file.write(cc.encrypt(line, offset))
        output_file.close()
    elif ans == '2':
        output_file = open("enc_" + file_name, 'w')
        key = input("\nВведите ключ:\n")
        for line in input_file:
            output_file.write(vc.encrypt(line, key))
        print(vc.square)
        output_file.close()
    elif ans == '3':
        output_file = open("dec_" + file_name, 'w')
        for line in input_file:
            ca << line
        ca.analyze()
        key = ca.find_key()
        print(key)
        input_file.seek(0)
        for line in input_file:
            output_file.write(cc.encrypt(line, -1 * key))
        output_file.close()
    else:
        #output_file = open("dec_" + file_name, 'w')
        text = ""
        for line in input_file:
            check = False
            for c in line:
                text += c
                if (len(text) == 40):
                    check = True
                    break
            if (check):
                break
        print(va.make_matches_table(text))
    input_file.close()
    ans = None