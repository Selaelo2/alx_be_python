def safe_divide(numerator, denominator):
    try:
        # Try converting the input values to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform the division
        result = num / denom
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
    
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."
