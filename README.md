> **Created by N1ck, 2024**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green) [![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/n1ck_dv) [![Steam](https://img.shields.io/badge/steam-%23000000.svg?style=for-the-badge&logo=steam&logoColor=white)](https://steamcommunity.com/id/n1ck_dv/)


![USA](https://cdn2.steamgriddb.com/file/sgdb-cdn/icon/8b3bac12926cc1d9fb5d68783376971d/32/256x256.png)

## Дисклеймер
> Данный алгоритм предоставлен исключительно  в ознакомительных и/или образовательных целях. Автор не несет никакой ответсвенности за последствия внедрения данного алгоритма в Ваши проекты и/или продукты коммерческого характера.

# DES (Data Encryption Standard)
##### Алгоритм для симметричного шифрования, разработанный фирмой IBM и утверждённый правительством США в 1977 году как официальный стандарт (FIPS 46-3). Размер блока для DES равен 64 битам. В основе алгоритма лежит сеть Фейстеля с 16 циклами (раундами) и ключом, имеющим длину 56 бит. Алгоритм использует комбинацию нелинейных (S-блоки) и линейных (перестановки E, IP, IP-1) преобразований.
### Полезные ссылки:
1. [AES](https://ru.wikipedia.org/wiki/DES "Wikipedia")
2. [Лекция Шакурского М. В. по криптографическому стандарту AES](https://disk.yandex.ru/i/LjTqyCtlKiAY0Q "Яндекс.Диск")
3. [Отчет с подробным описанием работы программы](https://disk.yandex.ru/i/kYd8p2-LD08g0g "Яндекс.Диск")

### Описание вспомогательных функций
1. `permute(block, table)`: Эта функция применяет перестановку к блоку данных на основе таблицы перестановок.
2. `split(input)`: Эта функция разбивает входную строку на две равные части.
3. `xor(bits1, bits2)`: Выполняет операцию XOR между двумя строками битов.
4. `left_shift(bit_string, shift_count)`: Сдвигает строку битов влево на указанное количество позиций.

**_Генерация подключей:_**

5. `generate_subkeys(key)`: Эта функция создает 16 48-битных подключей на основе 64-битного ключа. Она использует таблицы перестановок PC1 и PC2, а также таблицу сдвигов LEFT_SHIFTS для создания каждого подключа.

**_Шифрование:_**

6. `sbox_substitution(input, sbox)`: Это функция преобразует 6-битный вход в 4-битный выход на основе заданной S-бокс таблицы.
7. `f_function(right, subkey)`: Это функция расширяет 32-битный вход до 48 бит, затем выполняет операцию XOR с подключом, применяет 8 S-бокс таблиц к результату и затем применяет P-перестановку.
8. `des_encrypt(plain_text_bits, key)`: Эта функция реализует основной алгоритм шифрования DES. Она применяет начальную перестановку, выполняет 16 раундов шифрования, используя подключи, и затем применяет итоговую перестановку.

![alt-текст](https://slideplayer.com/slide/4832841/15/images/18/DES+Encryption+The+basic+process+in+enciphering+a+64-bit+data+block+using+the+DES%2C+shown+on+the+left+side%2C+consists+of%3A.jpg "Общая структура работы алгоритма DES:")

### Пояснения к работе программы
Программа состоит из нескольких файлов: `ВES.py, main.py, lib.py, test.py`.
В файле DES реализован основной криптографический алгоритм со всеми функциями.
Файл `test.py` содержит в себе функцию для проверки и вывода сгенерированных раундовых ключей (16)
В файле `lib.py` указаны основные матричные постоянные: `IP, INV_IP, S, E, P, PC1, PC2`.
Файл `main.py` демонстрирует работу алгоритма на данных, вводимых с клавиатуры.

## License

MIT

**Free Software, GLHF!**
