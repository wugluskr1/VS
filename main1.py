from random import randint
from functools import total_ordering
from typing import Any
from collections import Counter
import math

sentence = input("Enter a sentence: ")

word_count = {}
for word in sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

num_unique_words = len(word_count)

most_frequent_word = ""
max_count = 0
for word, count in word_count.items():
    if count > max_count:
        most_frequent_word = word
        max_count = count

print("The sentence contains", num_unique_words, "unique words.")
print("The most frequent word is:", most_frequent_word)

MyList = list(range(5,15))
print(f" Список от 1 до 15: {MyList}")
NewList = MyList[1::2]
print(f" Список от 1 до 15 c четными числами: {NewList}")
Przd = 1
for val in NewList:
    Przd *= val
print(f" Произведение: {Przd}")
Summa = sum(NewList)
print(f"Сумма : {Summa}")
NewList2 = list()
NewList2.extend(MyList)
NewList2.extend(NewList)
NewList2.append(Przd)
NewList2.append(Summa)
NewList2.sort(reverse=True)
print(f"Два объединенных списка с добалвенным произведением и суммой с ранжированием в обратном порядке : {NewList2}")
StringsList = [str(i) for i in NewList2]
print(f" Перевод в строковый тип: {StringsList}")
StringsList2 = '='.join(StringsList)
print(f' Добавление знака "=" : {StringsList2}')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 5, 9, -7, -10]
print(f" Вывод элементов меньше 5 {[elem for elem in a if elem < 5]}")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 11]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 11, 12, 13]
NewList3 = list(set(a) & set(b))
NewList3.sort()
print(f'Вывод списка с общими для двух изначальных списков элементами и отсортированных по возрастанию  : {NewList3}')
#Дана строка. Выведите слово, которое встречается чаще всего.
#Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
s = 'kafka python course stack flow dict list python stack course star product star product analytics ' \
    'flow star kafka stack flow ython list set ist fit predict dict list python ourse ython ourse star product ' \
    'ist fit predict analytics kafka stack flow product ist fit predict analytics star flow dict flow list python ' \
    'course stack flow dict list python stack course'
s = s.split()
Dict = {}
for i in s:
   Dict[i] = s.count(i)
count1 = min(Dict.values())
Consume = {}
for key, value in Dict.items():
    if value == count1:
        Consume[key] = value
print(f'Искомое слово:  {Consume.values()}')


names = ['igor', 'dasha', 'martin', 'vladimir', 'rishat', 'maria', 'marat', 'petr', 'dima', 'polina', 'katya', 'elena']
occupations = ['smm', 'developer', 'analyst', 'president', 'analyst', 'ceo', 'customer development', 'founder', 'developer', 'ml engineer', 'product manager', 'cmo']
DictNamesandOccupations = {}
for i in range(0, len(names)):
    DictNamesandOccupations[names[i]] = occupations[i]
print(f'Значения словаря:  {DictNamesandOccupations}')
print(f"Профессия Maria:  {DictNamesandOccupations.get('maria')}")
#Сложение трех словарей
dict1={1:10, 2:20, 3901:11, 384:13, 8489:1, 48:10}
dict2={3:30, 4:40, 93:12, 91:41, 95:1, 841:11, 584:11}
dict3={5:50, 6:60, 9:90, 3:13, 7:11}
Summdict = {**dict1, **dict2, **dict3}
print(f'Значения полей словаря, содержащего сумму трех словарей:  {Summdict}')
print(f'Длина словаря:  {len(Summdict)}')

#Напишите код, который для любой строки автоматически вернет словарь с количеством вхождений каждого символа.
#Потом, используя этот код, выведи для строки given_string 8 самых непопулярных букв без пробелов и запятых.
#Регистр надо учитывать!
Sentence = input("Пожайлуста введите предложение: ")
Sentence = ''.join(Sentence.split())
DictLetter = {}
for i in Sentence:
   DictLetter[i] = Sentence.count(i)
   LetterDict = dict(zip(DictLetter.values(), DictLetter.keys()))
print(f'Содержание словаря: {LetterDict}')
print(' Наименее встречающиеся буквы по возрастанию: ')
list_d = list(DictLetter.items())
list_d.sort(key=lambda i: i[1])
for k, v in list_d:
    print(k+ ':', v)


a = int(input('Enter a number: '))
b = int(input('Enter b number: '))
c = int(input('Enter c number: '))
D = int()
def discriminant(D):
    D = b ** 2 - 4 * a * c
    return D

def solve(a, b, c):
    d = discriminant(D)
    if d > 0:
        x1 = (-b - math.sqrt(d)) / 2 * a
        x2 = (-b - math.sqrt(d)) / 2 * a
        print ('Два корня: ')
        print(f'x1 =', x1)
        print(f'x2 =', x2)
    elif d == 0:
        x = -b / 2 * a
        print(f'Один  корень =', x)
    else:
        print('Корней нет')
    return
solve(a,b,c)


# Создание списка,
# его сортировка по возрастанию
# и вывод на экран
a = []
for i in range(10):
    a.append(randint(1, 50))
a.sort()
print(a)

# искомое число
value = int(input())

mid = len(a) // 2
low = 0
high = len(a) - 1

while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
else:
    print("ID =", mid)

[6, 17, 21, 27, 32, 35, 35, 36, 37, 48]
27
ID = 3
[4, 5, 12, 13, 13, 18, 22, 26, 30, 35]


a = [randint(1, 50) for i in range(10)]
a.sort()
print(a)


## сортировка
value = int(input())
left = 0
right = len(a) - 1
center = (left + right) // 2

while a[center] != value:
    if value > a[center]:
        left = center + 1
    else:
        right = center - 1
    center = (left + right) // 2
    if left >= right:
        break

if value == a[center]:
    print("ID =", center)
else:
    print("No value")



@total_ordering
class Millimeter:
    label = 'мм'
    ratio = 1  # Отношение определяемой единицы измерения к миллиметрам

    def __init__(self, value) -> None:
        if type(value) == int:
            self._value = float(value)
        elif type(value) == float:
            self._value = value
        else:
            self._value = float(value.as_millimeters() / self.ratio)

    def __repr__(self) -> str:
        return (f'{type(self).__name__}({self._value})') # 'Inch(9.2332)'

    def as_millimeters(self) -> float:
        return round(self._value * self.ratio, 5)

    def __add__(self, argument):
        return self.__class__((self.as_millimeters() + argument.as_millimeters()) / self.ratio)

    def __sub__(self, argument):
        return self.__class__((self.as_millimeters() - argument.as_millimeters()) / self.ratio)

    def __mul__(self, argument):
        return self.__class__((self.as_millimeters() * argument.as_millimeters()) / self.ratio**2)

    def __truediv__(self, argument):
        return self.__class__((self.as_millimeters() / argument.as_millimeters()))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __le__(self, other):
        return (self.as_millimeters()) <= (other.as_millimeters())

    def __lt__(self, other):
        return (self.as_millimeters()) < (other.as_millimeters())

    def __hash__(self):
       return hash(self.as_millimeters())

    def __int__(self):
        return int(self.as_millimeters())
    def __float__(self):
        return float(self.as_millimeters())

class Centimeter(Millimeter):
    label = 'см'
    ratio = 10

    def __init__(self, value) -> None:
        super().__init__(value)


class Meter(Millimeter):
    label = 'метр'
    ratio = 1000

    def __init__(self, value) -> None:
        super().__init__(value)


class Inch(Millimeter):
    label = 'дюйм'
    ratio = 25.4

    def __init__(self, value) -> None:
        super().__init__(value)

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