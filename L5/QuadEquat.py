class QuadraticEquation(object):
    def __init__(self, a, b, c):
        self.a, self.b, self.c, self.d = a, b, c, None
        self.x1 = None
        self.x2 = None
    def calc_discr(self):
        self.d = self.b**2 - 4 * self.a * self.c
    def get_discr(self):
        return self.d
    def calc_roots(self):
        if self.d is None:
            self.calc_discr()
        if self.d >= 0:
            self.x1 = (-self.b + self.d**(1/2.0))/2*self.a
            if self.d > 0:
                 self.x2 = (-self.b - self.d**(1/2.0))/2*self.a
    def get_roots(self):
        if self.x1 is not None and self.x2 is not None:
            print 'x1 = ', self.x1
            print 'x2 = ', self.x2
        elif self.x1 is not None:
            print 'x1 = ', self.x1
        else:
            print 'No roots here'
