##1

#a# змінна одним словом
variables = 9

#b# однакові змінні в яких тільки одна літера відрізняється за регістром(а чи А, наприклад)
var = 10
Var = 12

#c# створити змінну з двох слів
var_greate = 45
_var_greate = 60

#d# створити змінну з числом
var_1 = 1
_var2 = 2

#e# створити змінну яка починається з символу ʼ_ʼ
_var = 8

#f# створити креативну змінну чи змінні :)
_var2_date_4  = 56

##2 Використовуючи інструкції if/else та/або if/elif/else та оператори порівняння(>, <, <=, >=. ==, !=) створити:
a = 10
b = 15

#a# cитуацію коли перша умова є істиною

if a < b:
    print('10 less than 15')

#b# інструкція переходить до else
if a > b:
    print('10 greater that 15')
else:
    print('10 > 15')

#c# перевірку чи число не нуль щоб при подальшому діленні на нього не виникло помилки.
if a != 0:
    print('a not equal 0')

#d# перевірити чи дві змінні дорівнюють одна одній
if a == b:
    print('a equal b')
else:
    print('a > b')

#e# перевірити чи дві змінні не дорівнюють одна одній
if a != b:
    print('a not equal b')

##3 Використовуючи інструкції match-case створити структуру для привітання різних користувачів в залежності від їх імені.

User = str(input("Enter you name: "))
match User:
    case 'Ivan' | 'ivan' | 'Vanya' | 'vanya':
        print('I am glad to see you here')
    case 'Dima' | 'dima' | 'Dmytro' | 'dmytro':
        print('You are not a registered user')
    case 'Olya' | 'olya' | 'olga' | 'Olga':
        print('I have not seen you for a long time')
    case 'Tima' | 'tima' | 'Timofiy' | 'timofiy':
        print('Hello Tima')
    case _:
        print("I do not know you")









