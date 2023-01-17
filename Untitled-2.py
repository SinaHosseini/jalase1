a = int(input("zele aval ra vared konid  "))
b = int(input("zele dovom ra vared konid  "))
c = int(input("zele sevom ra vared konid  "))
x = 0

if a < b + c:
    x = 1 + x

if b < a + c:
    x = 1 + x

if c < a + b:
    x = 1 + x

if x == 3:
    print("mosalas ghabel rassm ast")

else:
    print("mosalas ghabel rasm nist")
