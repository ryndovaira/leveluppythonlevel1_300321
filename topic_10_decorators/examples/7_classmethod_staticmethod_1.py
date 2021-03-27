class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        # date = Date(day, month, year)       # __init__ = Data(day, month, year)
        date = cls(day, month, year)       # __init__ = Data(day, month, year)

        return date

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date_obj = Date.from_string('11-09-2012')
date_tmp = date_obj.from_string('20-12-2042')

is_date = Date.is_date_valid('11-09-2012')
is_date2 = date_obj.is_date_valid('20-12-2042')

date_default = Date()   # __init__ with defaults

date_obj_2 = Date(44, 12, 2000)     # __init__

print(f'Is 55-09-2012 correct? {Date.is_date_valid("55-09-2012")}')
