first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third= int(input('Введите третье число: '))

if first == second and first == third:
    print('Найдено 3 совпадения )) Ура!')
elif first == second or first == third or second == third:
    print('Найдено 2 совпадения )')
else:
    print('Совпадения не обнаружены ((')