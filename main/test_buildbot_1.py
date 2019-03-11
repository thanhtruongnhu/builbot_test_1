"""Sample Test"""

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last #'{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay*1.04)

