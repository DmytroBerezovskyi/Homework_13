num_input = int(input('Введите десятичное число: '))
base_input = int(input('Введите систему исчисления (2-36): '))
while True:
    if 2 <= base_input <= 32:
        break
    else:
        base_input = int(input('Введите систему исчисления (2-36): '))

lst = []

def calculator(num, base):

    newNum = ''
    if base == 12 or base == 16 or base == 32:
        pass
    else:
        while num > 0:
            newNum = str(num % base) + newNum
            num //= base

        print(newNum)


    if base == 12:
        while num > 0:
            if num % base == 10:
                lst.append('A')
                num //= base
                continue
            if num % base == 11:
                lst.append('B')
                num //= base
                continue
            lst.append(str(num % base))
            num //= base
            if num < base:
                if (num == 10):
                    lst.append('A')
                    break
                if (num == 11):
                    lst.append('B')
                    break


    if base == 16:
        while num > 0:
            if num % base == 10:
                lst.append('A')
                num //= base
                continue
            if num % base == 11:
                lst.append('B')
                num //= base
                continue
            if num % base == 12:
                lst.append('C')
                num //= base
                continue
            if num % base == 13:
                lst.append('D')
                num //= base
                continue
            if num % base == 14:
                lst.append('E')
                num //= base
                continue
            if num % base == 15:
                lst.append('F')
                num //= base
                continue
            lst.append(str(num % base))
            num //= base
            if num < base:
                if (num == 10):
                    lst.append('A')
                    break
                if (num == 11):
                    lst.append('B')
                    break

    lst.reverse()
    return lst

calculator(num_input, base_input)
print(''.join(lst))
