# 🧮 Python Calculator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Status-Complete-success" alt="Status">
  <img src="https://img.shields.io/badge/Level-Beginner-orange" alt="Level">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

<p align="center">
  A simple and beginner-friendly command-line calculator built with Python 🐍
</p>

---

## 📖 About The Project

**Python Calculator** is a simple command-line application developed with Python.

The calculator performs the four basic mathematical operations:

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division

The main purpose of this project is not only to create a calculator, but also to practice fundamental Python concepts such as:

* User input
* Variables
* Type conversion
* Conditional statements
* Exception handling
* String methods
* Escape characters
* Arithmetic and comparison operators

This makes the project suitable for people who are starting their journey with Python.

---

## ✨ Features

* 🔢 Supports integer and decimal numbers
* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* 🛡️ Basic error handling
* 🚫 Division-by-zero protection
* 💻 Simple command-line interface
* 🐍 Written using standard Python features
* 📦 No external dependencies

---

## 🖥️ Example

```text
        Welcome to my Calculator

----------------------------------------

        Enter First Number : 25
        Enter Second Number : 5

Please Choose Your Operation From *,/,+,- : *

----------------------------------------

                 125.0
```

### Division Example

```text
        Enter First Number : 20
        Enter Second Number : 4

Please Choose Your Operation From *,/,+,- : /

----------------------------------------

                 5.0
```

---

# 🚀 Getting Started

## 📋 Prerequisites

Before running the project, make sure you have **Python 3** installed.

You can check your Python version with:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/Mahdiyy2244/python-calculator.git
```

Enter the project directory:

```bash
cd python-calculator
```

Run the calculator:

```bash
python calculator.py
```

If your system uses `python3`:

```bash
python3 calculator.py
```

---

# 📚 Educational Explanation

This section explains some of the important Python concepts used in the project.

## `input()`

The `input()` function receives data from the user.

```python
name = input("Enter your name: ")
```

Everything received from `input()` is initially a **string**.

For example, if the user enters:

```text
25
```

Python initially receives:

```python
"25"
```

not the number `25`.

---

## `float()`

The `float()` function converts a value into a floating-point number.

```python
num1 = float(input("Enter First Number: "))
```

This allows the calculator to accept values such as:

```text
10
5.5
3.14
```

For example:

```python
float("10")
```

produces:

```text
10.0
```

---

## `\t`

`\t` is an **escape character** representing a horizontal tab.

Example:

```python
print("\tHello")
```

It adds indentation before `Hello`.

The calculator uses it to make the terminal output more organized:

```python
print("\tWelcome to my Calculator")
```

---

## `print()`

The `print()` function displays information in the terminal.

Example:

```python
print("Hello World")
```

Output:

```text
Hello World
```

It can also display variables:

```python
num = 10
print(num)
```

---

## String Repetition with `*`

Python allows strings to be repeated using the multiplication operator.

```python
print("-" * 40)
```

Output:

```text
----------------------------------------
```

This is useful for creating visual separators in command-line programs.

---

## `.upper()`

`.upper()` is a string method that converts letters to uppercase.

Example:

```python
message = "hello"

print(message.upper())
```

Output:

```text
HELLO
```

The calculator can use it for important messages:

```python
print("A number cannot be divided by zero.".upper())
```

Result:

```text
A NUMBER CANNOT BE DIVIDED BY ZERO.
```

---

# 🔀 Conditional Statements

The calculator uses `if`, `elif`, and `else` to determine which operation the user selected.

Example:

```python
if opr == '*':
    print(num1 * num2)

elif opr == '/':
    print(num1 / num2)

elif opr == '+':
    print(num1 + num2)

elif opr == '-':
    print(num1 - num2)
```

### `if`

Checks the first condition.

```python
if opr == '*':
```

It asks:

> Is the selected operation `*`?

If the answer is yes, multiplication is performed.

### `elif`

`elif` means **else if**.

It allows Python to check another condition if the previous condition was false.

### `else`

`else` can be used when none of the previous conditions are true.

---

# ➗ Division by Zero

Dividing a number by zero is not allowed.

For example:

```python
10 / 0
```

causes a `ZeroDivisionError`.

Therefore, the calculator should check the second number before division:

```python
if num2 != 0:
    print(num1 / num2)
else:
    print("A number cannot be divided by zero.".upper())
```

Here:

```python
!=
```

means **not equal to**.

So:

```python
num2 != 0
```

means:

> `num2` is not zero.

---

# 🛡️ `try` / `except`

The calculator uses exception handling to deal with invalid input.

Example:

```python
try:
    num1 = float(input("Enter First Number: "))
except ValueError:
    print("The entered value must be numeric.")
```

If the user enters:

```text
hello
```

Python cannot convert it into a `float`, so a `ValueError` occurs.

Instead of crashing, the program can display a friendly error message.

### Why `ValueError` instead of bare `except`?

Using:

```python
except ValueError:
```

is generally better than:

```python
except:
```

because it catches the specific type of error we expect.

---

# ➕ Mathematical Operators

Python provides several arithmetic operators:

| Operator | Operation      | Example | Result |
| :------: | -------------- | ------: | -----: |
|    `+`   | Addition       | `5 + 2` |    `7` |
|    `-`   | Subtraction    | `5 - 2` |    `3` |
|    `*`   | Multiplication | `5 * 2` |   `10` |
|    `/`   | Division       | `5 / 2` |  `2.5` |

---

# ⚖️ Comparison Operators

Comparison operators are used to compare values.

| Operator | Meaning                  |
| :------: | ------------------------ |
|   `==`   | Equal to                 |
|   `!=`   | Not equal to             |
|    `>`   | Greater than             |
|    `<`   | Less than                |
|   `>=`   | Greater than or equal to |
|   `<=`   | Less than or equal to    |

For example:

```python
opr == '+'
```

checks whether the value of `opr` is equal to `+`.

---

# 🧠 What I Learned

By building this project, I practiced:

* Python variables
* `input()`
* `print()`
* `float()`
* Strings
* String methods
* `.upper()`
* Escape characters such as `\t`
* Arithmetic operators
* Comparison operators
* `if / elif / else`
* `try / except`
* Basic exception handling
* Command-line applications

---

# 🔮 Future Improvements

Possible improvements for future versions:

* 🔄 Continuous calculations without restarting the program
* 🧮 More mathematical operations
* 📜 Calculation history
* 🎨 Improved terminal interface
* 🛡️ More specific error handling
* √ Square-root operation
* `**` Power operation
* `%` Modulo operation
* 🖥️ Graphical User Interface (GUI)

---

# 🤝 Contributing

Contributions are welcome! 🎉

If you would like to improve this project:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/improvement
```

3. Make your changes.
4. Commit your changes:

```bash
git commit -m "Add new calculator feature"
```

5. Push the branch:

```bash
git push origin feature/improvement
```

6. Open a Pull Request.

### 💡 Ideas for Contributions

You can contribute by:

* Fixing bugs
* Improving error handling
* Adding new mathematical operations
* Improving the user interface
* Improving documentation
* Adding tests
* Suggesting new features

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to:

* Use the project
* Copy the project
* Modify the project
* Distribute the project

See the `LICENSE` file for more information.

---

# ⭐ Support

If you found this project useful or it helped you learn Python, consider giving the repository a ⭐.

It really helps support the project!

---

## 👨‍💻 Author

Created with ❤️ and Python 🐍

**Happy Coding! 🚀**
