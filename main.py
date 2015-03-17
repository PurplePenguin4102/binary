import binary, logic, converter, combinations

Logic = logic.LogicClass()
Conv = converter.ConverterClass()
Comb = combinations.Combinations()

if __name__ == "__main__":
    bin1 = binary.Number(binary = [0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,0], btype = "uns")
    # bin2 = binary.Number(binary = [0,0,1,1])
    print Conv.get_dec(bin1)
    bin1.prettyprint() 
    hexval = Conv.get_hex(bin1)
    print hexval
    # print bin3.decvalue