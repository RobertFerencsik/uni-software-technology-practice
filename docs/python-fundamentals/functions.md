# Functions

use_snake_case naming, defined by `def`

Basic form
```
def greet(name):
    """Docstring, for documenting what the function does"""
    return "Hello " + name
greet("Alice")
```

*args & **kwargs (arguments & keyword arguments) - use them when arbitrary number of arguments are expected, or to unpack iterable into arguments
```
def func(*args, **kwargs):
    print(args)
    print(kwargs)
func(1, 2, x=10, y=20)

def func(a, b, c, x=0, y=0)
    print(a, b, c, x, y)

args = (1, 2, 3)
kwargs = {"x": 10, "y": 20}
func(*args, **kwargs)
```

Lambda functions - small anonymous function: lambda arguments: expression (use for sorting with key, map() to apply for every element, filter() elements by condition)
```
square = lambda x: x * x
square(3)
```

[<- Back to Python fundamentals](./python-fundamentals.md)
