#1. Реализуйте рекурсивную функцию, которая выводит только нечетные числа из переданного списка на консоль.
#2. Реализуйте рекурсивную функцию для подсчета элементов в списке.
#3. Напишите функцию, которая при каждом следующем своем вызове выводит на консоль следующий элемент заданного списка.
from random import randint

j = int(input("Введите число символов в массиве: "))
numbers =  [randint(1, 100) for i in range(j)]
def filter_odd_num(i):
    if(i % 2) != 0:
        return True
    else:
        return False
odd_numbers = filter(filter_odd_num, numbers)
print("Изначальный список: ", list(numbers))
print("Отфильтрованный список: ", list(odd_numbers))

def factorial_recursion(n):  
   if n == 1:  
       return n  
   else:  
       return n*factorial_recursion(n-1)
# Вызов функции
num = numbers[j-1]
print("The factorial of ",num," is ",factorial_recursion(num))