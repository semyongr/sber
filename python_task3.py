import itertools

def MaxCombinatedNumber(list):
    max_number = 0
    for i in itertools.permutations(list): #формирование всех возможных комбинаций из полученного списка строк
        combinated_number = int(''.join(i)) #преобразование комбинации строк в число
        if combinated_number > max_number:
            max_number = combinated_number
    return max_number


list = []
count_items = int(input('Введите количество чисел в списке: '))
for i in range(count_items):
    list_item = input(f'Введите {i+1} число: ')
    list.append(list_item)

print(MaxCombinatedNumber(list))






