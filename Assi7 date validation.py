class Date:
    month_31_days = (1, 3, 5, 7, 8, 10, 12)
    month_30_days = (4, 6, 9, 11)

    def __init__(self, d, m, y):
        if self.is_valid_date(d, m, y):  
            self.d = d
            self.m = m
            self.y = y
        else:
            self.d = None  
            self.m = None
            self.y = None

    def is_valid_date(self, d, m, y):
        if m < 1 or m > 12:  
            return False
        if d < 1: 
            return False
    
        if m in self.month_31_days:
            return d <= 31
        elif m in self.month_30_days:
            return d <= 30
        elif m == 2: 
            if self.is_leap_year(y):
                return d <= 29
            else:
                return d <= 28
        return False

    def is_leap_year(self, y):
        return y % 4 == 0

    def is_valid(self):
        return self.d is not None and self.m is not None and self.y is not None

    def return_date(self):
        if self.is_valid():
            return f"{self.d}-{self.m}-{self.y}"
        return "Invalid date"

    def next_day(self):
        self.d += 1
        if self.m in self.month_31_days:
            if self.d > 31:
                self.d = 1
                self.m += 1
                if self.m > 12:  
                    self.m = 1
                    self.y += 1
        elif self.m in self.month_30_days:
            if self.d > 30:
                self.d = 1
                self.m += 1
        elif self.m == 2:
            if self.is_leap_year(self.y):
                if self.d > 29:
                    self.d = 1
                    self.m += 1
            else:
                if self.d > 28:
                    self.d = 1
                    self.m += 1

        return self

def get_user_input():
    d = int(input("Enter day: "))
    m = int(input("Enter month: "))
    y = int(input("Enter year: "))
    return Date(d, m, y)

date = get_user_input()
if date.is_valid():
    tomorrow = date.next_day()
    print("Tomorrow's date is:", tomorrow.return_date())
else:
    print("Invalid date entered.")
