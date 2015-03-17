import binary

class ConverterClass(LogicClass):
    '''a class for handling conversion of Binary numbers between excess-n, 1's comp, 2's comp, sign bit binary and unsigned binary.
    Also handles addition, converting to decimal, octal and hexadecimal.'''

    def __init__(self):
        self.Logic = LogicClass()

    def convert_1s(self, a):
        a.binvalue = self.logicnot()


    def convert_2s(self, a):
        self.convert_1s()
        b1 = binary.Number(1)
        self.add_bin(_b1)

    def convert_xs(self, a):
        pass

    def convert_sig(self, a):
        pass

    def get_dec(self, a):
        bit = len(a.binvalue)
        multiplier = 2**(bit-1)
        ans = 0
        for i in a.binvalue:
            ans += multiplier*i
            multiplier /= 2
        return ans

    def get_oct(self, a):
        if a.bit % 3 == 0:
            pass
        else:
            for i in range(a.bit % 3):
                a.binvalue.insert(0,0)
            get_oct(self.a)

    def get_hex(self, a):
        if a.bit % 4 == 0:
            pass
        else:
            for i in range(a.bit % 4):
                a.binvalue.insert(0,0)
            get_oct(self.a)
