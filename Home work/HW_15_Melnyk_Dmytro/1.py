##Створити файл та записати в нього рядок##
print(70* '-' )
print('Ex. № 1')

new_file = open('text_document.txt', 'tw')
print(new_file)
new_file.write('You only live once, but if you do it right, once is enough.')
new_file.close()

##Прочитати створений файл та вивести на консоль вміст файлу.##
print(70* '-' )
print('Ex. № 2')

with open('text_document.txt', 'r') as new_file:
    content = new_file.read()

print(content)

##Додати ще один рядок до створеного файлу.##
print(70* '-' )
print('Ex. № 3')

with open('text_document.txt', 'a') as new_file:
    new_file.write('\nIf you want to live a happy life, tie it to a goal, not to people or things.')

##Прочитати всі рядки з файлу та вивести на консоль.##
print(70* '-' )
print('Ex. № 4')

with open('text_document.txt', 'r') as new_file:
    content = new_file.readlines()

for line in content:
    print(line.strip())


##Записати у файл все що користувач введе з консолі.
# (Якщо хочете більш ніж один рядок спробуйте використати while True і перевірку на введений рядок,
# типу якщо exit тоді це кінець.)##
print(70* '-' )
print('Ex. № 5')


with open('text_document.txt', 'a') as file:
    while True:
        input_user = input('Enter your string (or "exit"):')
        if input_user.lower() == 'exit':
            break
        file.write('\n' + input_user)

print(f"Entered string saved in '{new_file}'")


##Використайте прикріплений файл csv та прочитайте його за допомогою модулю csv. ##
print(70* '-' )
print('Ex. № 7')

import csv

csv_file = 'SampleCSVFile_11kb.csv'
with open(csv_file, 'r', newline='', encoding= 'utf-8') as file:
    csv_read = csv.reader(csv_file)
    for row in csv_read:
        print(row)




##Використайте прикріплений файл json та прочитайте його за допомогою модулю json ##
print(70* '-' )
print('Ex. № 8')

import json

json_file = 'sample2.json'
with open(json_file, 'r', encoding='utf-8') as file:
    json_read = json.load(file)
print(json_read)
