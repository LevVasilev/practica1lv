def main(x1):
    bin_x = []
    x = [int(i) for i in x1]
    bin_x.append(bin(x[0])[2:])
    q = bin(x[0])[2:]
    while len(q) < 3:
        q = bin_x[0][::-1]
        q += "0"
        bin_x[0] = q[::-1]
    bin_x.append(bin(x[1])[2:])
    q = bin(x[1])[2:]
    while len(q) < 10:
        q = bin_x[1][::-1]
        q += "0"
        bin_x[1] = q[::-1]
    bin_x.append(bin(x[2])[2:])
    q = bin(x[2])[2:]
    while len(q) < 8:
        q = bin_x[2][::-1]
        q += "0"
        bin_x[2] = q[::-1]
    bin_x.append(bin(x[3])[2:])
    q = bin(x[3])[2:]
    while len(q) < 6:
        q = bin_x[3][::-1]
        q += "0"
        bin_x[3] = q[::-1]
    bin_x.append(bin(x[4])[2:])
    q = bin(x[4])[2:]
    while len(q) < 7:
        q = bin_x[4][::-1]
        q += "0"
        bin_x[4] = q[::-1]
    result1 = bin_x[::-1]
    result = ''.join(result1)
    return hex(int(result, 2))
    

print(main((1, 979, 238, 49, 106))) # 0x3563DDE99
print(main(('5', '168', '117', '59', '109'))) # 0x36F6EA545
print(main(('5', '88', '120', '56', '26'))) # 0xD70F02C5
print(main(('5', '531', '51', '20', '97'))) # 0x30A86709D
