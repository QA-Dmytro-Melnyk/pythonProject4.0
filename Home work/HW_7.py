##1##
print(70*'*')
print('Ex.1')
def count_it(sequence):
    digit_count = {}

    top_3 = []

    for digit in sequence:
        if digit.isdigit():
            digit = int(digit)
            if digit in digit_count:
                digit_count[digit] += 1
            else:
                digit_count[digit] = 1

    sorted_digits = sorted(digit_count.items(), key=lambda x: x[1], reverse=True)

    for digit, count in sorted_digits[:3]:
        top_3.append((digit, count))

    result = dict(top_3)

    return result


sequence = "5765765757544323337977"
result = count_it(sequence)
print(result)



##2##
print(70*'*')
print('Ex.2')

from collections import namedtuple

Fish = namedtuple('Fish', ['name', 'species', 'tank'])
fish1 = Fish(name='Shark', species='Predator', tank='Ocean')
fish2 = Fish(name='Pike', species='Predator', tank='River')
fish3 = Fish(name='Nemo', species='Striped', tank='Ocean')

selected_fish = fish2
selected_fish_dict = selected_fish._asdict()

print(selected_fish_dict)

##3##
print(70*'*')
print('Ex.3')

from collections import defaultdict, namedtuple

Fish = namedtuple('Fish', ['name', 'species', 'tank'])

default_fish = Fish(name='Shark', species='Predator', tank='Ocean')

fish_dict = defaultdict(lambda: default_fish)

fish_dict['fish1'] = Fish(name='Shark', species='Predator', tank='Ocean')
fish_dict['fish2'] = Fish(name='Nemo', species='Striped', tank='Ocean')
print(fish_dict['fish3'])

##4##
print(70*'*')
print('Ex.4')

from collections import  deque
new_deque= deque()
new_deque.appendleft('x')
new_deque.append('y')
new_deque.append('a')
print(new_deque)

element = new_deque.popleft()
print(new_deque)

element = new_deque.pop()
print(new_deque)

##5##
print(70*'*')
print('Ex.5')
def new_decor (func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Result:", result)
        return result

    return wrapper
@new_decor
def add(a, b):
    return a * b

result = add(100, 25)
