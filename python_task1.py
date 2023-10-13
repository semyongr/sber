import re

def GoodNumber(string):
    pattern = r'(\d{2,4}\\\d{2,5})' #регулярное выражение для поиска особенных номеров
    list_match = re.findall(pattern, string)
    for match in list_match:
        match = match.split("\\")
        if len(match[0]) < 4:
            match[0] = ("0"*(4 - len(match[0]))) + match[0] #добавление нулей к первой части номера
        if len(match[1]) < 5:
            match[1] = ("0"*(5 - len(match[1]))) + match[1] #добавление нулей ко второй части номера
        match = "\\".join(match)
        print(match)

string = input("Введите строку: ") #Адрес 5467\456. Номер 405\549
GoodNumber(string)