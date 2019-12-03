#!/usr/bin/env python
'''A custom class that import a word of length 16 characters as a string and perform actions on them'''

from datetime import datetime, timedelta

# ----------#
# CONSTANTS #
# ----------#

# The default word size exported per line
WORD_SIZE = 16 # 0000000000000000

# The reference date and time in which PLC calculations start
REF_DATE = datetime(2001, 1, 1)

# ------#
# CLASS #
# ------#

class word:
    def __init__(self, value):
        """
        https://stackoverflow.com/a/4843178/1061279
        """
        if not isinstance(value, str): raise TypeError(value)
        self.value = str(value)


    def __repr__(self):
        """https://stackoverflow.com/a/1984177"""
        return self.value


    # -----------#
    # PROPERTIES #
    # -----------#

    @property
    def length(self):
        """https://stackoverflow.com/a/27571588"""
        return len(self.value)


    @property
    def type(self):
        """"""
        return type(self.value)


    @property
    def sign(self):
        """"""
        return 1 if self.value[:1] == 0 else -1


    # ----------#
    # FUNCTIONS #
    # ----------#


    def encode(self):
        """"""
        return self.value.encode()


    def flip(self):
        """"""
        return self.split()[1] + self.split()[0]


    def resize(self):
        """Resize the word to the next word size (4bit -> 16bit, 23bit -> 32bit)"""
        # Quotient
        q = self.length // WORD_SIZE
        # Remainder
        r = self.length % WORD_SIZE
        # Check if the remainder is not zero
        if r != 0:
            return self.zfill((q + 1) * WORD_SIZE)
        else:
            return self.value


    def shift_left(self, n):
        """"""
        return bin(self.to_int() << n)[2:].zfill(self.length)


    def shift_right(self, n):
        """"""
        return bin(self.to_int() >> n)[2:].zfill(self.length)


    def split(self):
        """Split the value in half. Add a leading 0 if the length is negative"""
        n = int(self.length)
        # Add 1 to n if the length is negative
        n = n + 1 if n % 2 != 0 else n
        # Fill to even number of bits
        v = self.zfill(n)
        n = int(n / 2)
        return [v[:n],v[n:]]


    def to_bin(self):
        """"""
        return bin(self.to_int())


    def to_date(self):
        """Transform to a date in format D#YYYY-MM-DD"""
        dt = REF_DATE + timedelta(seconds=self.to_int())
        return "D#{:04}-{:02}-{:02}".format(dt.year,dt.month,dt.day)


    def to_date_and_time(self):
        """Transform to a date and time in format DT#YYYY-MM-DD-HH-MM-SS"""
        dt = REF_DATE + timedelta(seconds=self.to_int())
        return "DT#{:04}-{:02}-{:02}-{:02}:{:02}:{:02}".format(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second)


    def to_int(self):
        """"""
        return int(self.value,2)


    def to_string(self):
        """"""
        return chr(self.to_int)


    def to_time(self):
        """Transform to a time in the format T#MmSs"""
        # Get the total number of seconds
        v = self.to_int() / 100
        # Minutes
        m = int(v // 60)
        # Remaining seconds
        s = int(v % 60)
        return "T#{}m{}s".format(m,s)


    def to_time_of_day(self):
        """
        Return the time of day from the total number of seconds
        https://stackoverflow.com/a/539360/
        """
        s = self.to_int()
        # hours
        h = s // 3600
        # remaining seconds
        s -=(h * 3600)
        # minutes
        m = s // 60
        # remaining seconds
        s -= (m * 60)
        # total time
        return 'TOD#{:02}:{:02}:{:02}'.format(int(h), int(m), int(s))


    def to_float32(self):
        """
        Convert to a 32bit float
        https://math.stackexchange.com/a/1506364
        sign    1 bit  31
        exp     8 bits 30-23     bias 127
        frac   23 bits 22-0

        +[3]----+[2]----+[1]----+[0]----+
        S|  exp  |   fraction           |
        +-------+-------+-------+-------+
        1|<--8-->|<---23 bits---------->|
        <-----------32 bits------------->
        """
        if self.length != 32: raise ValueError(self.length)

        n = self.to_int()

        # Check for errors
        assert 0 <= n < 2**32

        # Shift it 31 digits to get the sign
        sign = self.sign

        #1 10000010 00111100000011001001111

        # Get the exponent
        exp = (n >> 23) & 0b011111111

        # Get the fraction
        fraction = n & (2**23 - 1)

        # Check if the exponent is 0
        if exp == 0:
            if fraction == 0:
                return -0.0 if sign else 0.0
            else:
                return (-1)**sign * fraction / 2**23 * 2**(-126)  # subnormal
        elif exp == 0b111111:
            if fraction == 0:
                return float('-inf') if sign else float('inf')
            else:
                return float('nan')
        return (-1)**sign * (1 + fraction / 2**23) * 2**(exp - 127)


    def two_comps(self):
        """
        compute the 2's compliment of the int value v
        https://stackoverflow.com/a/9147327
        """
        v = self.to_int()
        b = self.length
        if (v & (1 << (b - 1))) != 0: # if sign bit is set, e.g. 8bit: 128-255
            v = v - (1 << b)          # Compute the negative value
        return v

    def zfill(self, n):
        """"""
        return self.value.zfill(n)
