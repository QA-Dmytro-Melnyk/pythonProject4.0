##1. РЯДКИ##

#a# Навести приклад простого рядка

f = 'Hello world '
print(f)

#b# Навести приклад багаторядкового рядка (Вірш, хоку - щоб показати форматування)

_hoky = """
Нічної хвилі хлюпіт об весло. 
Нутро холоне,
Сльози набігають.
"""
print(_hoky)

#c# Навести приклад рядка з ігноруванням екрануючих символів (Raw)

_directory= r'C:\ProgramData\NVIDIA Corporation\Drs'
print(_directory)

_directory_1 = 'C:\\ProgramData\\NVIDIA Corporation\\Drs'
print(_directory_1)

_string = "Сім'я"
_string_1 = 'Сім\'я'
print(_string, _string_1, sep=', ')

#d# Навести приклад форматування довгих рядків

_text = 'and' + ' I am' + ' glad' + ' to see you'
first_last_name = 'Dmytro Melnyk'

text = 'My name is {}' .format(first_last_name)
print(text)

text_1 = 'My name is {} {}' .format(first_last_name, _text)
print(text_1)

text_2 = 'My name is {1} {0}' .format(first_last_name, _text)
print(text_2)

text_3 = f"My name is {first_last_name} {_text}"
print(text_3)






##2. Списки##

#a# створити список
print("Ex.2 p.a")
list_1 = [1, 2, 3, 4, 5]
print(list_1)

#b# копіювати через .copy()
print("Ex.2 p.b")
copy_list_1 = list_1.copy()
print(copy_list_1)

#c# додати елемент до списку
print("Ex.2 p.c")
list_3 = [9, 5, 6]
list_3.append('A, B, C')
print(list_3)

#d# вставити елемент в певне місце
print("Ex.2 p.d")
list_4 = ['n', 'd', 'g']
list_4.insert(2,'D')
print(list_4)

#e# додати один список до іншого 2 способами *
#створив другий список
print("Ex.2 p.e")
list_2 = ['N', 'V', 'S']
print(list_2)

 #
for x in list_2:
    list_1.append (x)
print(list_1)

#
list_3 = [list_1, list_2]
print(list_3)

#
list_1.extend(list_2)
print(list_1)


#f# команда .pop()
print("Ex.2 p.f")
list_5 = [1, 2, 3, 3]
list_5.pop(2)
print(list_5)

#g# видалити елемент за значенням і за індексом
print("Ex.2 p.g")
list_2.remove('V')
print(list_2)

del list_1 [2]
print(list_1)

#h# показати як дістати значення елемента за його індексом.
print("Ex.2 p.h")
print(list_1 [2])

#i# Створити змінну з посиланням на перший список
print("Ex.2 p.i")
list_8 = ['d', 'g', 'l', 'r', 'y']
deep_copy_list_11 = list_8.copy()
print(deep_copy_list_11)

#j# Створити поверхову (Shallow copy) копію першого списка
print("Ex.2 p.j")
list_26  = ['n', 'f', 'd', 'a']
_shallow_copy_list_26= list_26
print(_shallow_copy_list_26)
print(id(_shallow_copy_list_26))
print(list_26)
print(id(list_26))

#k# Створити глибоку (повну) (Deep copy) першого списка
print("Ex.2 p.k")
list_27 = [6, 3, 5, 4, 7]
deep_coppy_list_27 = list_27.copy()
print(id(deep_coppy_list_27))
print(deep_coppy_list_27)
print(id(list_27))
print(list_27)

#l# Вивести значення всіх списків
print("Ex.2 p.l")
print(list_26, list_27)

#m# Змінити перший список і ще раз вивести значення всіх списків
print("Ex.2 p.m")
list_13 = [6, 5, 4, 6]
list_14 = ['D', 'w', 'x', 'Z', 'v', 'G']
list_13.insert(3,'A')
print(list_13, list_14)





##3. Вкладені структури##


#a# Створити 3 вимірний список (список 3х списків)
print("Ex.3 p.a")
_list_10 = [1, 2, 3.4]
_list_11 = ['a', 'b', 'c']
_list_12 = ['T', 'H', 'X']

_list_14 = [_list_10, _list_11, _list_12]
print(_list_14)

#b# Змінити, будь який, елемент, будь якого, спиcку
print("Ex.3 p.b")
_list_17 = ['F', 'S', 'A']
_list_17 [0] = 9
print(_list_17)

#c# Вивести значення до та після
print("Ex.3 p.c")
_list_17 = ['F', 'S', 'A']
print(_list_17)
_list_17 [0] = 9
print(_list_17)

#d# Створити словник зі вкладеним списком
print("Ex.3 p.d")
dict_1 = {
    1: _list_17
}
print(dict_1)



#e# Зберегти вкладений список зі словника у нову змінну
print("Ex.3 p.e")

dict_2 ={
    1: _list_17
}
new_list = dict_2[1]
print(new_list)




##4. Показати форматування рядків за допомогою '{}'.format() та f'{}'
print('Ex.4 using format')

age = 34
name = 'Dmytro Melnyk'
city = 'Kyiv'
text = 'My name {} I am {} I live in {}'
print(text.format(name, age, city))

print('Ex.4 using f')
age = 34
name = 'Dmytro Melnyk'
city = 'Kyiv'
print(f'My name is {name} I am {age} I live in {city}')


##5. Показати роботу методів типу даних Рядок (на приклад .split(), .upper(), .lower(), .capitalize(), .find()*)
print('Ex.5')

string_11 = 'heLLo mY name is Dyma'
print(string_11)
print(string_11.upper())
print(string_11.capitalize())
print(string_11.lower())
print(string_11.find('o'))
print(string_11.split())


##6. slices##
print('Ex.6')
string_5 = 'ABCDFEG'

list_5 = ['A', 'D', 'E', 'R', 'F', 'Q', 'V', 'G']

#a# За допомогою даної конструкції перевернути рядок
print('Ex.6 p.a')
print(string_5 [::-1])

#b# За допомогою даної конструкції перевернути список
print('Ex.6 p.b')
print(list_5.reverse())
print(list_5)

#c# повернути частину списку від 2 до 7 елементу з кроком 2
print('Ex.6 p.c')
list_6 =['A', 'D', 'E', 'R', 'F', 'Q', 'V', 'G', 'T', 'U']
print(list_6 [2:7:2])



#d# повeрнути частину рядка (вважати рядок списком)
print(30 * '_')
print('Ex.6 p.d')

_string_1 = 'sdjkhdsjf'
list_20 = list(_string_1)
print(list_20)
print(list_20[1:4])

##7##За допомогою циклу for вивести всі елементи списку в консоль
print(30*'_')
print('Ex.7')

_list_20 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for item in _list_20:
    print(item)

##8##Зробити пункт 7 за допомогою циклу while
print(30*'_')
print('Ex.8')

a = 1
while a < 10:
    print(a)
    a += 2




