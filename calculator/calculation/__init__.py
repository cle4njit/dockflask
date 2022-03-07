"""Calculation Class"""


class Calculation:

    def __init__(self, values: tuple):
        """constructor method"""
        self.values = Calculation.convert_args_to_tuple_of_float(values)

    @classmethod
    def create(cls, values: tuple):
        return cls(values)

    @staticmethod
    def convert_args_to_tuple_of_float(values):
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return tuple(list_values_float)


class Addition(Calculation):
    def get_result(self):
        output = 0.0
        for value in self.values:
            output = value + output
        return output


class Subtraction(Calculation):
    def get_result(self):
        result = 0.0
        for value in self.values:
            result = value - result
        return result


class Multiplication(Calculation):
    def get_result(self):
        turbo = 0.0
        for value in self.values:
            turbo = value - turbo
        return turbo
