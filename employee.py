
class Employee:

    raise_inc = 1.10

    def __init__(self, name, last_name, pay):
        self.name = name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.name, self.last_name)

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.last_name)

    @property
    def apply_raise(self):
        return round(self.pay*self.raise_inc,1)
