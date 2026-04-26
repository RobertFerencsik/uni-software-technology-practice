# Control Flow

Conditional statements
```
if if_expression:
    branch_1
elif:
    branch_2
else:
    branch_3
```

Loops

For loop
```
for i in range(5):
    print(i)
```

While loop
```
i = 0
while i < 5:
    print(i)
    i += 1
```

Loop Control Statements

break - exits the loop

continue - skips current iteration

pass - placeholder statement

Pattern Matching
```
value = 2
match value:
    case 1:
        branch_1
    case 2:
        branch_2
    case _:
        branch_default
```
Pythonic practices

1. Use for loop whenever you can
```
for item in items:
    print(item)
```
2. Use `enumerate()` for indexes iteration
```
for index, value in enumerate(items):
    print(index, value)
```
3. Use `any()` and `all()` for boolean checks
```
if any(x > 20 for x in numbers):
    print("found")
```
4. Use conditional expressions (ternary operator)
`status = "adult" if age >= 18 else "minor"
5. Prefer guard clauses to reduce nesting - code struncturing technique used to immediately exit a function when invalid input or states detected
```
if not valid:
    return
```

[<- Back to Python fundamentals](./python-fundamentals.md)
