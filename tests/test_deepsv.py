#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from deepsv import deepsv
from unittest.mock import patch

"""Tests for the deepsv module.
"""


def test_something():
    assert True


def test_adding_numbers():
    assert deepsv.add_numbers(1, 1) == 2
    assert deepsv.add_numbers(1, 2) != 2


def test_with_error():
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise ValueError


# Fixture example
@pytest.fixture
def an_object():
    return {}


def test_deepsv(an_object):
    assert an_object == {}


def side_effect_function(mock):
    print('This part of the code runs when patched')
    return 'Some text that I want to test with'


def test_word_count_of_book_base():
    book = 'https://www.gutenberg.org/files/59560/59560-0.txt'
    wc = deepsv.word_count(book)
    assert wc == 30577


@patch('deepsv.deepsv.download_text', side_effect=side_effect_function)
def test_word_count_of_book(mock):
    # book = 'https://www.gutenberg.org/files/59560/59560-0.txt'
    wc = deepsv.word_count(mock.text)
    assert wc == 8


def test_count_single_base():

    sequence = 'TTAGGACCA'
    assert deepsv.count_single_base('A', sequence) == 3
    assert deepsv.count_single_base('C', sequence) == 2
    assert deepsv.count_single_base('G', sequence) == 2
    assert deepsv.count_single_base('T', sequence) == 2


def side_effect_get_sequence():
    return 'GTACGTCAG'


@patch('deepsv.deepsv.get_sequence', return_value='GTACGTCAG')
def test_count_bases(sequence):

    seq_dict = {'A': 2, 'C': 2, 'G': 3, 'T': 2}
    assert deepsv.count_bases(sequence) == seq_dict
