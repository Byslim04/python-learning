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
