##Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до
# величини end включно. Якщо користувач задасть перше число більше, ніж друге,
# просто поміняйте їх місцями. (35 балів)##

def sum_range(start, end):
    if start > end:
        start, end = end, start

    arg = 0
    for number in range(start, end + 1):
        arg += number
    return arg


total_suma = sum_range(6, 3)
print(f'Total sum all numbers: {total_suma}')


##Написати функцію season, що приймає 1 аргумент - номер місяця (від 1 до 12),
# і повертає пору року, якому цей місяць належить (зима, весна, літо чи осінь).##

def season(number_month):
    if 1 < number_month < 12:
        if number_month in (12, 1, 2):
            return 'Winter'
        elif number_month in (3, 4, 5):
            return 'Spring'
        elif number_month in (6, 7, 8):
            return 'Summer'
        elif number_month in (9, 10, 11):
            return 'Autumn'
entered_month = 7
results = season(entered_month)
print(f'You entered month which is in {results}')

##Написати функцію get_filtered(), що приймає 1 аргумент - список
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
# і виводить на консоль всі елементи які менші 5. (for/while + if)##



def get_filtered(a):
    for item in a:
        if item < 5:
            print(item)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
get_filtered(a)


##Написати функцію num1 яка приймає один аргумент x
# і повертає функцію вкладену функцію, а також має вкладену функцію num2
# яка приймає один аргумент y і повертає результат множення. (виклик буде num1(3)(4))##

def num1(x):
    def num2(y):
        return x * y
    return num2
num1_3 = num1(3)
result = num1_3(4)
print(result)