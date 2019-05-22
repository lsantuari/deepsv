# -*- coding: utf-8 -*-

import requests


# FIXME: put actual code here
def do_stuff():
    print('Do something useful')


def add_numbers(a, b):
    assert type(a) != str, "Invalid input type"
    assert type(b) != str, "Invalid input type"
    return a + b


# def word_count(book_url):
#     print('BOOK_URL: ' + book_url)
#     resp = requests.get(book_url)  # Download data --
#     # external / not in our control
#     print('Type of response object: %s' % type(resp))
#     print('Type of response text object: %s' % type(resp.text))
#     text = resp.text
#     return word_count_from_text(text)


def word_count(book_url):
    text = download_text(book_url)
    wc = word_count_from_text(text)
    return wc


def download_text(book_url):
    print('BOOK_URL: ' + book_url)
    resp = requests.get(book_url)
    return resp.text


def word_count_from_text(text):
    words = text.split()
    return len(words)


def get_sequence():
    return 'TTAGGACCA'


def count_single_base(base, sequence):

    c = 0
    for i in range(0, len(sequence)):
        if sequence[i] == base:
            c += 1
    return c


def count_bases(dna_sequence):

    bases = [b for b in sorted(list(set(dna_sequence)))]
    return {b: count_single_base(b, dna_sequence) for b in bases}
