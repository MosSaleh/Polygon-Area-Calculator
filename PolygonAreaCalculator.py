class Rectangle:
    def __init__(self, width, height):
        # creation of shape  with width and height as its attributed
        self.width = width
        self.height = height

    def __str__(self):
        string = (
            self.__class__.__name__
            + "(width="
            + str(self.width)
            + ", height="
            + str(self.height)
            + ")"
        )
        return string

    def set_width(self, newwidth):
        # function which sets the width of the shape

        self.width = newwidth
        return self.width

    def set_height(self, newheight):
        # function which sets the height of the shape
        self.height = newheight
        return self.height

    def get_area(self):
        # function which calculates the area of the shape
        width = self.width
        height = self.height

        area = width * height
        return area

    def get_perimeter(self):
        # function which calculates the perimiter of the shape
        width = self.width
        height = self.height

        perimiter = 2 * width + 2 * height

        return perimiter

    def get_diagonal(self):
        # function which calculates the diagonal of the shape
        width = self.width
        height = self.height
        diagonal = (width**2 + height**2) ** 0.5

        return diagonal

    def get_picture(self):
        # function which return a picture of the shape in the form of asterisk
        height = self.height
        width = self.width

        picture = ""

        if width > 50 or height > 50:
            return "Too big for picture."

        for i in range(height):
            for i in range(width):
                picture += "*"
            picture += "\n"

        return picture

    def get_amount_inside(self, othershape):
        # function which takes another shape (square or rectangle) as argument
        # and returns how many times it can fit in the first shape
        selfarea = self.get_area()
        otherarea = othershape.get_area()

        times = selfarea / otherarea

        times = str(times).split(".")
        times = times[0]
        times = int(times)

        return times


class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side
        self.side = side

    def __str__(self):
        string = self.__class__.__name__ + "(side=" + str(self.side) + ")"

        return string

    def set_side(self, side):
        self.side = side
        self.height = side
        self.width = side

        return side

    def set_width(self, width):
        # method sets both width and height
        self.width = super().set_height(width)
        self.height = super().set_width(width)
        self.side = width

    def set_height(self, height):
        # method sets both height and width
        self.width = super().set_height(height)
        self.height = super().set_width(height)
        self.side = height
