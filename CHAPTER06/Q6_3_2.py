class rectangle:
    '''長方形'''
    angle = 90

    def __init__(self, width, height):
        self .name = 'rectangle'
        self .width = width
        self .height = height
        self .perimeter = self.calc_perimeter()
        self .area = self .calc_area() 
