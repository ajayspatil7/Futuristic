
# input > a=b;c=d; e=f; g=h;
# output > ['a=b', 'c=d', 'e=f', 'g=h']

def csToLot():
    cs = input("Enter a string of modifiers: ")
    cs = cs.replace("=", ",")
    cs = cs.split(";")
    cs = cs[:-1]
    cs = [tuple(x.split(",")) for x in cs]

    return cs


def lotToCs(lot):
    cs = ""
    for x in lot:
        cs += x[0] + "=" + x[1] + ";"
    return cs.strip(",")


print(lotToCs([('a', 'b'), ('c', 'd'), ('e', 'f')]))
print(csToLot())
# [('a', 'b'), ('c', 'd'), ('e', 'f')]
