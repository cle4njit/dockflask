""" This is the Calculator Class"""
from calculator.operations.operations import Operations


class Calculator:

    """ This is the default result property"""
    result = 0

    @staticmethod
    def add(value_1, value_2):
        """ This is the add method"""

        return Operations.add(value_1, value_2)

    @staticmethod
    def subtract(value_1, value_2):
        """ This is the subtract method"""
        return Operations.subtract(value_1, value_2)

    @staticmethod
    def multiply(value_1, value_2):
        return Operations.multiply(value_1, value_2)

    def get_result(self):
        """ This is the get result method"""
        return self.result
