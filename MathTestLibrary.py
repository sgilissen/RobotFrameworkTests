import MathFunctions


class MathTestLibrary(object):
    """
    Test library for math functions to get a feel of the Robot framework
    """

    def __init__(self):
        self._math = MathFunctions
        self._result = ''

    def calculate_product(self, value1, value2):
        self._result = self._math.get_product(value1, value2)

    def calculate_sum(self, *args):
        self._result = self._math.get_sum(*args)

    def calculate_square_root(self, value):
        self._result = self._math.get_sqrt(value)

    def result_should_be(self, expected):
        if self._result != expected:
            raise AssertionError('%s != %s' % (self._result, expected))
