# Lesson 3: Loops and Input Validation - In-Class Practices

## Practice 1: Student Counter Practice (10 minutes)

### 🎯 **Objective**
Practice basic while loop syntax by creating a countdown program.

### 📋 **Requirements**
Write a program that counts from 10 down to 1, then prints 'Finished!'

### 💻 **Template**
```python
# Count from 10 down to 1
number = 10
while ___:  # Fill in the condition
    print(___)  # Fill in what to print
    ___ = ___ - 1  # Fill in the update
print("Finished!")
```

### 🔍 **Hints**
1. The condition should check if the number is still greater than or equal to 1
2. Print the current number inside the loop
3. Don't forget to subtract 1 from the number each time
4. Test your condition: when should the loop stop?

### ✅ **Example Output**
```
10
9
8
7
6
5
4
3
2
1
Finished!
```

### 🚀 **Challenge Extensions** (Optional)
If you finish early, try:
- Count from 20 down to 1
- Count from 1 up to 10
- Ask the user for starting and ending numbers

### 🔍 **What You're Learning**
- Basic while loop syntax
- Loop conditions that eventually become False
- Updating variables inside loops
- When and why loops stop

---

## Practice 2: Password Validator (20 minutes)

### 🎯 **Objective**
Build a password validation system that keeps asking until the user creates a valid password.

### 📋 **Requirements**
1. Ask user to create a password
2. Password must be at least 8 characters long
3. Password must contain at least one number
4. Keep asking until password meets requirements
5. Print "Password accepted!" when valid
6. Handle the validation gracefully (give helpful error messages)

### 💻 **Template**
```python
print("Password Creator")
print("===============")

while True:
    password = input("Create a password: ")
    
    # Check length
    if len(password) < 8:
        print("Password must be at least 8 characters!")
        continue
    
    # Check for number (you'll need to figure this out!)
    # Hint: Loop through each character and check if it's a digit
    
    # If we get here, password is valid
    print("Password accepted!")
    break
```

### 🔍 **Hints**
1. Use `len(password)` to check the length
2. Use a for loop to check each character: `for char in password:`
3. Check if a character is a digit: `char in '0123456789'` or `char.isdigit()`
4. Use a flag variable (like `has_number = False`) to track if you found a number
5. Use `continue` to restart the loop when validation fails
6. Use `break` to exit the loop when password is valid

### 🔍 **Key Components to Include**
```python
# For checking if password contains a number:
has_number = False
for char in password:
    if char in "0123456789":  # or char.isdigit()
        has_number = True
        break  # Found one, no need to keep looking

if not has_number:
    print("Password must contain at least one number!")
    continue
```

### ✅ **Example Output**
```
Password Creator
===============
Create a password: hello
Password must be at least 8 characters!
Create a password: helloworld
Password must contain at least one number!
Create a password: helloworld123
Password accepted!
```

