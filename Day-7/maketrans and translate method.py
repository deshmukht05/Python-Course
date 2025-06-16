print("MAKETRANS and TRANSLATE Method")
print("Syntax:\n1. maketrans(x[y,z])\n2. translate(table)")
print()
source = "abcd"
target = "1234"
print("Source: ", source)
print("Translate: ", target)
print()
trans_table = str.maketrans(source, target)
code = "dad acc bad".translate(trans_table)
print("Code: ", code)
