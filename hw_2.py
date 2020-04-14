# Задача 1
# Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
string = 0
n_string = 0
while n_string < 5:
    n_string += 1
    print(n_string, string)

# Задача 2
# Пользователь в цикле в водит 10 цифр. Найти количество введеных пользователем цифр 5.
digit = int(input('INPUT ten digits:  '))
digit_5 = 0
while digit > 0:
    if (digit % 10) == 5:
        digit_5 += 1
        digit = digit // 10
    else: digit = digit // 10
print(digit_5)

# Задача 3
# Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
sum = 0
for x in range(1, 101):
    sum += x
print(sum)

# Задача 4
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
multiply = 1
for x in range(1, 11):
    multiply *= x
print(multiply)

print()

x = 10
multiply = 1
while x > 1:
    multiply *= x
    x = x - 1
print(multiply)

# Задача 5
# Вывести цифры числа на каждой строчке.
number_original = int(input('Input number:  '))
number = number_original
x_zero = 1
while number > 10:
    x_zero *= 10
    number = number // 10
#print(x_zero)
while number_original > 0:
    print(number_original // x_zero)
    number_original = number_original % x_zero
    x_zero = x_zero // 10

# Задача 6
# Найти сумму цифр числа.
number = int(input('Input number:  '))
sum_digit = 0
while number > 0:
    sum_digit += number % 10
    number = number // 10
print(sum_digit)

# Задача 7
# Найти произведение цифр числа.
number = int(input('Input number:  '))
multiply = 1
while number > 0:
    multiply *= (number % 10)
    number = number // 10
print(multiply)

# Задача 8
# Дать ответ на вопрос: есть ли среди цифр числа 5?
number = int(input('Input number:  '))
while number > 0:
    if number % 10 == 5:
        print('YES')
        break
    number = number // 10
else: print('NO')

# Задача 9
# Найти максимальную цифру в числе

#### I DON'T KNOW

# Задача 10
# Найти количество цифр 5 в числе
number = int(input('Input number:  '))
sum_5 = 0
while number > 0:
    if number % 10 == 5:
        sum_5 += 1
        number //= 10
    else: number //= 10
print(sum_5)

