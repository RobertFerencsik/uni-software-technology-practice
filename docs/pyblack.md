# Black: The Uncompromising Python Code Formatter

## Prerequisites

- Python 3.8+ installed
- Basic understanding of Python syntax
- Terminal or Command Line access

---

## What is Black?

**Black** is the "uncompromising" Python code formatter. By using it, you cede control over the minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from style-related distractions.

---

### Why is it different?
Unlike other formatters (like `autopep8` or `yapf`), Black has very few configuration options. This is intentional: it ensures that **all** Python code formatted with Black looks the same, regardless of who wrote it.

**Key Benefits:**
- **Stop the Debates:** No more arguments in Code Reviews about tabs vs. spaces or where a bracket should go.
- **Save Time:** Focus on logic, let the machine handle the aesthetics.
- **Deterministic:** The same code will always result in the exact same output.
- **AST Verification:** Before saving, Black checks if the code still functions exactly the same way to ensure no bugs were introduced.

---

## Installation

Install Black via pip:

```bash
pip install black
```

---

## Basic Usage

### Format a file

```bash
black script.py
```

### Format a whole project

```bash
black .
```

### Check formatting (no changes)

```bash
black --check .
```

### Show difference

```bash
black --diff .
```

### Quiet/verbose

```bash
black --quiet .
black --verbose .
```

---

## Formatting in action
Black reformats your code to be more readable and consistent.

### Before (Messy)

```python
def my_function(  name,age,
    city):
    items = [1,2,
        3,4,5]
    return {"name":name,"age":age,"city":city}
```
### After Black

```python
def my_function(name, age, city):
    items = [1, 2, 3, 4, 5]
    return {"name": name, "age": age, "city": city}
```

---

## Configuration
Black is famous for having very few settings. However, you can store your preferences in a pyproject.toml file at the root of your project:

```toml
[tool.black]
line-length = 88
target-version = ['py311']
include = '\.pyi?$'
extend-exclude = '/(venv|\.git|build|dist)/'
```

- **Line-length:** Max characters per line (default is 88).
- **Target-version:** The Python version the code should be compatible with.
- **Exclude:** Folders Black should ignore (like virtual environments).

## Editor Integration
To get the most out of Black, you should automate it so you never have to run the command manually.

### VS Code
1. Install the Black Formatter extension by Microsoft.
2. Open Settings (Ctrl + ,).
3. Search for "Format on Save" and enable it.
4. Set "Default Formatter" to Black Formatter.