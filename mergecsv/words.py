'''

'''

# ----------#
# CONSTANTS #
# ----------#

WORD_SIZE = 16

class word:
    def __init__(self, value):
        # https://stackoverflow.com/a/4843178/1061279
        if not isinstance(value, str): raise TypeError(value)
        self.value = str(value)


    def __repr__(self):
        '''https://stackoverflow.com/a/1984177'''
        return(self.value)


    # -----------#
    # PROPERTIES #
    # -----------#

    @property
    def length(self):
        '''https://stackoverflow.com/a/27571588'''
        return(len(self.value))


    @property
    def type(self):
        ''''''
        return(type(self.value))


    @property
    def sign(self):
        ''''''
        return 1 if self.value[:1] == 0 else -1


    # ----------#
    # FUNCTIONS #
    # ----------#

    def encode(self):
        ''''''
        return self.value.encode()

    def to_bin(self):
        ''''''
        return(bin(self.to_int()))


    def to_int(self):
        ''''''
        return(int(self.value,2))

    def to_string(self):
        ''''''
        return(chr(self.to_int))

    def resize(self):
        ''''''
        # Quotient
        q = self.length // WORD_SIZE

        # Remainder
        r = self.length  % WORD_SIZE

        if r != 0:
            return self.zfill((q + 1) * WORD_SIZE)
        else:
            return self.value

    def shift_left(self, n):
        ''''''
        return(bin(self.to_int() << n)[2:].zfill(self.length))


    def shift_right(self, n):
        ''''''
        return(bin(self.to_int() >> n)[2:].zfill(self.length))

    """
       sign    1 bit  31
       exp     8 bits 30-23     bias 127
       frac   23 bits 22-0

    +[3]----+[2]----+[1]----+[0]----+
    S|  exp  |   fraction           |
    +-------+-------+-------+-------+
    1|<--8-->|<---23 bits---------->|
    <-----------32 bits------------->
    """
    def to_float32(self):
        '''https://math.stackexchange.com/a/1506364'''
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
        elif exp == 0b1111111:
            if fraction == 0:
                return float('-inf') if sign else float('inf')
            else:
                return float('nan')
        return (-1)**sign * (1 + fraction / 2**23) * 2**(exp - 127)


    def zfill(self, n):
        ''''''
        return self.value.zfill(n)
