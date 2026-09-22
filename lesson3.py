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
