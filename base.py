""" 

hey cutie, here is an example of using pytest to check methods on the go.
Note: i wrote the _to_base_10 first and tested it, next i was gonna write
	 to_base_b and then, once that works, impliment the __add__.

to run the test (using py2.7 , eep):
1. cd to the working dir
2. $ python -m pytest -v base.py

"""

import pytest

class Number:

	num = [
		'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd',
		'e', 'f']

	def __init__(self, val, base=10):
		self.val = str(val).lower() # TODO: some checking for valid inputs
		self.base = base

	def _to_base_10(self):
		""" given a starting val and base, convert the val to a base 10 int """
		total = 0
		for index in range(len(self.val)):
			char = self.val[len(self.val) - 1 - index]
			x = self.num.index(char)
			total += x * pow(self.base, index)
		return total

	def __add__(self, other):
		""" now we can do easy int arithmatic!!
		TODO: what should happen for division?
		"""
		# convert self and other to int, base 10
		# do arithmatic
		# return value probably using the base of self?
		pass

def to_base_b(x, b):
	""" assumes value starts is in base 10! 

	# TODO: might be a candiate for Number static method

	Args:
		x (int): the value we wish to convert
		b (int): the expected base of the retunr value
	Returns:
		a string value representin the number x in the base b
	"""
	val = ''
	# TODO impliment this!!
	return val

# TESTS

testdata = [
    ('0', 2, 0),
    ('1', 2, 1),
    ('10', 2, 2),
    ('11', 2, 3),
    ('111', 2, 7),
    ('1e', 16, 30),
    # TODO...so many more tests!
]
@pytest.mark.parametrize('v,b,expected', testdata)
def test_to_base_10(v, b, expected):
	n = Number(v, b)
	n10 = n._to_base_10()
	assert n10 == expected

testdata = [
    (0, 2, '0'),
    (3, 2, '11'),
    (30, 16, '1e'),    
]
@pytest.mark.parametrize('x,b,expected', testdata)
def test_to_base(x, b, expected):
	val = to_base_b(x, b)
	assert val == expected