def happy_number(n):
    tank = set()
    while True:
        if n not in tank:
            tank.add(n)
            n = sum([int(x)*int(x) for x in list(str(n))])
            if n == 1:
                return True
            else:
                return False


print(happy_number(100))
