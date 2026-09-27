# Урок 1: Знакомство с Python, переменные и базовый ввод/вывод

print("Привет! Добро пожаловать на мой первый урок по Python.")

# 1. Переменные и разные типы данных
name = "Алексей"  # Строка (str)
age = 20          # Целое число (int)
height = 1.75     # Число с плавающей точкой (float)
is_learning = True  # Булево значение (True/False)

print("Меня зовут:", name)
print("Мне лет:", age)
print("Мой рост:", height)
print("Изучаю ли я Python?", is_learning)

# 2. Простая математика
a = 10
b = 5

print("\nПримеры математики:")
print("Сумма a + b =", a + b)
print("Разность a - b =", a - b)
print("Умножение a * b =", a * b)
print("Деление a / b =", a / b)

# 3. Интерактив: запросим данные у пользователя
user_name = input("\nКак тебя зовут? ")
print(", ".join(["Привет", user_name]) + "! Рад знакомству с тобой на моем репозитории.")



----------

# Lesson 1: Introduction to Python, variables, and basic input/output

print("Hello! Welcome to my first Python lesson.")

# 1. Variables and different data types
name = "Alex"           # String (str)[span_0](start_span)[span_0](end_span)
age = 20                # Integer (int)[span_1](start_span)[span_1](end_span)
height = 1.75           # Float (float)[span_2](start_span)[span_2](end_span)
is_learning = True      # Boolean value (True/False)[span_3](start_span)[span_3](end_span)

print("My name is:", name)
print("I am:", age, "years old")
print("My height is:", height)
print("Am I learning Python?", is_learning)

# 2. Simple math
a = 10
b = 5

print("\nMath examples:")
print("Sum a + b =", a + b)
print("Difference a - b =", a - b)
print("Multiplication a * b =", a * b)
print("Division a / b =", a / b)

# 3. Interactive: requesting data from the user
user_name = input("\nWhat is your name? ")
print(", ".join(["Hello", user_name]) + "! Glad to meet you in my repository.")
