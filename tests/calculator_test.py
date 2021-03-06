"""Testing the Calculator"""
from calculator import Calculator


def test_calculator_is_instance():
    """Testing the Calculator"""
    calculator = Calculator()
    assert isinstance(calculator, Calculator)


def test_calculator_get_result_method():
    """Testing the Calculator"""
    calculator = Calculator()
    assert calculator.get_result() == 0


def test_calculator_result_property():
    """Testing the Calculator"""
    calc1 = Calculator()
    calc2 = Calculator()
    calc1.result = 5
    calc2.result = 6
    assert calc1.result == 5
    assert calc2.result == 6


def test_calculator_add_method():
    """Testing the Calculator"""
    assert Calculator.add(1, 1) == 2


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    assert Calculator.subtract(1, 1) == 0


def test_calculator_multiply_method():
    """Testing the Calculator Multiply"""
    assert Calculator.multiply(1, 1) == 1
