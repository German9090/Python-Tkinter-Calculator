# [EN]
import math
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x600")
window.configure(bg='lightblue')

# Create the entry widget to display the input and result
entry = tk.Entry(window, width=20, font=('Arial', 24), justify="right", bd=10, insertwidth=2, bg='white')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Initialize variables to store the current value and operation
current_value = 0
current_operation = None

# Define the callback function for button clicks
def on_click(value):
    global current_value, current_operation
    if value.isdigit():
        # If a digit is pressed, append it to the current value in the entry widget
        current = entry.get()  # Get the current value from the entry widget
        entry.delete(0, tk.END)  # Clear the entry widget
        entry.insert(0, current + value)  # Insert the new value into the entry widget
    elif value in ['+', '-', '*', '/']:
        # If an operation is pressed, store the current value and operation
        current_value = float(entry.get())  # Convert the current value to a float and store it
        current_operation = value  # Store the current operation
        entry.delete(0, tk.END)  # Clear the entry widget
    elif value == '=':
        # If the '=' button is pressed, perform the calculation
        second_value = float(entry.get())  # Get the second value from the entry widget
        entry.delete(0, tk.END)  # Clear the entry widget
        result = 0  # Initialize the result variable
        if current_operation == '+':
            result = current_value + second_value  # Perform addition
        elif current_operation == '-':
            result = current_value - second_value  # Perform subtraction
        elif current_operation == '*':
            result = current_value * second_value  # Perform multiplication
        elif current_operation == '/':
            result = current_value / second_value  # Perform division
        if result.is_integer():
            result = int(result)  # Convert the result to an integer if it is a whole number
        entry.insert(0, result)  # Insert the result into the entry widget
    elif value == 'C':
        # If the 'C' button is pressed, clear the entry widget and reset variables
        entry.delete(0, tk.END)  # Clear the entry widget
        current_value = 0  # Reset the current value
        current_operation = None  # Reset the current operation

# Define the callback function for engineering buttons
def on_eng_buttons(value):
    current = float(entry.get())  # Get the current value from the entry widget and convert it to a float
    entry.delete(0, tk.END)  # Clear the entry widget
    result = 0  # Initialize the result variable
    if value == "x²":
        result = current ** 2  # Calculate the square of the current value
    elif value == "√x":
        result = current ** 0.5  # Calculate the square root of the current value
    elif value == "x^y":
        second_value = float(entry.get())  # Get the second value from the entry widget and convert it to a float
        result = current ** second_value  # Calculate the current value raised to the power of the second value
    elif value == "sin":
        result = math.sin(math.radians(current))  # Calculate the sine of the current value (in degrees)
    elif value == "cos":
        result = math.cos(math.radians(current))  # Calculate the cosine of the current value (in degrees)
    elif value == "tan":
        result = math.tan(math.radians(current))  # Calculate the tangent of the current value (in degrees)
    if result.is_integer():
        result = int(result)  # Convert the result to an integer if it is a whole number
    entry.insert(0, result)  # Insert the result into the entry widget

# Create a function to display engineering buttons
def show_eng_buttons():
    buttons = ['x²', '√x', 'x^y', 'sin', 'cos', 'tan']  # List of engineering buttons
    for i, button in enumerate(buttons):
        tk.Button(window, text=button, font=('Arial', 18), bg='white', fg='black', bd=5,
                  command=lambda t=button: on_eng_buttons(t)).grid(row=5 + i // 3, column=i % 3, padx=5, pady=5)

# Create digit buttons and place them in the grid
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1)
]

for (text, row, col) in buttons:
    tk.Button(window, text=text, font=('Arial', 18), bg='white', fg='black', bd=5,
              command=lambda t=text: on_click(t)).grid(row=row, column=col, padx=5, pady=5)

# Create operation buttons and place them in the grid
operations = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3), ('=', 4, 2), ('C', 4, 0)
]

for (text, row, col) in operations:
    tk.Button(window, text=text, font=('Arial', 18), bg='orange', fg='black', bd=5,
              command=lambda t=text: on_click(t)).grid(row=row, column=col, padx=5, pady=5)

# Create a button to display engineering buttons
tk.Button(window, text="Eng", font=('Arial', 18), bg='blue', fg='white', bd=5,
          command=show_eng_buttons).grid(row=5, column=3, padx=5, pady=5)

# Run the main event loop
window.mainloop()

# [RU]
import math
import tkinter as tk

# Создаем главное окно
window = tk.Tk()
window.title("Калькулятор")
window.geometry("400x600")
window.configure(bg='lightblue')

# Создаем виджет ввода для отображения ввода и результата
entry = tk.Entry(window, width=20, font=('Arial', 24), justify="right", bd=10, insertwidth=2, bg='white')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Инициализируем переменные для хранения текущего значения и операции
current_value = 0
current_operation = None

