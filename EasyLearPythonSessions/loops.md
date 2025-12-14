Sure! Here are some exercises that involve different types of `for` loops in Python, including `for` loops in various contexts such as iterating over lists, dictionaries, strings, and ranges.

### Exercise 1: Iterate Over a List
**Problem:** Write a program that iterates over a list of numbers and prints each number multiplied by 2.

```python
# Sample list of numbers
numbers = [1, 2, 3, 4, 5]

# Using for loop to iterate over the list
for num in numbers:
    print(num * 2)
```

### Exercise 2: Iterate Over a Dictionary
**Problem:** Write a program that iterates over a dictionary and prints each key-value pair.

```python
# Sample dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Using for loop to iterate over the dictionary
for key, value in person.items():
    print(f"{key}: {value}")
```

### Exercise 3: Iterate Over a String
**Problem:** Write a program that iterates over each character in a string and prints it.

```python
# Sample string
text = "Hello, World!"

# Using for loop to iterate over the string
for char in text:
    print(char)
```

### Exercise 4: Iterate Over a Range
**Problem:** Write a program that iterates over a range of numbers from 1 to 5 and prints each number.

```python
# Using for loop with range
for i in range(1, 6):
    print(i)
```

### Exercise 5: Iterate Over Nested Lists
**Problem:** Write a program that iterates over a list of lists (a matrix) and prints each element.

```python
# Sample nested list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Using for loop to iterate over the nested list
for row in matrix:
    for elem in row:
        print(elem, end=" ")
    print()  # Print a new line after each row
```

### Exercise 6: Iterate Over Multiple Sequences Simultaneously
**Problem:** Write a program that iterates over two lists simultaneously and prints corresponding elements.

```python
# Sample lists
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]

# Using zip to iterate over multiple sequences simultaneously
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

### Exercise 7: Iterate Over a File Line by Line
**Problem:** Write a program that reads a file line by line and prints each line.

```python
# Sample file path (assuming the file is named 'example.txt')
file_path = "example.txt"

# Using for loop to iterate over file lines
with open(file_path, "r") as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character at the end of each line
```

### Exercise 8: Iterate Over a List and Count Elements
**Problem:** Write a program that iterates over a list and counts the number of occurrences of each element.

```python
# Sample list with duplicate elements
elements = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Using for loop to iterate over the list and count elements
element_count = {}
for elem in elements:
    if elem in element_count:
        element_count[elem] += 1
    else:
        element_count[elem] = 1

print(element_count)
```

### Exercise 9: Iterate Over a List of Dictionaries
**Problem:** Write a program that iterates over a list of dictionaries and prints the values for a specific key.

```python
# Sample list of dictionaries
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Using for loop to iterate over the list of dictionaries and print ages
for person in people:
    print(person["age"])
```

### Exercise 10: Iterate Over a Set
**Problem:** Write a program that iterates over a set and prints each element.

```python
# Sample set
numbers = {1, 2, 3, 4, 5}

# Using for loop to iterate over the set
for num in numbers:
    print(num)
```

These exercises should help you practice different types of `for` loops in Python. Feel free to modify and extend them as needed to suit your learning objectives!