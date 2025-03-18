#[EN] Import required libraries
#[RU] Импорт необходимых библиотек
import tkinter as tk
from tkinter.messagebox import showerror, showwarning, showinfo
import math

#[EN] Create and configure the main window
#[RU] Создание и настройка главного окна
window = tk.Tk()
window.title("Calculator")
window.geometry("475x500")
window.config(bg="lightblue")

#[EN] Create input field
#[RU] Создание поля ввода
entry = tk.Entry(window, width=25, font=("Arial", 24), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#[EN] Initialize variables for calculations
#[RU] Инициализация переменных для вычислений
current_value, current_operation = 0, None

def format_result(result):
    #[EN] Format result: int for integers, float for decimals
    #[RU] Форматирование результата: int для целых чисел, float для дробных
    return int(result) if result.is_integer() else result

#[EN] Handler for basic calculator operations
#[RU] Обработчик базовых операций калькулятора
def on_click(value):
    global current_value, current_operation
    if value.isdigit() or value == ".":
        entry.insert(tk.END, value)
    elif value in ["+", "-", "*", "/"]:
        current_value, current_operation = float(entry.get()), value
        entry.delete(0, tk.END)
    elif value == "=":
        try:
            if current_operation == "**":  # [EN] Check for exponentiation operation
                                           # [RU] Проверяем операцию возведения в степень
                result = current_value ** float(entry.get())
            else:
                result = eval(f"{current_value} {current_operation} {float(entry.get())}")
            entry.delete(0, tk.END)
            entry.insert(0, format_result(float(result)))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
            showerror(title="Error", message=f"Похоже есть ошибка: {e}")

#[EN] Handler for engineering calculator operations
#[RU] Обработчик инженерных операций калькулятора
def on_eng_click(op):
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)

        if op == "xʸ":
            global current_value, current_operation
            current_value = value
            current_operation = "**"  
            return  

        result = {
            "x²": value**2,
            "√x": math.sqrt(value),
            "sin": math.sin(math.radians(value)),
            "cos": math.cos(math.radians(value)),
            "tan": math.tan(math.radians(value)),
            "log": math.log10(value)
        }[op]
        entry.insert(0, format_result(float(result)))
    except ValueError:
        entry.insert(0, "Error")
        showerror(title="Error", message="Пожалуйста, введите числовое значение.")
    except Exception as e:
        entry.insert(0, "Error")
        showerror(title="Error", message=f"Похоже есть ошибка: {e}")

#[EN] Handler for unit converter operations
#[RU] Обработчик операций конвертера единиц
def on_conv_click(conv):
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        result = {
            "Miles->Km": value * 1.60934,
            "Pounds->Kg": value * 0.453592,
            "℉->℃": (value - 32) * 5/9,
            "Feets->Meters": value * 0.3048,
            "Gallons->Liters": value * 3.78541
        }[conv]
        entry.insert(0, format_result(float(result)))
    except ValueError:
        entry.insert(0, "Error")
        showerror(title="Error", message="Пожалуйста, введите числовое значение.")
    except Exception as e:
        entry.insert(0, "Error")
        showerror(title="Error", message=f"Похоже есть ошибка: {e}")

#[EN] Function to solve quadratic equations
#[RU] Функция для решения квадратных уравнений
def solve_quadratic_equation():
    try:
        a = float(entry_a_quad.get())
        b = float(entry_b_quad.get())
        c = float(entry_c_quad.get())
        if a == 0:
            result_label.config(text="Ошибка: коэффициент a не может быть 0")
            return

        D = b**2 - 4*a*c
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2*a)
            x2 = (-b - math.sqrt(D)) / (2*a)
            steps = f"1. Дискриминант D = {D:.2f}\n"
            steps += f"2. Корни уравнения: x1 = {x1:.2f}, x2 = {x2:.2f}"
            result_label.config(text=steps)
            entry.delete(0, tk.END)
            entry.insert(0, f"x1 = {format_result(x1)}, x2 = {format_result(x2)}")
        elif D == 0:
            x = -b / (2*a)
            steps = f"1. Дискриминант D = {D:.2f}\n"
            steps += f"2. Корень уравнения: x = {x:.2f}"
            result_label.config(text=steps)
            entry.delete(0, tk.END)
            entry.insert(0, format_result(x))
        else:
            result_label.config(text="Корней нет, так как дискриминант меньше нуля")
            entry.delete(0, tk.END)
            entry.insert(0, "Корней нет")
    except ValueError:
        result_label.config(text="Ошибка: введите числовые значения")
        showerror(title="Error", message="Пожалуйста, введите числовые значения для a, b и c.")
    except Exception as e:
        result_label.config(text="Ошибка: произошла ошибка")
        showerror(title="Error", message=f"Похоже есть ошибка: {e}")

#[EN] Function to solve linear equations
#[RU] Функция для решения линейных уравнений
def solve_linear_equation():
    try:
        a = float(entry_a_lin.get())
        b = float(entry_b_lin.get())
        if a == 0:
            result_label.config(text="Ошибка: коэффициент a не может быть 0")
            return

        x = -b / a
        steps = f"1. Преобразуем уравнение: {a}x + {b} = 0\n"
        steps += f"2. Решаем уравнение: x = {-b} / {a}\n"
        steps += f"3. Ответ: x = {x:.2f}"
        result_label.config(text=steps)
        entry.delete(0, tk.END)
        entry.insert(0, format_result(x))
    except ValueError:
        result_label.config(text="Ошибка: введите числовые значения")
        showerror(title="Error", message="Пожалуйста, введите числовые значения для a и b.")
    except Exception as e:
        result_label.config(text="Ошибка: произошла ошибка")
        showerror(title="Error", message=f"Похоже есть ошибка: {e}")

