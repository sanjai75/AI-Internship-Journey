# AI Learning Assistant

## Topic 1: Python Functions

### 1. Explain

**Prompt:**
Explain Python Functions in simple terms.

**AI Response:**
A function is a reusable block of code that performs a specific task. Functions help reduce code duplication and make programs easier to manage.

### 2. Example

**Prompt:**
Provide an example of a Python function.

**AI Response:**

```python
def greet(name):
    return "Hello " + name

print(greet("Sanjai"))
```

### 3. Exercise

**Prompt:**
Create an exercise on Python Functions.

**AI Response:**
Create a function that accepts two numbers and returns their sum.

### 4. My Solution

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

### 5. Review

**AI Feedback:**
The solution is correct. The function accepts two parameters and returns their sum.

---

# Topic 2: APIs

### 1. Explain

**Prompt:**
Explain APIs in simple terms.

**AI Response:**
An API allows different applications to communicate and exchange data with each other.

### 2. Example

**Prompt:**
Provide an API example.

**AI Response:**

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response.json())
```

### 3. Exercise

**Prompt:**
Create an API exercise.

**AI Response:**
Fetch data from a public API and print user names.

### 4. My Solution

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

for user in response.json():
    print(user["name"])
```

### 5. Review

**AI Feedback:**
The solution correctly fetches data and displays user names.

---

# Topic 3: JSON

### 1. Explain

**Prompt:**
Explain JSON in simple terms.

**AI Response:**
JSON is a lightweight format used to store and exchange data using key-value pairs.

### 2. Example

**Prompt:**
Provide a JSON example.

**AI Response:**

```json
{
    "name": "Sanjai",
    "role": "AI Intern"
}
```

### 3. Exercise

**Prompt:**
Create a JSON exercise.

**AI Response:**
Create a JSON profile containing name, role, and skills.

### 4. My Solution

```json
{
    "name": "Sanjai",
    "role": "AI Intern",
    "skills": ["Python", "GitHub", "AI"]
}
```

### 5. Review

**AI Feedback:**
The JSON structure is valid and correctly uses key-value pairs and arrays.

---

# Conclusion

This activity helped me learn Python Functions, APIs, and JSON through explanations, examples, exercises, and feedback. The AI acted as a learning assistant and helped me understand concepts interactively.
