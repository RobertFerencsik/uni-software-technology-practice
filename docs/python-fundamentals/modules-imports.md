# Modules & Imports

Moduels are python files contatining functions, classes, or variables that can be reused in other programs. (simple .py file)

```
# file: my_module.py
def greet(name):
    return f"Hello, {name}"
# file: main.py
import my_module
print(my_module.greet("Alice"))
```
1. basic import: import math
2. import with alias: import numpy as np
3. import specific items: from math import sqrt, pi
4. import all(not recommended): from math import *

Package is a directory with and __init__.py file that contains multiple modules

my_package/
    __init__.py
    module1.py
    module2.py

`from my_package import module1`

Organize imports standard, thrid-package, local

Lazy import: import inside functions to reduce startup time or avoid circular dependencies

[<- Back to Python fundamentals](./python-fundamentals.md)
