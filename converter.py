import binary

class ConverterClass(object):
    '''a class for handling conversion of Binary numbers between excess-n, 1's comp, 2's comp, sign bit binary and unsigned binary.
    Also handles addition, converting to decimal, octal and hexadecimal.'''

    def __init__(self):
        self.Logic = binary.Logic

    def convert_1s(self, a):
        a.btype = "1s"
        if a.decvalue < 0:
            for ind in range(a.bit):
                a._flipbit(ind)

    def convert_2s(self, a):
        self.convert_1s(a)
        a.btype = "2s"
        b = binary.Number(1)
        a.addbin(b)

    def convert_xs(self, a):
        pass

    def convert_sig(self, a):
        a.btype = "sig"
        if a.decvalue < 0:
            a.flipbit(0)

    def get_dec2s(self, a):
        bit = len(a.binvalue)
        multiplier = 2**(bit-1)
        ans = -multiplier*a.binvalue[0]
        multiplier /= 2

        for i in a.binvalue[1:]:
            ans += multiplier*i
            multiplier /= 2
        return ans

    def get_dec1s(self, a):
        if a.binvalue[0] == 0:
            return self.get_dec(a)
        else:
            bit = len(a.binvalue[1:])
            multiplier = 2**(bit-1)
            ans = 0
            for i in a.binvalue[1:]:
                if i == 0: i = 1
                else: i = 0
                ans += multiplier*i
                multiplier /= 2
            return -ans

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
            ans = "0"
            for i in range(a.bit/3):
                to_convert = a.binvalue[i*3:i*3+3]
                to_convert = binary.Number(binary = to_convert)
                octval = self.get_dec(to_convert)    
                ans += str(octval)

            if ans[1] == '0':
                ans = ans[0] + ans[2:]
            return ans

        else:
            to_convert = a.binvalue[:]
            for i in range(3 - (a.bit % 3)):
                to_convert.insert(0,0)
            to_convert = binary.Number(binary = to_convert)
            return self.get_oct(to_convert)            

    def get_hex(self, a):
        if a.bit % 4 == 0:
            HEX = {10 : "A",
                   11 : "B",
                   12 : "C",
                   13 : "D",
                   14 : "E",
                   15 : "F"}

            ans = "0x"
            for i in range(a.bit/4):
                to_convert = a.binvalue[i*4:i*4+4]
                to_convert = binary.Number(binary = to_convert)
                hexval = self.get_dec(to_convert)
                if hexval < 10:
                    ans += str(hexval)
                else:
                    ans += HEX[hexval]

            if ans[1] == '0':
                ans = ans[0] + ans[2:]
            return ans

        else:
            for i in range(4 - (a.bit % 4)):
                a.binvalue.insert(0,0)
            return self.get_hex(a)
