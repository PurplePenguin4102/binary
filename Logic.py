import binary

class LogicClass(object):
    '''a subclass of Bin_num that defines all the different basic gates and combination 
    circuits that can be used.'''

    def __init__(self):
        pass

    def And(self, a, b):
        ''' takes two binary values with the same bit and returns the bitwise logical 'and' between them. i.e. c = 1 iff a = 1 and b = 1'''
        tempbin = []
        for i in range(len(a.binvalue)):
            if a.binvalue[i] + b.binvalue[i] == 2:
                tempbin.append(1)
            else:
                tempbin.append(0)

        bin = binary.Number(binary = tempbin)
        return bin

    def Or(self, a, b):
        ''' same as logicand but for or. c = 1 iff a = 1 or b = 1 '''
        tempbin = []
        for i in range(len(a.binvalue)):
            if a.binvalue[i] + b.binvalue[i] != 0:
                tempbin.append(1)
            else:
                tempbin.append(0)

        bin = binary.Number(binary = tempbin)
        return bin

    def Not(self, a):
        ''' flips all the bits of self and returns a binary'''
        tempbin = a.binvalue[:]
        for i in range(len(tempbin)):
            if tempbin[i] == 1: tempbin[i] = 0
            else: tempbin[i] = 1

        bin = binary.Number(binary = tempbin)
        return bin

    def Nand(self, a, b):
        tempbin = self.And(a, b)
        tempbin = self.Not(tempbin)

        return tempbin

    def Nor(self, a, b):
        tempbin = self.Or(a,b)
        tempbin = self.Not(tempbin)
        return tempbin

    def Xor(self, a, b):
        ''' implement xor using only nand gates'''

        # stage 1
        in_1 = self.Nand(a, self.Not(b))
        in_2 = self.Nand(self.Not(a), b)

        # stage 2
        out = self.Nand(in_1, in_2)

        return out