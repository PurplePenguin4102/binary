import math, logic, converter, combinations

Logic = logic.LogicClass()
Conv = converter.ConverterClass()
Comb = combinations.Combinations()

class Number(object):
    '''Superclass for Logic and Converter, this is where the binary data is stored, hopefully it can be manipulated from here too...'''
    def __init__(self, decvalue=None, binary=None, btype="uns", bit = 8):
        
        if decvalue is None:
            pass
        elif (decvalue > 2**bit) or ((btype == "uns") and (decvalue < 0)):
            print "can't do that boss"
            btype = "null"
            self.decvalue = 0
            return
        elif (abs(decvalue) > 2**(bit-1)) and (btype != "uns"):
            print "can't do that boss"
            btype = "null"
            self.decvalue = 0
            return
        else:
            pass

        self.HASH = {"uns":"Unsigned binary",
                     "sig":"Sign bit binary",
                     "1s":"One's complement binary",
                     "2s":"Two's complement binary",
                     "x128":"Excess 128/127 binary"}
        self.btype = btype

        if decvalue:
            self.decvalue = decvalue
            self._make_bin(bit)
        elif binary:
            self.binvalue = binary
            self.decvalue = Conv.get_dec(self)
            self.bit = len(binary)
        else:
            pass

    def _make_bin(self,bit):

        position = []
        tempvalue = abs(self.decvalue)
        for i in range(bit):
            position.insert(0, tempvalue % 2)
            tempvalue /= 2

        self.binvalue = position
        self.bit = len(self.binvalue)
        
        if (self.decvalue < 0) and (self.btype == "sig"):
            position[0] = 1
        elif (self.decvalue < 0) and (self.btype == "1s"):
            Conv.convert_1s(self)
        elif (self.decvalue < 0) and (self.btype == "2s"):
            Conv.convert_2s(self) 
        else:
            pass

    def _flipbit(self, ind):
        if self.binvalue[ind] == 0:
            self.binvalue[ind] = 1
        else:
            self.binvalue[ind] = 0

    def prettyprint(self, format = "dec"):
        ''' prints out the value of self. Accompanying the binary is the value in either "dec", "hex" or "oct"'''
        if self.btype == "null": return
        else:
            if format == "dec":
                value = self.decvalue
            elif format == "hex":
                value = Conv.get_hex(self)
            elif format == "oct":
                value = Conv.get_oct(self)
                print value
            else: return 

            print value, "in", str(len(self.binvalue)) + "-bit", self.HASH[self.btype] + ":"
            if self.bit % 4 == 0:
                print (("{}"*4+" ")*(self.bit/4)).format(*self.binvalue)
            else:
                print ("{}"*self.bit).format(*self.binvalue)

    def addbin(self,b):
        ''' a mathematical binary adder. Simply adds bits together and discards the carry. 
        Modifies the number, useful for adding a decimal value converted to unsigned binary to a number

        computes a = a + b'''
        a = self.binvalue[::-1]
        b = b.binvalue[::-1]
        carry = 0

        for i in range(len(a)):
            a[i] += b[i] + carry
            if a[i] >= 2:
                a[i] += -2
                carry = 1
            else: carry = 0

        self.binvalue = a[::-1]
        if self.btype == "uns":
            self.decvalue = Conv.get_dec(self)

if __name__ == "__main__":
    pass
