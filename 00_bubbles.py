# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# TODO Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(300, 300)
# radius = 50
# for _ in range(3) :
#     radius += 5
#     sd.circle(center_position=point, radius=radius,width=2)

# TODO Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
#
# def bubble(point, step):
#     radius = 50
#     for _ in range(3) :
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
# point = sd.get_point(300, 300)
# bubble(point=point,step=10)
#
# TODO Нарисовать 10 пузырьков в ряд
# def bubble(point, step):
#     radius = 50
#     for _ in range(3) :
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
# for x in range (100,1100, 100):
#     point = sd.get_point(x, 100)
#     bubble(point=point, step=5)
#
# TODO Нарисовать 3 ряда по 10 пузырьков
# def bubble(point, step):
#     radius = 50
#     for _ in range(3) :
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
# for y in range (100,301, 100):
#     for x in range (100,1001, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=5)
#
# TODO Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# def bubble(point, step):
#     radius = 50
#     for _ in range(3) :
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
# for _ in range (100):
#     point=sd.random_point()
#     bubble(point=point, step=5)

# def bubble(point, step):
#     radius = 50
#     for _ in range(3) :
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
# for _ in range (100):
#     point=sd.random_point()
#     step=random.randint(2,10)
#     bubble(point=point, step=step)
sd.pause()


