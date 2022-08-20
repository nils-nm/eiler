# Проект Эллера. Задача 002
# todo вставь строки документации в функции
"""
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...
Найдите сумму всех четных элементов ряда Фибоначчи,
которые не превышают четыре миллиона.
"""

# ===== variables =====

fib_max_num = int(input("Введите максимальное положительное число: "))  # max number
# for Fibonacci sequence
div_1 = int(input("Введите число кратности: "))

# ===== functions =====


def main():
    fib(fib_max_num)
    fib_list(fib_max_num)
    answer_is()


def fib(x):
    while True:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return fib(x-1) + fib(x-2)


def fib_list(x):
    fl = []
    a = 0
    b = 1
    s = 0
    for i in range(x):
        a, b = b, a + b
        if a % div_1 == 0:
            fl = fl + [a]
            s += a
    return fl, s


def answer_is():
    print("Максимальное число Фибоначи равно " + str(fib(fib_max_num)))
    print("Сумма чисел Фибоначи в диапазоне от 0 до " + str(fib_max_num))
    print("кратных " + str(div_1))
    print("равна: " + str(my_s))
    print("Лист с числами Фибоначи равен " + str(my_fl))


# ===== main =====

my_fl, my_s = fib_list(fib_max_num)

main()
