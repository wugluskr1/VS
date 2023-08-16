#1. Реализуйте рекурсивную функцию, которая выводит только нечетные числа из переданного списка на консоль.
#2. Реализуйте рекурсивную функцию для подсчета элементов в списке.
#3. Напишите функцию, которая при каждом следующем своем вызове выводит на консоль следующий элемент заданного списка.
from random import randint

j = int(input("Введите число символов в списке: "))
numbers =  [randint(1, 100) for i in range(j)]

def filter_odd_num(n):
    if (n < 2):
        return (n % 2 != 0)
    return (filter_odd_num(n - 2))
odd_numbers = filter(filter_odd_num, numbers)
print("Изначальный список: ", list(numbers))
print("Отфильтрованный список: ", list(odd_numbers))

def length(lst):
    if not lst:
        return 0
    return 1 + length(lst[1:])
print("Длина списка равна: ", length(numbers))
print(length(numbers))

def factorial_recursion(n):  
   if n == 1:  
       return n  
   else:  
       return n*factorial_recursion(n-1)
num = numbers[j-1]
print("The factorial of ",num," is ",factorial_recursion(num))

def numbers_generate(lst):
    lst = iter(lst)
    return print(next(lst, 'STOP'))
numbers_generate(numbers)

def numbers_generate(lst):
    lst = iter(lst)
    try:
        while True:
            next_val = next(lst)
            print("Значение:", next_val)
    except StopIteration:
        print("перебор завершен")
numbers_generate(numbers)
