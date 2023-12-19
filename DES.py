from lib import *
import test

def permute(block, table):
    return [block[x - 1] for x in table]

def split(block):
    n = len(block)
    return block[:n // 2], block[n // 2:]

def xor(bits1, bits2):
    return [x ^ y for x, y in zip(bits1, bits2)]

def des_round(data, key):
    L, R = split(data)
    new_R = xor(L, feistel(R, key))
    return R + new_R

def feistel(R, subkey):
    expanded = permute(R, E)
    xored = xor(expanded, subkey)
    substituted = substitute(xored)
    return permute(substituted, P)

def substitute(xored):
    substituted = []
    for i in range(8):
        block = xored[i * 6:i * 6 + 6]
        row = int(str(block[0]) + str(block[5]), 2)
        col = int(''.join([str(x) for x in block[1:5]]), 2)
        substituted.extend(format(S[i][row][col], '04b'))
    return [int(x) for x in ''.join(substituted)]

# TODO: Левый сдвиг каждого полублока (1 или 2 позиции в зависимости от раунда)
LEFT_SHIFTS = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]

def left_shift(bits, count):
    return bits[count:] + bits[:count]

def generate_subkeys(key):
    key_permuted = permute(key, PC1)
    L, R = split(key_permuted)
    subkeys = []
    for shift in LEFT_SHIFTS:
        L = left_shift(L, shift)
        R = left_shift(R, shift)
        subkey = permute(L + R, PC2)
        subkeys.append(subkey)
    return subkeys

def des(input_block, key,
        decrypt = False):
    # 1. Начальная перестановка
    data = permute(input_block, IP)

    # 2. Генерация подключей
    subkeys = generate_subkeys(key)

    # Если дешифрование, то нужно использовать подключи в обратном порядке
    if decrypt:
        subkeys = subkeys[::-1]

    # 3. 16 раундов DES
    for subkey in subkeys:
        data = des_round(data, subkey)

    # Переворот L и R перед конечной перестановкой при дешифровании
    if decrypt:
        data = data[32:] + data[:32]

    # 4. Конечная перестановка
    output_block = permute(data, IP_INV)

    return output_block

def string_to_bits(s):
    return [int(b) for char in s for b in format(ord(char), '08b')]

def bits_to_string(bits):
    return ''.join([chr(int(''.join(map(str, bits[i:i + 8])), 2)) for i in range(0, len(bits), 8)])

def encrypt_string(input_string, key_bits):
    # Преобразование строки в биты
    plaintext_bits = string_to_bits(input_string)
    # Шифрование при помощи DES
    cipher_bits = des(plaintext_bits, key_bits)
    # Преобразование битов в строку и возврат результата
    return ''.join(map(str, cipher_bits))

def decrypt_string(cipher_bits_str, key_bits):
    # Преобразование строки битов обратно в список
    cipher_bits = [int(b) for b in cipher_bits_str]
    # Дешифрование при помощи DES
    plaintext_bits = des(cipher_bits, key_bits,
                         decrypt = True)
    # Преобразование битов в строку и возврат результата
    return bits_to_string(plaintext_bits)

if __name__ == '__main__':
    test.test_trace()