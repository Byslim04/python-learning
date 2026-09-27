# Урок 2: Условия (if/elif/else) и циклы (for, while)

print("--- 1. Условные операторы (if, elif, else) ---")
age = int(input("Сколько вам лет? "))

if age < 18:
    print("Вы еще несовершеннолетний(-яя).")
elif age == 18:
    print("Поздравляем с совершеннолетием!")
else:
    print("Вы взрослый человек.")


print("\n--- 2. Цикл со счетчиком (for) ---")
print("Считаем от 1 до 5:")
for i in range(1, 6):
    print(f"Шаг цикла: {i}")


print("\n--- 3. Цикл с условием (while) ---")
print("Обратный отсчет ракетоносца:")
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1

print("Пуск! 🚀")


----------


# Lesson 2: Conditions (if/elif/else) and loops (for, while)

print("--- 1. Conditional statements (if, elif, else) ---")
age = int(input("How old are you? "))

if age < 18:
    print("You are still a minor.")
elif age == 18:
    print("Happy 18th birthday!")
else:
    print("You are an adult.")

print("\n--- 2. Counter loop (for) ---")
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Loop step: {i}")

print("\n--- 3. Conditional loop (while) ---")
print("Rocket launch countdown:")
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1

print("Lift-off! 🚀")
