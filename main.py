#1. Реализуйте рекурсивную функцию, которая выводит только нечетные числа из переданного списка на консоль.
#2. Реализуйте рекурсивную функцию для подсчета элементов в списке.
#3. Напишите функцию, которая при каждом следующем своем вызове выводит на консоль следующий элемент заданного списка.
from random import randint
numbers =  [randint(1, 100) for i in range(20)]
def filter_odd_num(in_num):
    if(in_num % 2) != 0:
        return True
    else:
        return False
odd_numbers = filter(filter_odd_num, numbers)
print("Изначальный список: ", list(numbers))
print("Отфильтрованный список: ", list(odd_numbers))