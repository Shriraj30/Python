class Time: 
    def __init__(self, h, m):
        self.h = h
        self.m = m

    def displayTime(self):
        return f"{self.h}h {self.m}m"

    def __add__(self, otherobj):
        m = self.m + otherobj.m
        h = m // 60
        m = m % 60
        h = h + self.h + otherobj.h
        return f"{h}h {m}m"

    def __sub__(self, otherobj):
        # Subtract minutes and handle borrowing of hour if minutes go negative
        m = self.m - otherobj.m
        h = self.h - otherobj.h
        
        if m < 0:
            m += 60
            h -= 1  # Borrow 1 hour
        
        if h < 0:
            return "Invalid result: negative time"  # Handle case of negative time
        
        return f"{h}h {m}m"

    def __mul__(self, multiplier):
        # Multiply hours and minutes by the multiplier
        m = self.m * multiplier
        h = self.h * multiplier
        
        h += m // 60  # Convert extra minutes to hours
        m = m % 60    # Get the remaining minutes
        
        return f"{h}h {m}m"

# Example usage:
T1 = Time(2, 30)
T2 = Time(1, 45)

# Adding times
print("Add:", T1 + T2)  # 4h 15m

# Subtracting times
print("Sub:", T1 - T2)  # 0h 45m

# Multiplying time
print("Mul:", T1 * 3)  # 7h 30m
