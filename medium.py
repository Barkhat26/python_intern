#!/usr/bin/env python
# -*- coding: utf-8 -*-


def prime_time(num):
    i = 2
    while i <= num / 2:
        if num % i == 0:
            return 'false'
        i += 1
    return 'true'


def run_length(str):
    res = ''
    prev = ''
    cnt = 0
    for ch in str:
        if ch == prev:
            cnt += 1
        else:
            if cnt > 0:
                res += '%d%s' % (cnt, prev)
            prev = ch
            cnt = 1
    res += '%d%s' % (cnt, prev)
    return res


def prime_mover(num):
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def palindrome_two(s):
  s = ''.join([c.lower() for c in s if c.isalpha()])
  return 'true' if s == s[::-1] else 'false'


def division(num1,num2):
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


def string_scramble(str1,str2):
    for c in str2:
        if str1.find(c) == -1:
            return 'false'
    return 'true'


def arith_geo_2(arr):
    arith_step = arr[1] - arr[0]
    geo_step = arr[1] / arr[0]
    is_arith = True
    is_geo = True
    for i in range(len(arr) - 1):
        is_arith = False if arr[i] != arr[i+1] - arith_step else True
        is_geo = False if arr[i] != arr[i+1] / geo_step else True
    return 'Arithmetic' if is_arith else 'Geometric' if is_geo else '-1'


def array_addition(arr):
    from itertools import combinations
    arr_without_max = [x for x in arr if x != max(arr)]
    for L in range(2, len(arr_without_max)+1):
        for subset in combinations(arr_without_max, L):
            if sum(subset) == max(arr):
                return 'true'
    return 'false'


def binary_converter(s):
    return int(s, 2)


def letter_count(s): 
    max_count = 1
    greatest = '-1'
    for word in s.split():
        for ch in word:
            if word.count(ch) > max_count:
                max_count = word.count(ch)
                greatest = word
    return greatest


def caesar_cipher(s,num):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_text = ''
    for c in s:
        if c.isalpha():
            cipher_text += alphabet[(alphabet.index(c.lower()) + num) % 26] if c.islower() \
                else alphabet[(alphabet.index(c.lower()) + num) % 26].upper()
        else:
            cipher_text += c
    return cipher_text


def simple_mode(arr):
    max_count = 1
    mode = arr[0]
    for i in arr[1:]:
        if arr.count(i) > max_count:
            max_count = arr.count(i)
            mode = i
    return mode if max_count != 1 else -1


def consecutive(arr):
    arr.sort()
    numbers_between = 0
    for i in xrange(1, len(arr)):
        if arr[i] - arr[i - 1] != 0:
            numbers_between += arr[i] - arr[i - 1] - 1
    return numbers_between


def formatted_division(num1,num2):
    return "{:,.4f}".format(float(num1) / float(num2))


def counting_minutes(s): 
    num1, num2 = s.split('-')
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


def permutation_step(num):
    a = list(str(num))
    n = len(a)
    k = n - 2
    while k >= 0 and a[k] >= a[k+1]:
        k -= 1
    if k == -1:
        return -1
    t = n - 1
    while t >= k + 1 and a[k] >= a[t]:
        t -= 1
    a[k], a[t] = a[t], a[k]
    i = k + 1
    while i <= (n + k) / 2:
        t = n + k - i
        a[i], a[t] = a[t], a[i]
        i += 1
    return ''.join(a)