#[EN] Clear input field function
#[RU] Функция очистки поля ввода
def clear():
    entry.delete(0, tk.END)

#[EN] Function to switch between calculator modes
#[RU] Функция переключения между режимами калькулятора
def switch_mode(node):
    global entry
    current_text = entry.get()

    #[EN] Clear all widgets and recreate input field
    #[RU] Очистка всех виджетов и пересоздание поля ввода
    for widget in window.winfo_children():
        widget.destroy()

    entry = tk.Entry(window, width=25, font=("Arial", 24), justify="right")
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    entry.insert(0, current_text)

    #[EN] Create mode selection buttons
    #[RU] Создание кнопок выбора режима
    modes = ["Normal", "Engineering", "Converter", "Equations"]
    for i, m in enumerate(modes):
        tk.Button(window, text=m, bg="blue", fg="white", command=lambda t=m: switch_mode(t.lower())).grid(row=1, column=i)

    #[EN] Define button layouts for different modes
    #[RU] Определение расположения кнопок для разных режимов
    buttons = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),
        ('0', 5, 1), ('.', 5, 0), ('C', 5, 2)
    ]

    ops = [
        ('+', 2, 3), ('-', 3, 3), ('*', 4, 3),
        ('/', 5, 3), ('=', 6, 2)
    ]

    eng_buttons = [
        ('x²', 2, 0), ('√x', 2, 1), ('sin', 2, 2),
        ('cos', 3, 0), ('tan', 3, 1), ('log', 3, 2),
        ('xʸ', 4, 0)
    ]

    conv_buttons = [
        ('Miles->Km', 2, 0), ('Pounds->Kg', 2, 1), ('℉->℃', 2, 2),
        ('Feets->Meters', 3, 0), ('Gallons->Liters', 3, 1)
    ]

    #[EN] Create buttons based on selected mode
    #[RU] Создание кнопок в зависимости от выбранного режима
    if node == "normal":
        for text, row, col in buttons:
            cmd = clear if text == 'C' else lambda t=text: on_click(t)
            tk.Button(window, text=text, font=("Arial", 18), command=cmd).grid(row=row, column=col)
        for text, row, col in ops:
            tk.Button(window, text=text, font=("Arial", 18), bg="orange", fg="white", command=lambda t=text: on_click(t)).grid(row=row, column=col)

    elif node == "engineering":
        for text, row, col in eng_buttons:
            tk.Button(window, text=text, font=("Arial", 18), command=lambda t=text: on_eng_click(t)).grid(row=row, column=col)
        tk.Button(window, text="C", font=("Arial", 18), command=clear).grid(row=4, column=2)

    elif node == "equations":
        #[EN] Quadratic equation section
        #[RU] Секция для квадратных уравнений
        tk.Label(window, text="Введите коэффициенты a, b, c для квадратного уравнения:", bg="lightblue").grid(row=2, column=0, columnspan=4)
        global entry_a_quad, entry_b_quad, entry_c_quad, entry_a_lin, entry_b_lin, result_label
        entry_a_quad = tk.Entry(window)
        entry_a_quad.grid(row=3, column=0, padx=5, pady=5)
        entry_b_quad = tk.Entry(window)
        entry_b_quad.grid(row=3, column=1, padx=5, pady=5)
        entry_c_quad = tk.Entry(window)
        entry_c_quad.grid(row=3, column=2, padx=5, pady=5)
        
        # [EN] Adding example of correct input
        # [RU] Добавление примера правильного ввода
        example_label = tk.Label(window, text="Пример: a=1, b=-3, c=2", bg="lightblue", fg="gray")
        example_label.grid(row=4, column=0, columnspan=3, pady=5)
        
        solve_button = tk.Button(window, text="Решить квадратное уравнение", command=solve_quadratic_equation, bg="orange", fg="white")
        solve_button.grid(row=5, column=0, columnspan=3, pady=10)
        
        #[EN] Linear equation section
        #[RU] Секция для линейных уравнений
        tk.Label(window, text="Введите коэффициенты a, b для линейного уравнения:", bg="lightblue").grid(row=6, column=0, columnspan=4)
        entry_a_lin = tk.Entry(window)
        entry_a_lin.grid(row=7, column=0, padx=5, pady=5)
        entry_b_lin = tk.Entry(window)
        entry_b_lin.grid(row=7, column=1, padx=5, pady=5)
        
        solve_button = tk.Button(window, text="Решить линейное уравнение", command=solve_linear_equation, bg="orange", fg="white")
        solve_button.grid(row=8, column=0, columnspan=3, pady=10)
        
        result_label = tk.Label(window, text="", justify="left", bg="lightblue")
        result_label.grid(row=9, column=0, columnspan=4)

    elif node == "converter":
        for text, row, col in conv_buttons:
            tk.Button(window, text=text, font=("Arial", 14), command=lambda t=text: on_conv_click(t)).grid(row=row, column=col)
        tk.Button(window, text="C", font=("Arial", 18), command=clear).grid(row=3, column=2)

#[EN] Start the calculator in basic mode
#[RU] Запуск калькулятора в обычном режиме
switch_mode("normal")
window.mainloop()
