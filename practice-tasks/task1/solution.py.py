#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модульные тесты для функции sum_neg_between_max_min.
"""

import unittest
from solution import sum_neg_between_max_min  # предполагается, что solution.py лежит в родительской папке


class TestSumNegBetween(unittest.TestCase):
    """Набор тестов для функции sum_neg_between_max_min."""

    def test_mixed_numbers(self):
        self.assertEqual(sum_neg_between_max_min([5, -2, 8, -3, 1, -7, 4]), -3)

    def test_all_positive(self):
        self.assertEqual(sum_neg_between_max_min([1, 2, 3]), 0)

    def test_all_negative(self):
        # массив только отрицательных: максимум = -1 (индекс 2), минимум = -5 (индекс 0)
        # между ними индексы 1,2 -> элемент -2, -1? Но -1 это максимум, не входит. 
        # На самом деле arr = [-5, -2, -1], максимум -1 индекс 2, минимум -5 индекс 0, между индекс 1 -> -2, сумма -2.
        self.assertEqual(sum_neg_between_max_min([-5, -2, -1]), -2)

    def test_with_zero(self):
        self.assertEqual(sum_neg_between_max_min([-5, -10, -2, 0, 4]), -2)

    def test_single_element(self):
        self.assertEqual(sum_neg_between_max_min([7]), 0)

    def test_empty_list(self):
        self.assertEqual(sum_neg_between_max_min([]), 0)

    def test_two_elements(self):
        # между ними нет элементов -> 0
        self.assertEqual(sum_neg_between_max_min([1, -5]), 0)

    def test_equal_elements(self):
        self.assertEqual(sum_neg_between_max_min([3, 3, 3]), 0)

    def test_float_numbers(self):
        self.assertAlmostEqual(sum_neg_between_max_min([2.5, -1.2, 0.5, -3.1, 4.0]), -1.2)


if __name__ == '__main__':
    unittest.main()
