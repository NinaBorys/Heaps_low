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
    return points, res_dict

def heaps_plot(points):
    '''plot from points (tuples)'''
    plt.scatter(*zip(*points), linewidth=0.5, color='red', marker='s')
    plt.xlim([-50,250000])
    plt.ylim([-50,40000])
    plt.suptitle('heaps low check')
    plt.show()

def heaps_low_check():
    '''reaing text from file and checking heaps low + plot'''
    with open('book2.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    text = prepare_text(text)
    points, res_dict = create_dict(text)

    #with ('result_file.csv', 'w') as myfile:
    #    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #    wr.writerow(points)

    heaps_plot(points)



def main():
    heaps_low_check()



if __name__ == '__main__':
    main()
