import binary

class Combinations(object):
    ''' a class for dealing with combinational logic: Adders, decoders, multiplexers. To be used with Bin_nums'''

    def __init__(self):
        self.Logic = binary.Logic
        
    def onebit_adder(self, bin_a, bin_b, carry):
        "logical implementation of an unsigned adder"
        if not ((bin_a.bit, bin_b.bit, carry.bit) == (1, 1, 1)):
            print "Did nothing, numbers weren't 1 bit"
            return
        else:
            #stage 1
            spart = self.Logic.Xor(bin_a, bin_b)
            cout1 = self.Logic.And(bin_a, bin_b)

            #stage 2
            s = self.Logic.Xor(spart, carry)
            cout2 = self.Logic.And(spart, carry)

            #stage 3
            carry_out = self.Logic.Or(cout1, cout2)

            return (s, carry_out)

    def nbit_adder(self, bin_a, bin_b):
        if bin_a.bit != bin_b.bit:
            print "numbers must be the same bit"
            return
        else:
            carry = binary.Number(binary = [0])
            n = bin_a.bit
            ans = []
            for i in range(n)[::-1]:
                a = binary.Number(binary = [bin_a.binvalue[i]])
                b = binary.Number(binary = [bin_b.binvalue[i]])
                (s, carry) = self.onebit_adder(a, b, carry)
        
                ans.insert(0, s.binvalue[0])
            ansbin = binary.Number(binary = ans)

            return ansbin, carry

    def nbit_adder2s(self, bin_a, bin_b):
        '''detects overflow for 2s complement addition NOT CURRENTLY WORKING'''
        (s, carry) = self.nbit_adder(bin_a, bin_b)
        
        a = binary.Number(binary = [bin_a.binvalue[0]])
        b = binary.Number(binary = [bin_b.binvalue[0]])

        ab = self.Logic.Xor(a, b)
        ab = self.Logic.Not(ab) # We check that a and b's MSB are the same using XNOR

        print a.binvalue, b.binvalue
        print ab.binvalue, carry.binvalue
        overflow = self.Logic.Xor(ab,carry) # We check that the carry is different to a and b

        return (s, overflow)
