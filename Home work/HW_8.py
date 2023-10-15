##1## Написати лямбда функцію яка приймає один або 2 аргументи
# (другому задати значення за замовчуванням рівне 100, як у звичайних функціях)
# та друкує символ переданий як перший аргумент ту кількість раз яка вказана в другому аргументі,
# зробити можливим роботу фyнкції не тільки з рядком а й з цифрами.

print(70* '*')
print('Ex. 1')

var_lambda_1 = lambda x, y = 100: (
    print(str(x) * int(y)))
var_lambda_1('j')


##2##Написати лямбда функцію яка приймає 2 числа як аргументи та повертає більше з них (використовуйте тернарний if)

print(70* '*')
print('Ex. 2')

var_lambda_2 = lambda a, b: a if a > b else b
print(var_lambda_2(10, 15))

##3## Написати лямбда функція яка нічого не приймає та завжди повертає 10.

print(70* '*')
print('Ex. 3')

var_lambda_3 = lambda v: v
print(var_lambda_3(10))


##4## Використовуйте list comprehension, щоб створити новий список, але додайте 6 до кожного елемента.

print(70* '*')
print('Ex. 4')

lst1 = [44, 54, 64, 74, 104]
lst2 = [x + 6 for x in lst1]
print(lst2)


##5##Використовуючи list comprehension, побудуйте список із квадратів кожного елемента в списку.
print(70* '*')
print('Ex. 5')

lst3 = [2, 4, 6, 8, 10, 12, 14]
lst4 = [x ** 2 for x in lst3]
print(lst4)

##6## Дано словник який складається з транспортних засобів та їх маси в кілограмах.
# Складіть список назв транспортних засобів вагою до 5000 кілограмів.
# У тому самому list comprehension зробіть імена ключів великими регістром.

print(70* '*')
print('Ex. 6')

car_dict = {"Sedan": 1500,
            "SUV": 2000,
            "Pickup": 2500,
            "Minivan": 1600,
            "Van": 2400,
            "Semi": 13600,
            "Bicycle": 7,
            "Motorcycle": 110}
list5 = [a.upper() for a,  x in car_dict.items() if x < 5000]
print(list5)


##Map##Написати функцію яка повертає назву місяця за його номером.
# Використовуючи функцію map() і список який складається з чисел вивести список з навзвами місяців.

print(70* '*')
print('Ex. Map')

def month_1(number_month):
    number = {
       1: 'January',
       2: 'February',
       3: 'March',
       4: 'April',
       5: 'May',
       6: 'June',
       7: 'July',
       8: 'August',
       9: 'September',
      10: 'October',
      11: 'November',
      12: 'December'
}

    month_name = number.get(number_month)
    return month_name

month_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_name = list(map(month_1, month_number))
print(month_name)

