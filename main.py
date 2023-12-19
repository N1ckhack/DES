from DES import encrypt_string as DES

key = [int(x) for x in format(0x0e329232ea6d0d73, '064b')]
print('Key: ', *key)

input_string = input("Введите строку для шифрования (8 символов): ")

encrypted = DES(input_string, key)
print(f"Зашифрованная строка: {hex(encrypted)}")
