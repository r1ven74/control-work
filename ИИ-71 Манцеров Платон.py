#сложный уровень, 2 задание

symbol = int(input("кол-во символов в строке"))
line = int(input("кол-во строк"))

byte = symbol * line * 2 * 5  # мы берем символы умножаем на кол-во линий и умножаем на 2 т.к. двухстороняя печать, а затем умножаем на 5 т.к. 32-х смивольный алфавит
print(byte, "байт")
kb = byte / 1024 # переводим байт в килобайты
print(kb, "килобайт")
bit = byte * 8 # переводим байт в бит
print(bit, "бит")