import numpy as np
from PIL import Image


class Canvas:
	def __init__(self, width: int, height: int, color: list):
		self.image = None
		self.width = width
		self.height = height
		self.color = color
		self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
		self.data[:] = self.color

	def make(self, filepath):
		self.image = Image.fromarray(self.data)
		self.image.save(filepath)

	def show(self):
		self.image.show()
