from backend.canvas import Canvas
from backend.shapes import *
import filestack

if __name__ == "__main__":
	canvas_width = int(input("Enter canvas width: "))
	canvas_height = int(input("Enter canvas height: "))
	canvas_color = input("Enter canvas color (red, green, blue): ")
	canvas_color = canvas_color.split(", ")
	canvas = Canvas(canvas_width, canvas_height, canvas_color)

	while True:
		shape = input("What shape would you like to draw (Rectangle or Square) (enter Quit to quit): ")
		if shape.lower() == "rectangle":
			rectangle_x = int(input("Enter rectangle x coordinate: "))
			rectangle_y = int(input("Enter rectangle y coordinate: "))
			rectangle_width = int(input("Enter rectangle width: "))
			rectangle_height = int(input("Enter rectangle height: "))
			rectangle_color = input("Enter rectangle color (red, green, blue): ")
			rectangle_color = rectangle_color.split(", ")
			rectangle = Rectangle(rectangle_x, rectangle_y, rectangle_width, rectangle_height, rectangle_color)
			rectangle.draw(canvas)
		elif shape.lower() == "square":
			square_x = int(input("Enter square x coordinate: "))
			square_y = int(input("Enter square y coordinate: "))
			square_side = int(input("Enter square side length: "))
			square_color = input("Enter square color (red, green, blue): ")
			square_color = square_color.split(", ")
			square = Square(square_x, square_y, square_side, square_color)
			square.draw(canvas)
		elif shape.lower() == "quit":
			break
		else:
			print("Invalid shape")

	canvas.make("files/canvas.png")
	client = filestack.Client("AmJkWTGMSxSKoGxC3EWHdz")
	new_file = client.upload(filepath="files/canvas.png")
	print(new_file.url)
	canvas.show()
