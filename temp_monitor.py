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
        if lowest is None or temp < lowest:
            lowest = temp

        if highest is None or temp > highest:
            highest = temp
        
        count += 1

        total += temp
        
    except ValueError:
        print("Please enter a valid number or 'done'!")

# Your code here: show the summary
if count > 0:
    print(f"\nTemperature Summary:")
    print(f"===================")
    print(f"Temperatures recorded: {count}")
    print(f"Highest temperature: {highest}°C")
    print(f"Lowest temperature: {lowest}°C")
    print(f"Average temperature: {total/count:.1f}°C")
else:
    print("No temperatures recorded.")