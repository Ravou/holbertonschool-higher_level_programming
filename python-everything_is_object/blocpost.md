# Python Objects: Mutable vs Immutable

![Python Objects Memory](https://www.memorymanagement.org/_images/object-repr.png)
*Memory representation of Python objects*

## Introduction
In Python, everything is an object, and each object has a unique identity, a type, and a value. Understanding the difference between mutable and immutable objects is crucial for writing efficient and bug-free Python code. This distinction affects how objects are stored in memory, how they behave when modified, and how they're passed to functions.

## ID and Type
Every object in Python has an identity (a unique integer) and a type. The `id()` function returns the object's identity (its memory address), while `type()` returns its type. These characteristics are fixed once an object is created.

```python
x = 42
print(f"ID: {id(x)}, Type: {type(x)}")  # ID: 140736123456, Type: <class 'int'>

s = "hello"
print(f"ID: {id(s)}, Type: {type(s)}")  # ID: 12345678, Type: <class 'str'>
```

## Mutable Objects
Mutable objects can be changed after creation. Common mutable types in Python include:
- Lists
- Dictionaries
- Sets
- Byte Arrays
- User-defined classes (unless made immutable)

```python
# List example (mutable)
my_list = [1, 2, 3]
print(f"Original ID: {id(my_list)}")  # Original ID: 12345678
my_list.append(4)  # Modifying the list
print(f"After append ID: {id(my_list)}")  # Same ID: 12345678

# Dictionary example (mutable)
my_dict = {"a": 1, "b": 2}
print(f"Original dict: {my_dict}")
my_dict["c"] = 3  # Modifying the dictionary
print(f"Modified dict: {my_dict}")
```

## Immutable Objects
Immutable objects cannot be changed after creation. Common immutable types include:
- Integers
- Floats
- Strings
- Tuples
- Frozen sets
- Bytes

```python
# String example (immutable)
name = "Alice"
print(f"Original ID: {id(name)}")  # Original ID: 23456789
name = name + " Smith"  # Creates a new string object
print(f"After concatenation ID: {id(name)}")  # New ID: 34567890

# Tuple example (immutable)
coordinates = (10, 20)
print(f"Original tuple: {coordinates}")
# coordinates[0] = 5  # This would raise TypeError
```

## Why It Matters: Python's Treatment of Mutable vs Immutable Objects

Python treats mutable and immutable objects differently in terms of memory management and behavior:

1. **Memory Efficiency**: Python caches small integers and strings (interning) to save memory
2. **Performance**: Operations on immutable objects can be optimized by the interpreter
3. **Dictionary Keys**: Only immutable types can be used as dictionary keys
4. **Thread Safety**: Immutable objects are inherently thread-safe

```python
# Integer interning (immutable)
a = 10
b = 10
print(a is b)  # True - same object due to interning

# List comparison (mutable)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)  # False - different objects
print(list1 == list2)  # True - same content
```

## Function Arguments: Pass by Object Reference

In Python, arguments are passed by object reference. This means:
- For immutable objects, you can't modify the original object in a function
- For mutable objects, you can modify the object in place

```python
def modify_list(lst):
    lst.append(4)  # Modifies the original list
    print(f"Inside function: {lst}")

def modify_string(s):
    s = s + " world"  # Creates a new string
    print(f"Inside function: {s}")

# Mutable object (list)
numbers = [1, 2, 3]
modify_list(numbers)
print(f"Outside function: {numbers}")  # [1, 2, 3, 4]

# Immutable object (string)
greeting = "Hello"
modify_string(greeting)
print(f"Outside function: {greeting}")  # Still "Hello"
```

## Advanced Topic: Shallow vs Deep Copy

When working with mutable objects, it's important to understand the difference between shallow and deep copying:

```python
import copy

# Shallow copy
original = [[1, 2], [3, 4]]
shallow_copy = copy.copy(original)
shallow_copy[0][0] = 5
print(original)  # [[5, 2], [3, 4]] - nested list is shared!

# Deep copy
original = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(original)
deep_copy[0][0] = 5
print(original)  # [[1, 2], [3, 4]] - completely independent copy
```

Understanding these concepts will help you write more predictable and efficient Python code, especially when dealing with function arguments and data structures.
