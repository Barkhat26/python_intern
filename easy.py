#!/usr/bin/env python
# -*- coding: utf-8 -*-

def first_reverse(str):
    return "".join(reversed(str))


def first_factorial(n):
    from math import factorial
    return factorial(n)


def longest_word(str):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    word_list = [word.strip(punctuation) for word in str.split()]
    return max(word_list, key=len)


def letter_changes(str):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    vowels = 'aeiou'
    for i in str:
        if i in lowercase:
            lower_char = lowercase[(lowercase.find(i) + 1) % len(lowercase)]
            if lower_char in vowels:
                result += lower_char.upper()
            else:
                result += lower_char
        elif i in uppercase:
            result += uppercase[(uppercase.find(i) + 1) % len(uppercase)]
        else:
            result += i
    return result


def simple_adding(num):
    return sum(range(1, num + 1))


def letter_capitalize(str):
    word_list_capitalized = [word.capitalize() for word in str.split()]
    return " ".join(word_list_capitalized)


def simple_symbols(str):
    if str[0].isalpha() or str[-1].isalpha():
        return 'false'

    for i in range(1, len(str) - 1):
        if str[i].isalpha() and (str[i-1] == '+' and str[i+1] == '+'):
            return 'true'

    return 'false'

def check_nums(num1, num2):
    return 'true' if num2 > num1 else 'false' if num2 < num1 else '-1'


def time_convert(num):
    return ":".join([str(num / 60), str(num % 60)])


def alphabet_soup(str):
    return "".join(sorted(str))


def ab_check(str):
    for i in range(len(str)-4):
        if str[i] == 'a':
            if str[i+4] == 'b':
                return 'true'
    return 'false'


def vowel_count(str):
    vowels = 'aoeiu'
    return len([char for char in str if char.lower() in vowels])


def word_count(str):
    return len(str.split())


def ex_oh(str):
    return 'true' if str.count('o') == str.count('x') else 'false'


def palindrome(str):
    str = ''.join([c for c in str if c.isalpha()])
    return 'true' if str == str[::-1] else 'false'


def arith_geo(arr):
    arith_step = arr[1] - arr[0]
    geo_step = arr[1] / arr[0]
    is_arith = True
    is_geo = True

    for i in range(len(arr) - 1):
        is_arith = False if arr[i] != arr[i+1] - arith_step else True
        is_geo = False if arr[i] != arr[i+1] / geo_step else True
    return 'Arithmetic' if is_arith else 'Geometric' if is_geo else '-1'


def array_addition_1(arr):
    from itertools import combinations
    arr_without_max = [x for x in arr if x != max(arr)]
    for L in range(2, len(arr_without_max)+1):
        for subset in combinations(arr_without_max, L):
            if sum(subset) == max(arr):
                return 'true'
    return 'false'


def letter_count_1(str):
    max_count = 1
    greatest = '-1'
    for word in str.split():
        for ch in word:
            if word.count(ch) > max_count:
                max_count = word.count(ch)
                greatest = word
    return greatest


def second_greatlow(arr):
    arr = sorted(list(set(arr)))
    return str(arr[1]) + " " + str(arr[-2])


def division_stringified(num1, num2):
    from math import ceil
    result = int(round(float(num1) / float(num2)))
    return result if len(str(result)) < 4 else "{:,d}".format(result)


def counting_minutes_1(str):
    num1, num2 = str.split('-')
    num1 = {'hrs': int(num1.split(':')[0]),
            'mins': int(num1.split(':')[1][:2]),
            'notation': num1[-2:]}
    num2 = {'hrs': int(num2.split(':')[0]),
            'mins': int(num2.split(':')[1][:2]),
            'notation': num2[-2:]}
    if num1['notation'] == num2['notation']:
        if (num1['hrs'] * 60 + num1['mins']) < (num2['hrs'] * 60 + num2['mins']):
            return (num2['hrs'] * 60 + num2['mins']) - (num1['hrs'] * 60 + num1['mins'])
        else:
            return (num2['hrs'] * 60 + num2['mins']) - (num1['hrs'] * 60 + num1['mins']) + 1440
    else:
        return (num2['hrs'] * 60 + num2['mins']) - (num1['hrs'] * 60 + num1['mins']) + 720


def mean_mode(arr):
    mean = sum(arr) / len(arr)
    max_count = 1
    mode = arr[0]
    for i in arr[1:]:
        if arr.count(i) > max_count:
            max_count = arr.count(i)
            mode = i
    return 1 if mode == mean else 0


def dash_insert(str):
    result_str = str[0]
    prev = str[0]
    for n in str[1:]:
        if (int(n) % 2 == 1) and (int(prev) % 2 == 1):
            result_str += '-'
        result_str += n
        prev = n
    return result_str


def swap_case(str):
    return ''.join([ch.lower() if ch.isupper() else ch.lower() for ch in str])


def number_addition(str):
    only_number_str = ''
    for ch in str:
        only_number_str += ch if ch.isdigit() else ' '
    return sum(map(int, only_number_str.split()))


def third_greatest(strArr):
    return sorted(strArr, key=len, reverse=True)[2]


def powers_of_two(num):
    return 'true' if num & (num-1) == 0 else 'false'


def additive_persistence(num):
    count = 0
    while len(str(num)) > 1:
        num = sum(map(int, list(str(num))))
        count += 1
    return count


def multiplicative_persistence(num):
    count = 0
    while len(str(num)) > 1:
        digits = map(int, list(str(num)))
        num = 1
        for d in digits:
            num *= d
        count += 1
    return count


def off_line_minimum(strArr):
    res = []
    tmp = set()
    for c in strArr:
        if c == 'E':
            minimum = sorted(tmp)[0]
            res.append(minimum)
            tmp.remove(minimum)
        else:
            tmp.add(c)
    return ",".join(res)


