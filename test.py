from DES import *

def test_trace():
    # TODO: Тестирование генерации ключей
    key = [int(x) for x in format(0x0e329232ea6d0d73, '064b')]
    subkeys = generate_subkeys(key)
    for idx, sk in enumerate(subkeys, 1):
        print(f"K{idx}: {''.join(map(str, sk))}")

if __name__ == '__main__':
    test_trace()
