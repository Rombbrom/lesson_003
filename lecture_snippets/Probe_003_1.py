# f1, f2 = 1, 1
# print(f1)
# while f2 < 1000 :
#     print(f2)
#     next_f2 = f1 + f2
#     next_f1 = f2
#     f1, f2 = next_f1, next_f2

# i = 1
# while i < 10:
#     i *= 2
#     print(i)
# else:
#     print('i >= 10')
# print('дотвиданя!')

# my_pets = ['dog', 'hamster', 'hamster', 'hamster', 'hamster', 'hamster', 'hamster', 'hamster', 'hamster', ]
# i = 0
# while i < len(my_pets) :
#     pet = my_pets[i]
#     print('Проверяем ', pet)
#     if pet == 'cat' :
#         print('Ура, кот найден!')
#         break
#     i += 1
# else:
#     print('не нашли')
# print('дотвиданя!')


# my_pets = ['lion', 'dog', 'skunk', 'hamster', 'cat', 'monkey']
# i = -1
# while i < len(my_pets):
#     i += 1
#     if i == 2:
#         continue
#     pet = my_pets[i]
#     print('Проверяем ', pet)
#     if pet == 'cat':
#         print('Ура, кот найден!')
#         break
# print('дотвиданя!')

f1, f2, count = 0, 1, 0
while f2 < 1000000:
    count += 1
    if count > 27:
        print('Итераций больше чем 27. Прерываюсь.')
        break
    f1, f2 = f2, f1 + f2
    if f2 < 1000:
        continue
    print(f2)
else:
    print('Было', count, 'итераций')