### 🚀 **Challenge Extensions** (Optional)
If you finish early, try adding these requirements:
- Must contain at least one uppercase letter
- Must contain at least one lowercase letter
- Must contain at least one special character (!@#$%^&*)
- Cannot contain spaces
- Display a strength score (weak/medium/strong)

### 🔍 **What You're Learning**
- While loops with `while True:` pattern
- Using `break` and `continue` for loop control
- String processing and validation
- Combining loops with conditional logic
- Building user-friendly validation systems

---

## Practice 3: Temperature Monitor (20 minutes)

### 🎯 **Objective**
Create a data collection and analysis program that gathers temperatures and provides statistical analysis.

### 📋 **Requirements**
1. Keep asking for temperatures until user enters 'done'
2. Track the highest and lowest temperatures
3. Count how many temperatures were entered
4. Calculate and show average temperature
5. Handle invalid inputs gracefully (try/except)
6. Show a professional summary at the end

### 💻 **Template**
```python
print("Temperature Monitor")
print("==================")

count = 0
total = 0
highest = None
lowest = None

while True:
    user_input = input("Enter temperature (or 'done' to finish): ")
    
    # Check if user wants to finish
    if user_input.lower() == 'done':
        break
    
    # Try to convert to number
    try:
        temp = float(user_input)
        # Your code here: update count, total, find min/max
        
    except ValueError:
        print("Please enter a valid number or 'done'!")

# Your code here: show the summary
```

### 🔍 **Hints**
1. Use `float(user_input)` to convert input to a decimal number
2. For each valid temperature:
   - Increase the count by 1
   - Add the temperature to the total
   - Check if it's higher than current highest (or if this is the first temperature)
   - Check if it's lower than current lowest (or if this is the first temperature)
3. For min/max tracking: if `highest is None`, this is the first temperature
4. Calculate average as `total / count` (but check that count > 0!)
5. Use `.lower()` to handle 'DONE', 'Done', 'done', etc.

### 🔍 **Key Components to Include**
```python
# Inside the try block, after temp = float(user_input):
count = count + 1
total = total + temp

# For tracking highest/lowest:
if highest is None or temp > highest:
    highest = temp
if lowest is None or temp < lowest:
    lowest = temp

# For the summary (after the while loop):
if count > 0:
    print(f"\nTemperature Summary:")
    print(f"===================")
    print(f"Temperatures recorded: {count}")
    print(f"Highest temperature: {highest}°C")
    print(f"Lowest temperature: {lowest}°C")
    print(f"Average temperature: {total/count:.1f}°C")
else:
    print("No temperatures recorded.")
```

### ✅ **Example Output**
```
Temperature Monitor
==================
Enter temperature (or 'done' to finish): 25
Enter temperature (or 'done' to finish): 18
Enter temperature (or 'done' to finish): 30
Enter temperature (or 'done' to finish): abc
Please enter a valid number or 'done'!
Enter temperature (or 'done' to finish): 22
Enter temperature (or 'done' to finish): done

Temperature Summary:
===================
Temperatures recorded: 4
Highest temperature: 30°C
Lowest temperature: 18°C
Average temperature: 23.8°C
```

### 🚀 **Challenge Extensions** (Optional)
If you finish early, try adding:
- Temperature trend analysis (is it getting warmer or cooler?)
- Convert between Celsius and Fahrenheit
- Add reasonable temperature range validation (-50°C to 60°C)
- Count how many temperatures are above/below average
- Find the temperature range (highest - lowest)

### 🔍 **What You're Learning**
- Data collection with loops
- Statistical analysis (min, max, average)
- Error handling with try/except
- Working with None values
- String processing (checking for 'done')
- Handling edge cases (no data entered)
- Professional program output formatting

---

## 🎉 Bonus Challenges

### For Practice 1 (Student Counter):
- Ask user for starting and ending numbers
- Count by 2s, 3s, or other step sizes
- Count up or down automatically based on start/end values
- Add a delay between numbers (like a real countdown timer)

### For Practice 2 (Password Validator):
- Add a password strength meter (weak/medium/strong)
- Show which requirements are missing vs. satisfied
- Generate a random strong password if user requests it
- Keep track of how many attempts it took to create a valid password

### For Practice 3 (Temperature Monitor):
- Save all temperatures to a list and show them at the end
- Calculate median temperature (middle value when sorted)
- Show temperature in both Celsius and Fahrenheit
- Create a simple ASCII chart showing the temperature range
- Add time stamps to each temperature reading

---

## 📚 Key Concepts Review

After completing these practices, you should understand:

### While Loops:
- `while condition:` syntax with proper indentation
- Loop conditions that eventually become False
- Updating variables inside loops to avoid infinite loops
- When and why loops terminate

### Loop Control:
- `break` - exits the loop immediately
- `continue` - skips to the next iteration
- `while True:` pattern for input validation
- How break and continue affect program flow

### Input Validation:
- `try/except` blocks for handling conversion errors
- `ValueError` when converting invalid strings to numbers
- Persistent validation (keep asking until valid)
- Providing helpful error messages to users

### String Processing:
- `len(string)` to get string length
- `for char in string:` to check each character
- `char.isdigit()` or `char in "0123456789"` to check for numbers
- `.lower()` for case-insensitive comparisons

### Data Analysis:
- Tracking count, sum, min, and max values
- Calculating averages from collected data
- Handling the "first value" case with None
- Edge case handling (what if no data entered?)

### Real-World Applications:
- User input validation systems
- Data collection and analysis programs
- Menu-driven applications
- Interactive programs that respond to user needs

### Best Practices:
- Always have a way to exit loops (avoid infinite loops)
- Provide clear, helpful error messages
- Handle edge cases gracefully
- Test with various inputs including invalid ones
- Use meaningful variable names

**Remember**: Loops are one of the most powerful programming concepts. They let you automate repetitive tasks and create interactive programs that respond intelligently to user input. These patterns will be essential in every program you write! 