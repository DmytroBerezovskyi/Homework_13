
lst = [int(s) for s in input('Введите пожалуйста список чисел: ').split()]

if len(lst) % 2 == 0:
    for i in range((len(lst))//2):                 # Количество таких обменов будет равно половине длины списка
        lst.insert(len(lst)-i-1, lst.pop(i))
        lst.insert(i, lst.pop(len(lst)-i-2))
    print(lst)

else:
    for i in range((len(lst))):                 # Иначе элементы поменяются местами по-второму кругу
        lst.insert(len(lst)-i-1, lst.pop(i))    # и вернутся в первоначальное положение.
        lst.insert(i, lst.pop(len(lst)-i-2))
    print(lst)