# Определяем функцию обратного вызова для нажатий кнопок
def on_click(value):
    global current_value, current_operation
    if value.isdigit():
        # Если нажата цифра, добавляем ее к текущему значению в виджете ввода
        current = entry.get()  # Получаем текущее значение из виджета ввода
        entry.delete(0, tk.END)  # Очищаем виджет ввода
        entry.insert(0, current + value)  # Вставляем новое значение в виджет ввода
    elif value in ['+', '-', '*', '/']:
        # Если нажата операция, сохраняем текущее значение и операцию
        current_value = float(entry.get())  # Преобразуем текущее значение в число с плавающей точкой и сохраняем его
        current_operation = value  # Сохраняем текущую операцию
        entry.delete(0, tk.END)  # Очищаем виджет ввода
    elif value == '=':
        # Если нажата кнопка '=', выполняем расчет
        second_value = float(entry.get())  # Получаем второе значение из виджета ввода
        entry.delete(0, tk.END)  # Очищаем виджет ввода
        result = 0  # Инициализируем переменную для результата
        if current_operation == '+':
            result = current_value + second_value  # Выполняем сложение
        elif current_operation == '-':
            result = current_value - second_value  # Выполняем вычитание
        elif current_operation == '*':
            result = current_value * second_value  # Выполняем умножение
        elif current_operation == '/':
            result = current_value / second_value  # Выполняем деление
        if result.is_integer():
            result = int(result)  # Преобразуем результат в целое число, если он является целым числом
        entry.insert(0, result)  # Вставляем результат в виджет ввода
    elif value == 'C':
        # Если нажата кнопка 'C', очищаем виджет ввода и сбрасываем переменные
        entry.delete(0, tk.END)  # Очищаем виджет ввода
        current_value = 0  # Сбрасываем текущее значение
        current_operation = None  # Сбрасываем текущую операцию

# Определяем функцию обратного вызова для инженерных кнопок
def on_eng_buttons(value):
    current = float(entry.get())  # Получаем текущее значение из виджета ввода и преобразуем его в число с плавающей точкой
    entry.delete(0, tk.END)  # Очищаем виджет ввода
    result = 0  # Инициализируем переменную для результата
    if value == "x²":
        result = current ** 2  # Вычисляем квадрат текущего значения
    elif value == "√x":
        result = current ** 0.5  # Вычисляем квадратный корень текущего значения
    elif value == "x^y":
        second_value = float(entry.get())  # Получаем второе значение из виджета ввода и преобразуем его в число с плавающей точкой
        result = current ** second_value  # Вычисляем текущее значение, возведенное в степень второго значения
    elif value == "sin":
        result = math.sin(math.radians(current))  # Вычисляем синус текущего значения (в градусах)
    elif value == "cos":
        result = math.cos(math.radians(current))  # Вычисляем косинус текущего значения (в градусах)
    elif value == "tan":
        result = math.tan(math.radians(current))  # Вычисляем тангенс текущего значения (в градусах)
    if result.is_integer():
        result = int(result)  # Преобразуем результат в целое число, если он является целым числом
    entry.insert(0, result)  # Вставляем результат в виджет ввода

# Создаем функцию для отображения инженерных кнопок
def show_eng_buttons():
    buttons = ['x²', '√x', 'x^y', 'sin', 'cos', 'tan']  # Список инженерных кнопок
    for i, button in enumerate(buttons):
        tk.Button(window, text=button, font=('Arial', 18), bg='white', fg='black', bd=5,
                  command=lambda t=button: on_eng_buttons(t)).grid(row=5 + i // 3, column=i % 3, padx=5, pady=5)

# Создаем кнопки с цифрами и размещаем их в сетке
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1)
]

for (text, row, col) in buttons:
    tk.Button(window, text=text, font=('Arial', 18), bg='white', fg='black', bd=5,
              command=lambda t=text: on_click(t)).grid(row=row, column=col, padx=5, pady=5)

# Создаем кнопки операций и размещаем их в сетке
operations = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3), ('=', 4, 2), ('C', 4, 0)
]

for (text, row, col) in operations:
    tk.Button(window, text=text, font=('Arial', 18), bg='orange', fg='black', bd=5,
              command=lambda t=text: on_click(t)).grid(row=row, column=col, padx=5, pady=5)

# Создаем кнопку для отображения инженерных кнопок
tk.Button(window, text="Eng", font=('Arial', 18), bg='blue', fg='white', bd=5,
          command=show_eng_buttons).grid(row=5, column=3, padx=5, pady=5)

# Запускаем главный цикл событий
window.mainloop()
