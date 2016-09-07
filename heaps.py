#! /usr/bin/python3.3
# -*- coding:utf-8 -*-

from collections import Counter
import matplotlib.pyplot as plt
import csv


def prepare_text(z):
    """Deletes all non-alphabet symbols from text"""
    alphabet_str = "абвгдежзийклмнопрстуфхцчшщъыьэюя "
    z = list(' '.join(z.lower().split()))
    for i,k in enumerate(z):
        if k not in alphabet_str:
            z[i] = ''
    return ''.join(z)


def create_dict(text):
    '''returns list of pairs (step, unique words), dict of unique words from text'''
    res_dict = dict()
    points = list()
    i=0
    for word in text.split():
        if word in res_dict:
            res_dict[word] += 1
        else:
            res_dict[word] = 1
            points.append((i,len(res_dict)))
        i += 1
    res_list = list(res_dict.values())
    res_list.sort(reverse=True)
    return points, res_list


def heaps_plot(points):
    '''plot from points (tuples)'''
    plt.scatter(*zip(*points), linewidth=0.5, color='red', marker='s')
    plt.xlim([-50,250000])
    plt.ylim([-50,40000])
    plt.suptitle('heaps low check')
    plt.show()


def heaps_low_check(write_to_file=True):
    '''reaing text from file and checking heaps low + plot'''
    with open('book2.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    text = prepare_text(text)
    points, res_list = create_dict(text)

    if write_to_file:
        with open('result_file.csv', 'w') as f:
            wr = csv.writer(f, delimiter='\t')
            wr.writerows(r for r in points)
    #plot drowing part
    #heaps_plot(points)
    return res_list


def zipf_low_check(y):
    '''checking I zipf low + plot'''
    x = [i for i in range(0,len(y))]
    plt.scatter(x,y)
    plt.xlim([-50,35000])
    plt.ylim([-50,12000])
    plt.suptitle('zipf low check')
    plt.show()


def main():
    #d = { 'key1': 3, 'key2': 11, 'key3': 3, 'key14': 6, 'key72': 56, 'key38': 6,'key12': 7, 'key22': 44, 'key33': 9 }

    d = heaps_low_check(write_to_file=False)
    zipf_low_check(d)


if __name__ == '__main__':
    main()
