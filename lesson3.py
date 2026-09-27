# Урок 3: Функции и работа со списками

# 1. Создание и использование простой функции
def greet(name):
    """Функция приветствия пользователя"""
    print(f"Привет, {name}! Рад видеть тебя в третьем уроке.")

# Вызываем функцию
greet("Алексей")


# 2. Функция, которая возвращает результат (return)
def multiply_numbers(a, b):
    """Возвращает произведение двух чисел"""
    return a * b

result = multiply_numbers(4, 5)
print(f"Результат умножения функции: {result}")


# 3. Работа со списками
print("\n--- Работа со списками ---")
my_lessons = ["lesson1.py", "lesson2.py", "lesson3.py"]

print("Мои уроки в репозитории:")
for lesson in my_lessons:
    print(f" - {lesson}")

# Добавляем новый элемент в список
my_lessons.append("lesson4.py")
print(f"Всего уроков теперь: {len(my_lessons)}")



----------


# Lesson 3: Functions and working with lists

# 1. Creating and using a simple function
def greet(name):
    """User greeting function"""
    print(f"Hello, {name}! Glad to see you in the third lesson.")

# Calling the function
greet("Alex")

# 2. Function that returns a result (return)
def multiply_numbers(a, b):
    """Returns the product of two numbers"""
    return a * b

result = multiply_numbers(4, 5)
print(f"Function multiplication result: {result}")

# 3. Working with lists
print("\n--- Working with lists ---")
my_lessons = ["lesson1.py", "lesson2.py", "lesson3.py"]

print("My lessons in the repository:")
for lesson in my_lessons:
    print(f" - {lesson}")

# Adding a new element to the list
my_lessons.append("lesson4.py")
print(f"Total lessons now: {len(my_lessons)}")
