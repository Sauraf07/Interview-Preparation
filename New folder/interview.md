# 🚀 Wangoes Technologies — Complete Interview Preparation Guide
### AI/ML Developer Fresher | Saurav | DAVV University, Indore

---

## 📋 Table of Contents

1. [Round 1 — Python Coding Questions](#round-1--python-coding-questions)
2. [Round 2 — OOP Questions](#round-2--oop-questions)
3. [Round 3 — SQL Questions](#round-3--sql-questions)
4. [Round 4 — DSA Questions](#round-4--dsa-questions)
5. [Round 5 — Real Interview-Level Concepts](#round-5--real-interview-level-concepts)
6. [Round 6 — ML/AI Concepts](#round-6--mlai-concepts)
7. [Round 7 — FastAPI Questions](#round-7--fastapi-questions)
8. [Round 8 — Aptitude Questions](#round-8--aptitude-questions)
9. [Last-Minute Revision Cheat Sheet](#last-minute-revision-cheat-sheet)

---

## Round 1 — Python Coding Questions

### Problem 1: Find Duplicate Elements

**Question:** Given a list of integers, find all duplicates.

```python
# Input
nums = [1, 2, 3, 4, 2, 5, 6, 1]

# Output → [1, 2]

seen = set()
duplicate = set()

for num in nums:
    if num in seen:
        duplicate.add(num)
    else:
        seen.add(num)

print(list(duplicate))
# Output: [1, 2]
```

**Concept:** Using two sets — one for seen elements, one for duplicates. Time complexity: O(n).

---

### Problem 2: Reverse Words in a Sentence

**Question:** Reverse the order of words in a string.

```python
# Input
s = "hello world python"

# Output → "python world hello"

result = " ".join(s.split()[::-1])
print(result)
# Output: "python world hello"
```

**Concept:** `split()` breaks string into list, `[::-1]` reverses list, `join()` combines back.

---

### Problem 3: Count Character Frequency

**Question:** Count how many times each character appears in a string.

```python
s = "programming"

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

# Shortcut using Counter (also acceptable)
from collections import Counter
print(dict(Counter(s)))
```

---

### Problem 4: Second Largest Number

**Question:** Find the second largest number in a list without sorting.

```python
arr = [10, 20, 5, 40, 30]

# Output → 30

first = second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print(second)
# Output: 30

# Alternative using sorted (simpler but less optimal)
arr_sorted = sorted(set(arr), reverse=True)
print(arr_sorted[1])  # Output: 30
```

**Time Complexity:** O(n) — single pass, no sorting needed.

---

### Problem 5: Check Anagram

**Question:** Check if two strings are anagrams of each other.

```python
s1 = "listen"
s2 = "silent"

# Method 1: Sorting
print(sorted(s1) == sorted(s2))
# Output: True

# Method 2: Counter (better for interviews)
from collections import Counter
print(Counter(s1) == Counter(s2))
# Output: True
```

**Explanation:** Anagrams have the same characters with same frequency.

---

### Problem 6 (Bonus): Fibonacci Series

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)
# Output: 0 1 1 2 3 5 8 13 21 34
```

---

### Problem 7 (Bonus): Palindrome String Check

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("racecar"))   # True
print(is_palindrome("hello"))     # False
print(is_palindrome("A man a plan a canal Panama"))  # True
```

---

## Round 2 — OOP Questions

### Problem 1: BankAccount Class

```python
class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private attribute (encapsulation)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining: ₹{self.__balance}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        return self.__balance

# Usage
acc = BankAccount("Saurav", 1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.check_balance())
```

---

### Problem 2: Inheritance and Method Overriding

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a generic animal sound")

    def __str__(self):
        return f"Animal: {self.name}"


class Dog(Animal):
    def sound(self):               # Method overriding
        print(f"{self.name} says: Bark!")


class Cat(Animal):
    def sound(self):               # Method overriding
        print(f"{self.name} says: Meow!")


# Polymorphism in action
animals = [Dog("Rex"), Cat("Whiskers"), Animal("Unknown")]
for animal in animals:
    animal.sound()
```

---

### Problem 3: Four Pillars of OOP — Explained with Code

```python
# ─── 1. ENCAPSULATION ───────────────────────────────────
# Wrapping data and methods together; hiding internal state

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks       # private variable

    def get_marks(self):           # controlled access
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks

s = Student("Saurav", 85)
print(s.get_marks())               # 85
# print(s.__marks)  → Error! Cannot access directly


# ─── 2. ABSTRACTION ─────────────────────────────────────
# Hiding implementation details, showing only what is needed

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())                    # 78.5


# ─── 3. INHERITANCE ─────────────────────────────────────
# Child class inherits properties of parent class

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started")

class Car(Vehicle):
    def honk(self):
        print(f"{self.brand} car: Beep beep!")

my_car = Car("Toyota")
my_car.start()                     # inherited from Vehicle
my_car.honk()                      # Car's own method


# ─── 4. POLYMORPHISM ────────────────────────────────────
# Same method name, different behaviour depending on object

class Bird:
    def fly(self):
        print("Bird is flying")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly!")

class Eagle(Bird):
    def fly(self):
        print("Eagle soaring high!")

for bird in [Bird(), Penguin(), Eagle()]:
    bird.fly()
```

---

## Round 3 — SQL Questions

### Q1: Second Highest Salary

```sql
-- Method 1: Subquery (classic approach)
SELECT MAX(salary) AS second_highest
FROM employee
WHERE salary < (SELECT MAX(salary) FROM employee);

-- Method 2: DENSE_RANK (modern, preferred)
SELECT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employee
) ranked
WHERE rnk = 2;

-- Method 3: LIMIT OFFSET
SELECT DISTINCT salary
FROM employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

---

### Q2: Find Duplicate Emails

```sql
SELECT email, COUNT(*) AS count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

---

### Q3: Departments with More Than 5 Employees

```sql
SELECT department_id, COUNT(*) AS total_employees
FROM employee
GROUP BY department_id
HAVING COUNT(*) > 5
ORDER BY total_employees DESC;
```

---

### Q4: Highest Salary per Department

```sql
SELECT department_id, MAX(salary) AS highest_salary
FROM employee
GROUP BY department_id;

-- With department name (using JOIN)
SELECT d.dept_name, MAX(e.salary) AS highest_salary
FROM employee e
INNER JOIN departments d ON e.department_id = d.id
GROUP BY d.dept_name;
```

---

### Q5: Top 3 Salaries

```sql
-- DISTINCT avoids duplicates
SELECT DISTINCT salary
FROM employee
ORDER BY salary DESC
LIMIT 3;

-- Using DENSE_RANK
SELECT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employee
) ranked
WHERE rnk <= 3;
```

---

### Q6: All Types of JOINs

```sql
-- INNER JOIN: only matching rows from both tables
SELECT e.name, d.dept_name
FROM employee e
INNER JOIN departments d ON e.dept_id = d.id;

-- LEFT JOIN: all rows from left + matched from right
SELECT e.name, d.dept_name
FROM employee e
LEFT JOIN departments d ON e.dept_id = d.id;

-- RIGHT JOIN: all rows from right + matched from left
SELECT e.name, d.dept_name
FROM employee e
RIGHT JOIN departments d ON e.dept_id = d.id;

-- SELF JOIN: compare rows within same table
SELECT a.name AS employee, b.name AS manager
FROM employee a
JOIN employee b ON a.manager_id = b.id;
```

---

### Q7: Window Functions

```sql
-- DENSE_RANK: no gaps in ranking (use for salary ranking)
SELECT name, salary,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employee;

-- RANK: has gaps (1, 1, 3 — not 1, 1, 2)
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employee;

-- ROW_NUMBER: unique number for every row
SELECT name, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employee;

-- Partition by department
SELECT name, department_id, salary,
       DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dept_rank
FROM employee;
```

---

## Round 4 — DSA Questions

### Problem 1: Two Sum

```python
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]  (nums[0] + nums[1] = 2 + 7 = 9)

def two_sum(nums, target):
    lookup = {}                        # value → index

    for i, num in enumerate(nums):
        diff = target - num
        if diff in lookup:
            return [lookup[diff], i]
        lookup[num] = i

    return []

print(two_sum([2, 7, 11, 15], 9))     # [0, 1]
print(two_sum([3, 2, 4], 6))          # [1, 2]
```

**Time Complexity:** O(n) | **Space Complexity:** O(n)

---

### Problem 2: Palindrome Number

```python
def is_palindrome(num):
    return str(num) == str(num)[::-1]

print(is_palindrome(121))    # True
print(is_palindrome(-121))   # False
print(is_palindrome(10))     # False

# Without converting to string (follow-up question)
def is_palindrome_math(num):
    if num < 0:
        return False
    original = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return original == reversed_num
```

---

### Problem 3: Remove Duplicates

```python
arr = [1, 1, 2, 2, 3, 4]

# Method 1: set (order NOT preserved)
print(list(set(arr)))
# Output: [1, 2, 3, 4]

# Method 2: Without set (order preserved) — interviewer may ask this!
def remove_duplicates(arr):
    seen = []
    for item in arr:
        if item not in seen:
            seen.append(item)
    return seen

print(remove_duplicates(arr))
# Output: [1, 2, 3, 4]

# Method 3: dict.fromkeys (preserves order, Pythonic)
print(list(dict.fromkeys(arr)))
```

---

### Problem 4: FizzBuzz

```python
# Classic
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# One-liner version (shows Python skill)
result = ["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, 101)]
print("\n".join(result))
```

---

### Problem 5: Missing Number

```python
# Input: [1, 2, 3, 5]
# Output: 4

arr = [1, 2, 3, 5]

n = len(arr) + 1
expected_sum = n * (n + 1) // 2   # formula: sum of 1 to n
actual_sum = sum(arr)

print(expected_sum - actual_sum)  # 4

# Alternative using XOR (advanced follow-up)
def missing_xor(arr, n):
    result = 0
    for i in range(1, n + 1):
        result ^= i
    for num in arr:
        result ^= num
    return result
```

---

### Problem 6 (Bonus): Binary Search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 7))   # 3 (index)
print(binary_search(arr, 6))   # -1 (not found)
```

**Time Complexity:** O(log n)

---

### Problem 7 (Bonus): Stack using List

```python
stack = []

stack.append(1)    # push
stack.append(2)
stack.append(3)
print(stack.pop()) # pop → 3  (LIFO: Last In First Out)
print(stack[-1])   # peek → 2 (view top without removing)
print(len(stack))  # size → 2
```

---

## Round 5 — Real Interview-Level Concepts

### Q1: List vs Tuple vs Set vs Dictionary

```python
# LIST — ordered, mutable, allows duplicates
my_list = [1, 2, 3, 2]
my_list.append(4)
my_list[0] = 10

# TUPLE — ordered, immutable, allows duplicates, faster than list
my_tuple = (1, 2, 3, 2)
# my_tuple[0] = 10  → TypeError!

# SET — unordered, mutable, NO duplicates
my_set = {1, 2, 3, 2}
print(my_set)  # {1, 2, 3}

# DICTIONARY — key-value pairs, ordered (Python 3.7+), mutable
my_dict = {"name": "Saurav", "age": 21}
print(my_dict["name"])  # Saurav
```

| Feature   | List  | Tuple | Set   | Dict       |
|-----------|-------|-------|-------|------------|
| Ordered   | Yes   | Yes   | No    | Yes (3.7+) |
| Mutable   | Yes   | No    | Yes   | Yes        |
| Duplicates| Yes   | Yes   | No    | Keys: No   |
| Syntax    | `[]`  | `()`  | `{}`  | `{k:v}`    |

---

### Q2: `is` vs `==`

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # True  — same value
print(a is b)    # False — different objects in memory
print(a is c)    # True  — same object (c points to a)

print(id(a))     # memory address of a
print(id(b))     # different address
print(id(c))     # same as a
```

**Rule:** `==` compares values. `is` compares object identity (memory address).

---

### Q3: Generator and `yield`

```python
# Regular function — stores all values in memory
def get_numbers(n):
    return [i for i in range(n)]

# Generator — produces values one at a time (memory efficient)
def get_numbers_gen(n):
    for i in range(n):
        yield i              # pauses here, resumes on next call

gen = get_numbers_gen(5)
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

# Or iterate directly
for num in get_numbers_gen(5):
    print(num)

# Use case: reading large files line by line
def read_large_file(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()
```

---

### Q4: Decorators

```python
# A decorator wraps a function to add behaviour

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Saurav")
# Output:
# Before function call
# Hello, Saurav!
# After function call

# Real-world example: timing a function
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Executed in {time.time() - start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()
```

---

### Q5: Lambda Function

```python
# Syntax: lambda arguments: expression

square = lambda x: x * x
print(square(5))   # 25

add = lambda x, y: x + y
print(add(3, 4))   # 7

# Common use: sorting with key
students = [("Saurav", 85), ("Rahul", 92), ("Ankit", 78)]
students.sort(key=lambda s: s[1], reverse=True)
print(students)    # sorted by marks descending

# With map and filter
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(squares)     # [1, 4, 9, 16, 25]
print(evens)       # [2, 4]
```

---

### Q6: `append()` vs `extend()`

```python
a = [1, 2, 3]
b = [1, 2, 3]

a.append([4, 5])      # adds as single element (nested list)
print(a)              # [1, 2, 3, [4, 5]]

b.extend([4, 5])      # adds each element individually
print(b)              # [1, 2, 3, 4, 5]
```

---

### Q7: Deep Copy vs Shallow Copy

```python
import copy

original = [[1, 2], [3, 4]]

# Shallow copy — nested objects still share reference
shallow = copy.copy(original)
shallow[0][0] = 99
print(original)    # [[99, 2], [3, 4]]  ← CHANGED!

original = [[1, 2], [3, 4]]

# Deep copy — completely independent copy
deep = copy.deepcopy(original)
deep[0][0] = 99
print(original)    # [[1, 2], [3, 4]]  ← NOT changed
```

---

### Q8: Time Complexity — Big O

```python
# O(1) — Constant: same time regardless of input size
def get_first(lst):
    return lst[0]

# O(log n) — Logarithmic: binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1

# O(n) — Linear: single loop
def find_max(lst):
    return max(lst)

# O(n log n) — Linearithmic: efficient sorting
sorted_list = sorted([3, 1, 4, 1, 5])

# O(n²) — Quadratic: nested loops
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

| Complexity | Name          | Example              |
|------------|---------------|----------------------|
| O(1)       | Constant      | dict lookup, indexing|
| O(log n)   | Logarithmic   | binary search        |
| O(n)       | Linear        | single loop          |
| O(n log n) | Linearithmic  | merge sort, timsort  |
| O(n²)      | Quadratic     | bubble sort, nested  |

---

### Q9: Exception Handling

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)

except ValueError:
    print("Invalid input — not a number!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    print("This always runs — cleanup code here")

# Custom exception
class InsufficientBalanceError(Exception):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Insufficient balance! Need ₹{amount} more")

# raise InsufficientBalanceError(500)
```

---

### Q10: `*args` and `**kwargs`

```python
# *args — variable number of positional arguments (tuple)
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3))         # 6
print(add_all(1, 2, 3, 4, 5))   # 15

# **kwargs — variable number of keyword arguments (dict)
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Saurav", age=21, college="DAVV")

# Combined
def full_function(required, *args, **kwargs):
    print(f"Required: {required}")
    print(f"Extra args: {args}")
    print(f"Keyword args: {kwargs}")

full_function("hello", 1, 2, 3, name="Saurav", city="Indore")
```

---

## Round 6 — ML/AI Concepts

### Q1: What is Machine Learning?

```
Machine Learning is a subset of AI where systems learn from data
to make predictions or decisions without being explicitly programmed.

Types:
├── Supervised Learning   → labelled data (spam detection, price prediction)
├── Unsupervised Learning → no labels (clustering, anomaly detection)
├── Semi-supervised       → some labels
└── Reinforcement Learning → reward/punishment based (games, robots)
```

### Q2: Train a Model with Scikit-learn

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load data
data = load_iris()
X, y = data.data, data.target

# 2. Split: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 4. Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nReport:\n", classification_report(y_test, y_pred))
```

### Q3: Pandas — Data Preprocessing

```python
import pandas as pd
import numpy as np

# Create sample DataFrame
df = pd.DataFrame({
    'name':   ['Saurav', 'Rahul', None, 'Ankit'],
    'age':    [21, 22, 23, None],
    'marks':  [85, 92, 78, 88]
})

# Check missing values
print(df.isnull().sum())

# Fill missing values
df['age'].fillna(df['age'].mean(), inplace=True)
df['name'].fillna('Unknown', inplace=True)

# Drop rows (if needed)
df.dropna(inplace=True)

# Basic stats
print(df.describe())

# Filter rows
high_scorers = df[df['marks'] > 80]

# Group by
# df.groupby('dept')['marks'].mean()

# Add new column
df['grade'] = df['marks'].apply(lambda x: 'A' if x >= 85 else 'B')

print(df)
```

### Q4: Key ML Metrics

```python
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_squared_error,
    r2_score
)

# Classification metrics
# Accuracy  = (TP + TN) / Total
# Precision = TP / (TP + FP)  — how many predicted positives are actually positive
# Recall    = TP / (TP + FN)  — how many actual positives were caught
# F1 Score  = 2 * (Precision * Recall) / (Precision + Recall)

# Regression metrics
# MSE  = Mean Squared Error (lower = better)
# RMSE = sqrt(MSE)
# R²   = 1 means perfect fit, 0 means as good as mean baseline
```

---

## Round 7 — FastAPI Questions

### What is FastAPI?

```
FastAPI is a modern, fast Python web framework for building REST APIs.
- Based on Python type hints
- Automatic documentation (Swagger UI at /docs)
- Async support (very fast)
- Uses Pydantic for data validation
```

### Basic FastAPI App

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Pydantic model for request body validation
class Student(BaseModel):
    name: str
    age: int
    marks: Optional[float] = None

# In-memory database
students_db = {}

# GET — read data
@app.get("/")
def root():
    return {"message": "Welcome to Wangoes API"}

@app.get("/students")
def get_all_students():
    return students_db

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    return students_db[student_id]

# POST — create data
@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student):
    students_db[student_id] = student
    return {"message": "Created", "student": student}

# PUT — update data
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    students_db[student_id] = student
    return {"message": "Updated"}

# DELETE — remove data
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Not found")
    del students_db[student_id]
    return {"message": "Deleted"}
```

### Key FastAPI Interview Questions

```
Q: What is Pydantic?
A: A data validation library. FastAPI uses it to validate request/response data
   using Python type hints. If wrong data type is sent, it auto-rejects with error.

Q: What is async in FastAPI?
A: async/await allows non-blocking I/O. While waiting for DB or API response,
   server handles other requests — making it very fast.

Q: Difference between GET and POST?
A: GET retrieves data (no body, data in URL params)
   POST sends data to create/process something (body contains data)

Q: What is a REST API?
A: An architectural style using HTTP methods (GET, POST, PUT, DELETE)
   with stateless requests and JSON responses.

Q: What is HTTP status code?
A: 200 OK | 201 Created | 400 Bad Request | 401 Unauthorized
   403 Forbidden | 404 Not Found | 500 Internal Server Error
```

---

## Round 8 — Aptitude Questions

### Section A: Number Problems

**Q1. If a train travels 360 km in 4 hours, what is its speed in m/s?**

```
Speed = 360 / 4 = 90 km/h
Convert to m/s: 90 × (1000/3600) = 90 × 5/18 = 25 m/s
Answer: 25 m/s
```

**Q2. A can do a work in 12 days, B in 18 days. Together?**

```
A's 1 day work = 1/12
B's 1 day work = 1/18
Combined = 1/12 + 1/18 = 3/36 + 2/36 = 5/36
Together they finish in 36/5 = 7.2 days
Answer: 7 days 4 hours 48 minutes
```

**Q3. Simple Interest: Principal ₹5000, Rate 8%, Time 3 years**

```
SI = (P × R × T) / 100
SI = (5000 × 8 × 3) / 100 = 1200
Amount = 5000 + 1200 = ₹6200
```

**Q4. Compound Interest: ₹10000 at 10% for 2 years**

```
A = P × (1 + R/100)^T
A = 10000 × (1.1)² = 10000 × 1.21 = ₹12100
CI = 12100 - 10000 = ₹2100
```

**Q5. A shopkeeper sells at 20% profit. Cost is ₹500. Selling price?**

```
SP = CP × (1 + Profit%) / 100
SP = 500 × (120/100) = ₹600
```

**Q6. If 40% of a number is 200, what is the number?**

```
40% of x = 200
x = 200 / 0.40 = 500
Answer: 500
```

**Q7. Ratio and Proportion — Salary split in 3:4:5**

```
Total salary = ₹36,000
Parts = 3 + 4 + 5 = 12
Person A = (3/12) × 36000 = ₹9,000
Person B = (4/12) × 36000 = ₹12,000
Person C = (5/12) × 36000 = ₹15,000
```

**Q8. Speed, Distance, Time — Relative speed**

```
Two trains: 60 km/h and 40 km/h, same direction
Relative speed = 60 - 40 = 20 km/h
To cross a platform: use (Length of train + Length of platform) / Speed
```

### Section B: Logical Reasoning

**Q9. Pattern Series: 2, 6, 18, 54, ?**

```
Pattern: each term × 3
54 × 3 = 162
Answer: 162
```

**Q10. Series: 1, 4, 9, 16, 25, ?**

```
Pattern: perfect squares (1², 2², 3², 4², 5²...)
Next: 6² = 36
Answer: 36
```

**Q11. Number series: 3, 8, 15, 24, 35, ?**

```
Differences: 5, 7, 9, 11, 13...
Next difference = 13
35 + 13 = 48
Answer: 48
```

**Q12. Coding-Decoding: If PYTHON = QZUIPO, what is JAVA?**

```
Each letter shifted by +1
J→K, A→B, V→W, A→B
Answer: KBWB
```

### Section C: Python Aptitude-Style Problems

**Q13. What is the output?**

```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)
# Answer: [1, 2, 3, 4]
# Reason: y is not a copy, it points to same list as x
```

**Q14. What is the output?**

```python
print(type(1/2))
print(type(1//2))
# Answer:
# <class 'float'>   — division always returns float
# <class 'int'>     — floor division returns int
```

**Q15. What is the output?**

```python
def func(a, b=[]):
    b.append(a)
    return b

print(func(1))
print(func(2))
print(func(3))
# Answer: [1], [1, 2], [1, 2, 3]
# Reason: Default mutable argument is shared across calls (common Python gotcha!)
```

**Q16. What is the output?**

```python
x = 5
def change():
    x = 10      # local variable, not global x
change()
print(x)
# Answer: 5
# Reason: x inside function is local, global x unchanged
```

**Q17. List comprehension output?**

```python
result = [x**2 for x in range(5) if x % 2 == 0]
print(result)
# Answer: [0, 4, 16]
# Even numbers from 0–4 are: 0, 2, 4 → squared: 0, 4, 16
```

---

## Last-Minute Revision Cheat Sheet

### ⚡ Python Quick Reference

```python
# List comprehension
squares = [x**2 for x in range(10)]

# Dictionary comprehension
freq = {ch: s.count(ch) for ch in set(s)}

# Enumerate
for i, val in enumerate(my_list):
    print(i, val)

# Zip
for a, b in zip(list1, list2):
    print(a, b)

# String methods
s.upper() | s.lower() | s.strip() | s.split() | s.replace()

# List methods
lst.append() | lst.extend() | lst.pop() | lst.sort() | lst.reverse()
```

### ⚡ SQL Quick Reference

```sql
SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT

-- Order of execution (important!)
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

### ⚡ ML Algorithms — Quick Summary

| Algorithm | Type | Use Case |
|-----------|------|----------|
| Linear Regression | Supervised | Predict continuous value (price) |
| Logistic Regression | Supervised | Binary classification (yes/no) |
| Decision Tree | Supervised | Both classification & regression |
| Random Forest | Supervised | Better accuracy, handles noise |
| KMeans | Unsupervised | Customer segmentation |
| KNN | Supervised | Recommendation, classification |
| SVM | Supervised | Image classification |
| Naive Bayes | Supervised | Spam detection, NLP |

### ⚡ 30-Minute Power Revision Order

```
1. Python OOP (10 min)   → class, __init__, inheritance, @property
2. ML concepts (8 min)   → supervised, overfitting, confusion matrix
3. SQL joins (7 min)     → INNER, LEFT, GROUP BY + HAVING
4. DSA patterns (5 min)  → two pointers, hashmap, sliding window
```

---

## 🎯 Your Introduction Template

> "My name is Saurav, I'm a BCA final year student at DAVV University, Indore. I've completed an IBM SkillsBuild AI Strategy & Business Intelligence internship, which gave me hands-on exposure to real AI use cases. I run a YouTube channel called 'Saurav Education' where I teach DBMS, Java, and Web Design — which has sharpened my communication and teaching ability.
>
> I'm passionate about AI/ML and have been building projects in Python. I'm excited about Wangoes Technologies specifically because you build deployed, real-world AI solutions — not just prototypes. I want to grow through your 3-phase structure and become a strong AI developer."

---

*Prepared for Wangoes Technologies AI/ML Developer Fresher Interview*
*Best of luck, Saurav! 🚀*