def gen_bin(M, prefix=""): # только для двоичной
    if M == 0:
        print(prefix)
    #else:
        #gen_bin(M-1, prefix+"0")
        #gen_bin(M-1, prefix+"1")
        # либо
        #return
    #gen_bin(M - 1, prefix + "0")
    #gen_bin(M-1, prefix+"1")
        # в цикле
        return
    for digit in "0", "1":
        gen_bin(M-1, prefix+digit)

def generate_numder(N:int, M:int, prefix=None): # для параметрическим количеством циф
    """Генерирует все числа (с лидирующими незначащами нулями)
    в N-ричной системе счисления (N <= 10)
    длины M
    """
    prefix = prefix or [] # создать пустой список
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numder(N, M-1, prefix)
        prefix.pop()

generate_numder(3, 3)
gen_bin(3)