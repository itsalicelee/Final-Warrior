from game_object import Object
class Boss(Object):
	"""docstring for boss"""
	def __init__(self, x, y, hp = 100):
		super(Boss, self).__init__(x, y)
		self.hp = hp


		
	def attack():
		pass
		