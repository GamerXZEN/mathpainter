class Square:
	def __init__(self, x: int, y: int, side_length: int, color: list):
		self.x = x
		self.y = y
		self.side = side_length
		self.color = color

	def draw(self, canvas):
		canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle(Square):
	def __init__(self, x: int, y: int, width: int, height: int, color: list):
		super().__init__(x, y, width, color)
		self.height = height

	def draw(self, canvas):
		canvas.data[self.x: self.x + self.height, self.y: self.y + self.side] = self.color
