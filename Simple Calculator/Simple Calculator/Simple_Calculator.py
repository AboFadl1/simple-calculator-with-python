# Simple Calculator Program with History Feature

# A list to store calculation history
history = []

# -------------------- Functions --------------------

# Add Function
def add(n1, n2, result):
    # Add two numbers
    result = n1 + n2
    print(f"Result = {result}")  # Display result
    return result  # Return result to main loop

# Subtract Function
def subtract(n1, n2, result):
    # Subtract second number from first
    result = n1 - n2
    print(f"Result = {result}")
    return result

# Multiply Function
def multiply(n1, n2, result):
    # Multiply two numbers
    result = n1 * n2
    print(f"Result = {result}")
    return result

# Division Function
def division(n1, n2, result):
    # Perform division if denominator is not zero
    if n2 != 0:
        result = n1 / n2
        print(f"Result = {result}")
        return result
    else:
        print("Syntax Error")  # Handle division by zero

# -------------------- Main Loop --------------------
while True:
    result = 0  # Store operation result
    r = ""      # Special result for error cases
    
    # Display available operations
    operations = """
    1. Add
    2. Subtract
    3. Multiply
    4. Division
    5. Show History
    6. Exit
    """
    print(operations)
    
    # Get user operation choice
    op = int(input("Please Enter Your Operation Number: "))
    
    # ----- Operation 1: Addition -----
    if op == 1:
        n1 = int(input("Please Enter The First Number: "))
        n2 = int(input("Please Enter The Second Number: "))
        result = add(n1, n2, result)  # Call add function
        operation_name = "Add"

    # ----- Operation 2: Subtraction -----
    elif op == 2:
        n1 = int(input("Please Enter The First Number: "))
        n2 = int(input("Please Enter The Second Number: "))
        result = subtract(n1, n2, result)
        operation_name = "Subtract"

    # ----- Operation 3: Multiplication -----
    elif op == 3:
        n1 = int(input("Please Enter The First Number: "))
        n2 = int(input("Please Enter The Second Number: "))
        result = multiply(n1, n2, result)
        operation_name = "Multiply"

    # ----- Operation 4: Division -----
    elif op == 4:
        n1 = int(input("Please Enter The First Number: "))
        n2 = int(input("Please Enter The Second Number: "))
        result = division(n1, n2, result)
        operation_name = "Division"
        # Check division by zero error
        if n2 == 0:
            r = "Syntax Error"

    # ----- Operation 5: Show History -----
    elif op == 5:
        if history != []:
            print("\n==== Calculation History ====")
            for record in history:
                print(record)  # Display each history record
            print("=============================\n")
            continue  # Go back to main menu
        else:
            print("History Is Empty")
            continue

    # ----- Operation 6: Exit -----
    elif op == 6:
        print("Exiting the calculator...")
        break

    # ----- Invalid choice -----
    else:
        print("Invalid choice! Please select From 1–6.")
        continue

    # ----- Store result in history -----
    if r != "":
        # Store error case in history
        history.append(
            f"---------------------\n"
            f"Operation: {operation_name}\n"
            f"Number 1: {n1}\n"
            f"Number 2: {n2}\n"
            f"Result: {r}\n"
            f"---------------------"
        )
    else:
        # Store normal calculation result in history
        history.append(
            f"---------------------\n"
            f"Operation: {operation_name}\n"
            f"Number 1: {n1}\n"
            f"Number 2: {n2}\n"
            f"Result: {result}\n"
            f"---------------------"
        )
