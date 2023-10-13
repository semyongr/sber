def DistanceBtwnATMs(n,k,list):
    max_list_L = (sorted(list,reverse=True))[:k]  #отсортированный список максимальных расстояний
    for i in max_list_L:
        pos = list.index(i) #индекс значения расстояния в исходном списке
        list[pos:pos + 1] = (int(i/2), int(i/2)) #замена исходного знач. расстояния на новые два значения

    for i in list:
        print(i)


nk = input("Введите n и k через пробел: ").split(' ')
n = int(nk[0])
k = int(nk[1])
if k > n:
    print('Некорректное число k')
else:
    list = []
    for i in range(n):
        list_item = int(input(f'Введите L{i+1}: '))
        list.append(list_item)
DistanceBtwnATMs(n, k, list)