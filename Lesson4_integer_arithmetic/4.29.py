'''
4.29. Дано двузначное число. Определить:
а) кратна ли трем сумма его цифр;
б) кратна ли сумма его цифр числу а.
'''

def multiplicity():
    print("Введите двухзначное число")
    number = int(input())
    print("Введите делитель")
    a = int(input())
    number_a = number//10
    number_b = number%10
    sum_ab = number_a+number_b
    if sum_ab%a == 0:
        print("сумма цифр {} кратна {}".format(number,a))
    else:
        print("сумма цифр {} не кратна {}".format(number,a))



multiplicity()