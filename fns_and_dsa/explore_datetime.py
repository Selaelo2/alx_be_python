from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_datetime = datetime.now()
    # Format the date and time in a readable format
    current_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    # Prompt the user for the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Get the current date and time
    current_datetime = datetime.now()
    # Calculate the future date by adding the specified number of days
    future_date = current_datetime + timedelta(days=days_to_add)
    # Format the future date in a readable format
    future_date_str = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {future_date_str}")

def main():
    # Display the current date and time
    display_current_datetime()
    
    # Calculate and display the future date
    calculate_future_date()

if __name__ == "__main__":
    main()
