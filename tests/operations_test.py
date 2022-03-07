"""Testing the Calculator"""
from calculator.operations.operations import Operations


def test_calculator_add_method():
    assert Operations.add(1, 1) == 2


def test_calc_sub_method():
    assert Operations.subtract(1, 1) == 0


def test_calc_multi_method():
    assert Operations.multiply(1, 1) == 1
