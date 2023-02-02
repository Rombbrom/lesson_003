# zoo_pets = [
#     'lion', 'skunk',
#     'elephant', 'horse',
# ]
#
# for i, animal in enumerate(zoo_pets):
#     print(i, animal)
#
# zoo_pets = [
#      'lion', 'skunk',
#      'elephant', 'horse',
#     ]
# for animal in zoo_pets :
#      print(animal)
#      del zoo_pets[0]
# print(zoo_pets)

# for i in range(100, 600, 50):
#     print(i)

# for i in range(12, 76, 3):
#     print(i)
#
# for i in range(10):
#     print(i)

# animal = 'lion'
# for char in animal :
#     print(char)
#
# zoo_pets = [
#     'lion', 'skunk',
#     'elephant', 'horse',
# ]
# for animal in zoo_pets:
#     for char in animal:
#         print(char)
#     print(animal)

# zoo_pet_mass = {
#     'lion': 300,
#     'skunk': 5,
#     'elephant': 5000,
#     'horse': 400,
# }
# total_mass = 0
# for animal in zoo_pet_mass:
#     print(animal, zoo_pet_mass[animal])
#     total_mass += zoo_pet_mass[animal]
# print('Общая масса животных', total_mass)
#
# total_mass = 0
# for animal, mass in zoo_pet_mass.items():
#     print(animal, mass)
#     total_mass += mass
# print('Общая масса животных', total_mass)
#
# total_mass = 0
# for mass in zoo_pet_mass.values():
#     print(mass)
#     total_mass += mass
# print('Общая масса животных', total_mass)

# values - только значения
# items - только вес

def some_func() :
    print('Привет! Я функция')


#
#
# some_func()
# some_func()
# some_func()
# some_func()
# some_func()

# my_list = [3, 14, 15, 92, 6]
# for element in my_list:
#     some_func()

# for _ in range(10):
#     some_func()

# def func_with_params(param, param2):
#     print('Функцию вызвали с параметром', param, param2)

# def func_with_params(param):
#     print('Функцию вызвали с параметром', param)
#
# my_list = [3, 14, 15, 92, 6]
# for element in my_list:
#     print('Начало цикла')
#     func_with_params(element)
#     print('Конец цикла')

# def power(number, pow):
#     print('Функцию вызвали с параметрами', number, pow)
#     power_value = number ** pow
#     return power_value
#
#
# my_list = [3, 14, 15, 92, 6]
# for element in my_list:
#     result = power(number=element, pow=10)
#     print(result)

# def some_func():
#     print("я ничего не верну")
#
# result = some_func()
# print(result)

# def create_default_user():
#     name = 'Василий'
#     age = 27
#     return name, age,
#
#
# user_name, user_age = create_default_user()
# print(user_name, user_age)

# def my_function():
#     """Не делаем ничего, но документируем.
#
#     Нет, правда, эта функция ничего не делает.
#     """
#     pass
# """ lkbnbld""" документирование обязательно в тройных кавычках!
#
# print(my_function.__doc__)


# def multiplay(number_1, number_2):
#     print('Функцию вызвали с параметрами', number_1, number_2)
#     if isinstance(number_1,int):
#         value = number_1 ** number_2
#         return value
#     return 'error'
#
#
# # print(multiplay(number_1=42, number_2=27))
# print(multiplay(number_1='привет! ', number_2=34))

# def elephant_to_free(some_list):
#     elephant_found = 'elephant' in some_list
#     if elephant_found:
#         some_list.remove('elephant')
#         print('Слон на свободе!!!')
#     return elephant_found
#
#
# zoo = ['lion', 'elephant', 'monkey', 'skunk', 'horse', 'elephant']
# # zoo = ('lion', 'elephant', 'monkey', 'skunk', 'horse', 'elephant') не будет работать с круглыми скобками, attributeError
# elephant_to_free(some_list=zoo)
# print(zoo)
#
# elephant_to_free(some_list=zoo)
# print(zoo)
#
# elephant_to_free(some_list=zoo)
# print(zoo)
