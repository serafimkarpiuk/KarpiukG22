a = int(input("a"))
b = int(input("b"))
z = a
while a < b:
    print(a, "<", b)
    a = a + z ;
if a > b:
    print("цикл окончен", a, ">", b)