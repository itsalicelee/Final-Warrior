class Object(object):
	"""docstring for Object"""
	def __init__(self, x, y):
		self._x = x
		self._y = y

	def distance_to(self, other):
		return ((self._x - other._x)**2 + (self._y - other._y)**2)**0.5

	def set_loc(self, x, y):
		self._x = x
		self._y = y
		