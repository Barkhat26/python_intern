#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Модуль sys обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python.

import sys

HORIZONTAL_LINE = '----------------------------------'

print('Аргументы командной строки:')
args = sys.argv
for i in range(len(args)):
    print('[{0}] {1}'.format(i, args[i]))
print(HORIZONTAL_LINE)

print('Порядок байтов: {0}-endian'.format(sys.byteorder))
print(HORIZONTAL_LINE)

print('Доступные модули:')
available_modules = sys.builtin_module_names
for i in available_modules:
    print(i)
print(HORIZONTAL_LINE)

print('Каталог установки Python: {0}'.format(sys.exec_prefix))
print(HORIZONTAL_LINE)

print('Путь к интерпретатору Python: {0}'.format(sys.executable))
print(HORIZONTAL_LINE)

print('Испльзуемая кодировка: {0}'.format(sys.getdefaultencoding()))
print(HORIZONTAL_LINE)

print('Кодировка файловой системы: {0}'.format(sys.getfilesystemencoding()))
print(HORIZONTAL_LINE)

print('Ссылки на объекты:')
object1 = 45
object2 = 'Hello'
print('object1: {0}'.format(sys.getrefcount(object1)))
print('object1: {0}'.format(sys.getrefcount(object2)))
print(HORIZONTAL_LINE)

print('Лимит рекурсии: {0}'.format(sys.getrecursionlimit()))
print(HORIZONTAL_LINE)

print('Размер объекта object1: {0} байт'.format(sys.getsizeof(object1)))
print('Размер объекта object2: {0} байт'.format(sys.getsizeof(object2)))
print(HORIZONTAL_LINE)

print('Версия Windows:')
print('\tmajor: {0}'.format(sys.getwindowsversion().major))
print('\tminor: {0}'.format(sys.getwindowsversion().minor))
print('\tbuild: {0}'.format(sys.getwindowsversion().build))
print(HORIZONTAL_LINE)

print('Пути поиска модулей:')
for i in sys.path:
    print(i)
print(HORIZONTAL_LINE)

print('Информация об ОС: {0}'.format(sys.platform))
print(HORIZONTAL_LINE)

print('Стандартный ввод: {0}'.format(sys.stdin))
print('Стандартный вывод: {0}'.format(sys.stdout))
print('Стандартный поток ошибок: {0}'.format(sys.stderr))
print(HORIZONTAL_LINE)

print('Версия Python: {0}'.format(sys.version))
print('\tmajor: {0}'.format(sys.version_info.major))
print('\tminor: {0}'.format(sys.version_info.minor))
print('\tmicro: {0}'.format(sys.version_info.micro))



