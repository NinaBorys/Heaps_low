#! /usr/bin/python3.3
# -*- coding:utf-8 -*-

from collections import Counter

def prepare_text(z):
    """Deletes all non-alphabet symbols from text"""
    alphabet_str = "абвгдежзийклмнопрстуфхцчшщъыьэюя "
    z = list(' '.join(z.lower().split()))
    for i,k in enumerate(z):
        if k not in alphabet_str:
            z[i] = ''
    return ''.join(z)

def main():

    with open('book2.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    text = prepare_text(text)
    result = Counter(text.split()).items()
    print(result)



if __name__ == '__main__':
    main()
