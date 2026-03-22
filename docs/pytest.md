##  Prerequisites

- Python installed
- Basic knowledge of the Python programming language



##  Why do we use pytest?

**pytest** is a popular Python testing framework that makes writing and running tests easier.

Unlike `unittest` and other frameworks:
- simpler syntax
- less boilerplate code
- cleaner and more readable tests

It supports, among others:
- Flask
- Django
- and other Python frameworks

With its rich feature set, it provides all the necessary tools for developing reliable software.



##  Key Features

-  Flexibility – tests can be written for functions, classes, and modules
-  Detailed output – easy-to-understand error reports
-  Automatic test discovery – `test_*.py`, `*_test.py`
-  Parameterization – run tests with multiple inputs
-  Fixtures – reduce repetitive code
-  Plugins – easy extensibility
-  Compatibility – works together with unittest



#  Writing Your First Test

## Installation

```bash
pip install pytest
```

## Importing

```python
import pytest
```



##  Two Basic Approaches

### Function-based

```python
def test_addition():
    assert 1 + 1 == 2
```

### Class-based

```python
class TestMathOperations:
    def test_addition(self):
        assert 1 + 1 == 2
```



#   Running Tests

### All tests
```bash
pytest
```

### Specific file
```bash
pytest test_example.py
```

### By keyword
```bash
pytest -k "keyword"
```

### A specific test
```bash
pytest test_example.py::test_addition
```



#  Understanding Results

pytest provides a detailed report:
- which test ran
- which succeeded
- which failed
- exactly where the error occurred

This greatly helps with debugging.



#  Handling Exceptions

```python
with pytest.raises(ValueError):
    calculate_square_root(-1)
```

If the exception occurs → the test is successful.



#  Advanced Features

##  Markers

Markers label tests and control how they are executed.

### 🔹 skip – always skip

```python
import pytest

@pytest.mark.skip(reason="The feature is not implemented yet")
def test_new_feature():
    assert 2 + 2 == 4
```

Useful when:
- the feature is not ready yet
- temporary bug
- faster execution



### 🔹 skipif – conditional skip

```python
import sys
import pytest

@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_linux_only_feature():
    assert True
```

Useful for:
- OS-dependent tests
- Python version dependent tests
- missing dependency



### 🔹 xfail – expected failure

```python
import pytest

@pytest.mark.xfail(reason="Known bug: division by zero is not handled")
def test_divide_by_zero():
    assert divide(10, 0) == 0
```

Behavior:
- runs
- failure → OK (XFAIL)
- success → XPASS (unexpected)

Useful for:
- known bugs
- incomplete features
- regression tests



##  Fixtures

Reusable test data:

```python
import pytest

@pytest.fixture
def user():
    return {"name": "Alice"}
```

Advantages:
- less repetition
- cleaner code
- easier maintenance



##  Parameterization

```python
import pytest

@pytest.mark.parametrize("x, expected", [
    (2, 4),
    (3, 9),
    (0, 0)
])
def test_square(x, expected):
    assert x*x == expected
```

One test runs with multiple inputs.

---

##  Plugins

Extra features:

```bash
pip install pytest-NAME
```

Examples:
- coverage measurement
- detailed reports
- Django integration
