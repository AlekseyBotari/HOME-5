#  Задание 1:
print('Задание 1')

# print('Введите слово')
# text_input_part_1 = str(input())

text_input_part_1 = 'MALAYALAM'

if text_input_part_1.lower() == text_input_part_1[::-1].lower():
    print('+')
else:
    print('-')

#  Задание 2:
print('Задание 2')

# print('Введите текст')
# text_input = str(input())

# print('Введите слово, которое нужно найти')
# world_find = str(input())

text_input = 'World of tanks'
world_find = 'tanks'

if text_input.find(world_find) != -1:
    print('YES')
else:
    print('NO')

# Задание 3:
print('Задание 3')

text_input_part_3 = 'www://metanit.com/python/tutorial/2.2.php'

if text_input_part_3.startswith('www'):
    print(text_input_part_3 + 'zzz')
else:
    print('www' + text_input_part_3[3:])

#  Задание 4:
print('Задание 4')

# print('Введите строку с буквами и цифрами')
# text_input_part_4 =  = str(input())

text_input_part_4 = 'fsdkfsjdljkfjs454534kdasdas548395849'

i = 0
while i <= 9:
    j = str(i)
    text_input_part_4 = text_input_part_4.replace(j, '')
    i += 1
print(text_input_part_4)

# Задание 5:
print('Задание 5')

# print('Введите электронную почту')
# text_input_part_5 =  = str(input())

text_input_part_5 = 'hydrokinetics745@gmail.com'

if text_input_part_5.find('@') != -1 and text_input_part_5.endswith('.com'):
    print('YES')
else:
    print('N0')


