
# Задачи на циклы и оператор условия------
# ----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

# for i in range(1, 6):
#     print(i, ')', 0, sep='')

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# count =0
# print('Введите 10 любых цифр:')
# for i in range(1,11):
#     number=int(input())
#     if number==5:
#         count+=1
# print('Всего пятёрок:',count)


'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# result = 1
#
# for i in range(1,11):
#      result*= i
# print(result)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# number = str(1488)
#
# for i in number:
#     print(i)


# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# integer_number = 5689
# sum=0
#
# while integer_number>0:
#     sum += integer_number%10;
#     integer_number = integer_number//10
# print(sum)

'''
Задача 7
Найти произведение цифр числа.
'''
# integer_number = 123
# result=1
#
# while integer_number>0:
#     result *= integer_number%10;
#     integer_number = integer_number//10
# print(result)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 213453
# while integer_number > 0:
#     if integer_number % 10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number // 10
# else:
#     print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# integer_number = 228
# max = 0
#
# while integer_number>0:
#     if integer_number%10>max:
#         max= integer_number%10;
#     integer_number = integer_number//10
# print(max)

'''
Задача 10
Найти количество цифр 5 в числе
'''
# integer_number = 525455
# count = 0
# while integer_number > 0:
#     if integer_number % 10 == 5:
#         count+=1
#     integer_number = integer_number // 10
# print(count)
