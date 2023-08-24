class Cylinder:
    '''円柱'''
    pi = 3.14

    def __init__(self, radius=1, height=1):
        '''赤'''
        self.radius = float(radius)
        self.height = float(height)

    def calc_base_area(self):
        '''底面積'''
        pi = Cylinder.pi
        r = self.radius
        return pi * r * r

    def calc_side_area(self):
        '''側面'''
        pi = Cylinder.pi
        r = self.radius
        h = self.height
        return 2 * pi * r *h

