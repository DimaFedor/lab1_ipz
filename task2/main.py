# Функція для обчислення чисел Фібоначчі
def fibonacci(n):
    fib_sequence = [0, 1]  # Початок ряду Фібоначчі
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]  # Наступне число - сума двох попередніх
        fib_sequence.append(next_value)
    return fib_sequence[:n]  # Повертаємо перші n чисел

# Введення користувача
num = int(input("Введіть кількість чисел Фібоначчі, які потрібно розрахувати: "))

# Виведення результату
if num > 0:
    print(f"Перші {num} чисел Фібоначчі: {fibonacci(num)}")
else:
    print("Будь ласка, введіть додатне ціле число.")
