<p align="center">
   <img src="https://img.shields.io/badge/Python-Version%203.13.0-blueviolet" alt="Python Version">
   <img src="https://img.shields.io/badge/Version-v0.0.2%20(Alpha)-blue" alt="Version">
   <img src="https://img.shields.io/badge/License-MIT-succsess" alt="License">
</p>

## About

This is a simple calculator application built using Python and the Tkinter library. The calculator supports basic arithmetic operations as well as some engineering functions.

## Documentation

### How the Code Works

1. **Window Initialization**:

   The main application window is created with the title "Calculator", a size of 400x500 pixels, and a light blue background.

2. **Input Field**:

   An input field is created for displaying and entering numbers and results. The input field is placed in the first row and spans four columns.

3. **Global Variables**:

   Global variables are declared to store the current value and the current operation.

4. **Button Click Handling Function**:

   This function handles button clicks. If a digit is pressed, it is added to the current value in the input field. If an operation (+, -, *, /) is pressed, the current value is saved and the input field is cleared. If the "=" button is pressed, the corresponding operation is performed with the current and second values, and the result is displayed in the input field. If the "C" button is pressed, the input field is cleared and the global variables are reset.

5. **Creating Buttons**:

   Buttons with digits and operations are created and placed in the corresponding grid cells. The buttons receive additional styles to improve their appearance.

6. **Main Loop Execution**:

   The main event loop is started, allowing interaction with the interface.

### How to Run This File on macOS, Windows, and Linux

### Visual Studio Code

#### macOS

1. **Open the File**:
   - Open Visual Studio Code.
   - Go to `File` -> `Open File...` and select the file `Python Calculator.py`.

2. **Set Up Python Interpreter**:
   - Make sure Python is installed. If not, download and install it from the [official Python website](https://www.python.org/).
   - In Visual Studio Code, press `Cmd+Shift+P` to open the command palette.
   - Type `Python: Select Interpreter` and select the installed Python interpreter.

3. **Run the File**:
   - Open the terminal in Visual Studio Code by pressing `Cmd+`.
   - In the terminal, type the command:
     ```sh
     python3 "path/to/your/Python Calculator.py"
     ```
   - Press `Enter` to run the file.

#### Windows

1. **Open the File**:
   - Open Visual Studio Code.
   - Go to `File` -> `Open File...` and select the file `Python Calculator.py`.

2. **Set Up Python Interpreter**:
   - Make sure Python is installed. If not, download and install it from the [official Python website](https://www.python.org/).
   - In Visual Studio Code, press `Ctrl+Shift+P` to open the command palette.
   - Type `Python: Select Interpreter` and select the installed Python interpreter.

3. **Run the File**:
   - Open the terminal in Visual Studio Code by pressing `Ctrl+`.
   - In the terminal, type the command:
     ```sh
     python "path/to/your/Python Calculator.py"
     ```
   - Press `Enter` to run the file.

#### Linux

1. **Open the File**:
   - Open Visual Studio Code.
   - Go to `File` -> `Open File...` and select the file `Python Calculator.py`.

2. **Set Up Python Interpreter**:
   - Make sure Python is installed. If not, install it using the package manager for your Linux distribution. For example, on Ubuntu, run:
     ```sh
     sudo apt-get install python3
     ```
   - In Visual Studio Code, press `Ctrl+Shift+P` to open the command palette.
   - Type `Python: Select Interpreter` and select the installed Python interpreter.

3. **Run the File**:
   - Open the terminal in Visual Studio Code by pressing `Ctrl+`.
   - In the terminal, type the command:
     ```sh
     python3 "path/to/your/Python Calculator.py"
     ```
   - Press `Enter` to run the file.

### PyCharm

#### macOS

1. **Open the Project**:
   - Open PyCharm.
   - Go to `File` -> `Open...` and select the folder containing the file `Python Calculator.py`.

2. **Set Up Python Interpreter**:
   - Make sure Python is installed. If not, download and install it from the [official Python website](https://www.python.org/).
   - In PyCharm, go to `PyCharm` -> `Preferences...`.
   - In the `Project: <your_project_name>` section, select `Python Interpreter` and add the installed Python interpreter.

3. **Run the File**:
   - In the project window, find the file `Python Calculator.py` and open it.
   - Right-click on the file and select `Run 'Python Calculator'`.
   - PyCharm will run the file, and you will see the calculator window.

#### Windows

1. **Open the Project**:
   - Open PyCharm.
   - Go to `File` -> `Open...` and select the folder containing the file `Python Calculator.py`.

2. **Set Up Python Interpreter**:
   - Make sure Python is installed. If not, download and install it from the [official Python website](https://www.python.org/).
   - In PyCharm, go to `File` -> `Settings...`.
   - In the `Project: <your_project_name>` section, select `Python Interpreter` and add the installed Python interpreter.

3. **Run the File**:
   - In the project window, find the file `Python Calculator.py` and open it.
   - Right-click on the file and select `Run 'Python Calculator'`.
   - PyCharm will run the file, and you will see the calculator window.

#### Linux

1. **Open the Project**:
   - Open PyCharm.
   - Go to `File` -> `Open...` and select the folder containing the file `Python Calculator.py`.

2. **Set Up Python Interpreter**:
   - Make sure Python is installed. If not, install it using the package manager for your Linux distribution. For example, on Ubuntu, run:
     ```sh
     sudo apt-get install python3
     ```
   - In PyCharm, go to `File` -> `Settings...`.
   - In the `Project: <your_project_name>` section, select `Python Interpreter` and add the installed Python interpreter.

3. **Run the File**:
   - In the project window, find the file `Python Calculator.py` and open it.
   - Right-click on the file and select `Run 'Python Calculator'`.
   - PyCharm will run the file, and you will see the calculator window.

### IMPORTANT

To ensure that your file runs, please check the installation of the Tkinter library. Here is an example of how to do this:

1. **Verify Tkinter Installation**:

   Open a terminal and run the following command:
   ```sh
   python -m tkinter
   ```
   If Tkinter is installed, a window with a test interface will open. If not, follow the next step to install it.

2. **Install Tkinter**:

   On Windows and macOS, Tkinter is usually installed with Python. On Linux, you may need to install it separately. For Ubuntu, run:
   ```sh
   sudo apt-get install python3-tk
   ```
   
### Renaming the Application

To rename the application, follow these steps:

1. Open the file `Python Calculator.py`.
2. Find the line containing `window.title("Calculator")`.
3. Change the text `"Calculator"` to the desired name of your application.

Example:
```python
window.title("My Custom Calculator")
```

After this, your application will display the new name in the window title.

## Developers

- [NlinsO](https://github.com/NlinsO)

## License
This project is licensed under the MIT License.
