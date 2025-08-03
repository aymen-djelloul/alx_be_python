from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

# Part 2: Calculate a future date
def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print("Future Date:", formatted_future)
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Main program
def main():
    print("Date and Time Operations with datetime Module")
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
