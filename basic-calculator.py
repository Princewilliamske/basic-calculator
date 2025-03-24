def calculate(num1, num2, operation):
    
    # Perform mathematical operations based on user input.
    
    # Args:
    #     num1 (float): First number
    #     num2 (float): Second number
    #     operation (str): Mathematical operation (+, -, *, /)
    
    # Returns:
    #     float: Result of the calculation
    
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

def main():
    try:
        # Get user inputs
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform calculation
        result = calculate(num1, num2, operation)

        # Display result
        print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        print("Error: Please enter valid numbers")

# Run the calculator
if __name__ == "__main__":
    main()