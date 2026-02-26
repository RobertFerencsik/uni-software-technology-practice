# Python fundamentals
- First released in 1991, created by Guido van Rossum
- High level, general-purpose, interpreted, dynamically typed
- designed: be simple, readable, easy to learn
- supports: procedural, OOP, functional
- Large standard lib, and huge ecosystem of third-party packages
- Widely used in: web dev, automation, data science, ai, scripting
[Documentation](https://docs.python.org/3/library/index.html)

## Running python

**Running interactive mode**
`python` interactive REPL (Read-Eval-Print Loop), use it to test a small piece of code
`quit() / exit` leave the interactive mode

**Running scripts**
`python script.py` run a python [script](# "file containing executable python code to accomplish a specific task")
`python script.py > output.txt` redirection: output redirected, creates the txt, or overwrites it, use `>>` to add the output instead of overwrite

**Running modules**
`python -m module_name` run [module](# "file containing python code that is designed to be imported and used from another python file") cli, module name no .py suffix! Use this when:
- module designed as a command-line tool
- running something inside package
- avoid environment / version confusion
- working with wirutal environments

**Run with import**
`import module_name` runs executable code in the imported module once
```python
import importlib
importlib.import_module("module_name") # imports module programmatically
importlib.reload(module_name) # forces the interpreter to import module again
```

**Run with exec()**
Run scripts from inside your code
```python
exec("python_code_as_string") # runs the string as python code
with open("script.py") as script # you can read it from file too
    exec(script.read())
```
**Sources**
[Real Python: run scripts and code](https://realpython.com/run-python-scripts/)
## Variables & assignement

int
float
complex
bool
str

