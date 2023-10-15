##Dictionary##

#a. Створити пустий словник одним з наведених в лекції способів#
print(30*'_')
print('Ex.1 p. a')

new_dict = {}
print(type(new_dict))

#b. Створити новий словник з 2-3 парами ключ:значення#
print(30*'_')
print('Ex.1 p. b')

new_dict_1 = {
    'age': 34,
    'first name':'Dyma',
    'last name':'Melnyk'
}
print(new_dict_1)

#c. Додати одну пару ключ:значення до першого словника#
print(30*'_')
print('Ex.1 p. c')

new_dict['city'] = 'Kyiv'
print(new_dict)

# d. Додати до першого словника другий словник використовуючи .update()#
print(30*'_')
print('Ex.1 p. d')

new_dict.update({
    'age': 34,
    'first name':'Dyma',
    'last name':'Melnyk'
})
print(new_dict)

#e. видалити один елемент словника за допомогою .pop()#
print(30*'_')
print('Ex.1 p. e')

new_dict.pop('last name')
print(new_dict)

#f.  Видалити один елемент за допомогою .popitem()#
print(30*'_')
print('Ex.1 p. f')

new_dict.popitem()
print(new_dict)

#g. Зробити глибоку копію першого словника в нову змінну#
print(30*'_')
print('Ex.1 p. g')

deep_copy_new_dict = new_dict.copy()
print(new_dict)
print(id(new_dict))
print(deep_copy_new_dict)
print(id(deep_copy_new_dict))

#h. Додати до нового словника новий ключ, а як значення передати перший словник#
print(30*'_')
print('Ex.1 p. h')

deep_copy_new_dict['country'] = new_dict
print(deep_copy_new_dict)

#i. Вивести список ключів#
print(30*'_')
print('Ex.1 p. i')

print(deep_copy_new_dict.keys())

#j. Вивести список значень#
print(30*'_')
print('Ex.1 p. j')

print(deep_copy_new_dict.values())


##2. Set##

#a. Створити set котрий приймає в себе наступний ряд: 1, 2, 3, 4, 5, 6, 7#
print(30*'_')
print('Ex.2 p. a')

new_set = {1, 2, 3, 4, 5, 6, 7}
print(f'new_set is {new_set}')

#b. Створити set котрий приймає в себе наступний ряд: 5, 6, 7, 8, 9, 10, 11#
print(30*'_')
print('Ex.2 p. b')

new_set_1 = {5, 6, 7, 8, 9, 10, 11}
print(f'new_set_1 is {new_set_1}')

#c. Розширити перший сет за допомогою коменди .add(0)#
print(30*'_')
print('Ex.2 p. c')

print(new_set)
new_set.add(0)
print(new_set)

#d. Виконати команду .intersection() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.#
print(30*'_')
print('Ex.2 p. d')

new_set_2 = new_set.intersection(new_set_1)
print(f'new_set_2 is {new_set_2}')

#e. Виконати команду .difference() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.#
print(30*'_')
print('Ex.2 p. e')

new_set_3 = new_set.difference(new_set_1)
print(f'new_set_3 is {new_set_3}')

#f.Виконати команду .symmetric_difference() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.#
print(30*'_')
print('Ex.2 p. f')

new_set_4 = new_set.symmetric_difference(new_set_1)
print(f'new_set_4 is {new_set_4}')

#g. Вивести всі змінні у консоль.#
print(30*'_')
print('Ex.2 p. g')

print(new_set)
print(new_set_1)
print(new_set_2)
print(new_set_3)
print(new_set_4)

##3. Tuple##

#a. Створити кортеж котрий приймає в себе наступний ряд: 1, 2, 3, 4, 5, 6, 7#
print(30*'_')
print('Ex.3 p. a')

new_tuple = (1, 2, 3, 4, 5, 6, 7)
print(new_tuple)
print(type(new_tuple))

#b. Вивести кортеж у консоль#
print(30*'_')
print('Ex.3 p. b')

a, b, c, d, f, e, g = new_tuple
print(a, b, c, d, f, e, g)

#c. Створити кортеж кортежів#
print(30*'_')
print('Ex.3 p. c')

tuple_of_tuples = (('a', 'b', 'c',), ('d', 'e', 'f'), ('g', 'k', 'l'))
print(tuple_of_tuples)

#d. Розширити кортеж через приведення типів#
print(30*'_')
print('Ex.3 p. d')

tuple_of_tuples = list(tuple_of_tuples)
print(type(tuple_of_tuples))
tuple_of_tuples.append(('m', 'x', 's'))
print(tuple_of_tuples)
tuple_of_tuples = tuple(tuple_of_tuples)
print(type(tuple_of_tuples))