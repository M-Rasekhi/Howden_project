class Rect():
    
    def __init__(self,width, height):
        self.width = width
        self.height = height

    def area(self):
        area = round(self.width * self.height, 2)
        return area

    def p_moment(self):
        x=self.width
        y=self.height
        principal_moment = round(x*y**3/12, 2)

        return principal_moment

        
    
