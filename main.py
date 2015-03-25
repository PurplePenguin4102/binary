import binary, logic, converter, combinations

Logic = logic.LogicClass()
Conv = converter.ConverterClass()
Comb = combinations.Combinations()

if __name__ == "__main__":
    bin1 = binary.Number(binary = [0,1,0,1])
    bin2 = binary.Number(binary = [0,0,1,1])
    (s,overflow) = Comb.nbit_adder2s(bin1, bin2)
    s.prettyprint()
    overflow.prettyprint()
    # bin2 = binary.Number(binary = [0,0,1,1])
    Logic.Nand(bin1,bin2).prettyprint()