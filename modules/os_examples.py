#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

HORIZONTAL_LINE = '----------------------------------'

print('Имя системы: '.format(os.name))
print(HORIZONTAL_LINE)

print('Переменные окружения: ')
env_vars = os.environ
for key in env_vars:
    print('{0}: {1}'.format(key, env_vars[key]))
print(HORIZONTAL_LINE)

print('Имя текущего пользователя системы: {0}'.format(os.getlogin()))
print(HORIZONTAL_LINE)

print('Текущий id процесса: {0}'.format(os.getpid()))
print(HORIZONTAL_LINE)

print('Имею ли я права на запись в C:\Windows\System32? {0}'.format(os.access('C:\Windows\System32', os.W_OK)))
print(HORIZONTAL_LINE)

print('Вы находитесь в директории: {0}'.format(os.getcwd()))
os.chdir('C:\\')
print('Теперь вы находитесь в директории: {0}'.format(os.getcwd()))
print(HORIZONTAL_LINE)

print('Список файлов и директорий в папке C:\\')
files_and_directories = os.listdir('C:\\')
for i in files_and_directories:
    print(i)
print(HORIZONTAL_LINE)

print('Создание директории С:\Users\Username\Desktop\Test')
os.mkdir('{0}\Desktop\{1}'.format(os.environ['USERPROFILE'], 'Test'))
