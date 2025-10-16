"""
GCIS123: Software Development & Problem Solving I
Assignment 2 Library Book Borrowing System
Group Members:
1. Karim Nsouli  [Student ID]
2. Varsha Jayakrishnan  [Student ID]
3. Nithin Julius Ceaser Ananthi [UID 426000109]

Manifesto:
- Karim Nsouli: Implemented check_limit() and process_borrowers()
- Varsha Jayakrishnan: Implemented calculate_average_books()
- Nithin Julius Ceaser Ananthi: Implemented count_over_limit() and main()
All members tested and debugged the program together.
"""

# Library Book Borrowing System
# This program processes a CSV file containing student names and
# the number of books they borrowed. It checks borrowing limits,
# calculates fines in USD, and generates a summary report.

def check_limit(borrowed):
    # borrowed: integer number of books borrowed by a student
    if borrowed < 0:
        # Negative values are invalid
        return "Error: Invalid number of books"
    elif borrowed <= 3:
        # 0-3 books is within the allowed limit
        return "Within limit"
    elif borrowed <= 6:
        # 4-6 books exceed limit and incur a $5 fine
        return "Over limit: Fine $5"
    else:
        # 7 or more books exceed limit and incur a $10 fine
        return "Over limit: Fine $10"


def process_borrowers(filename):
    # Open the provided filename and print status for each borrower
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace and newline
                if not line:
                    # Skip empty lines in the file
                    continue

                # Expect lines in "name,books" CSV format
                if ',' in line:
                    parts = line.split(',')  # Split into name and books parts
                    if len(parts) < 2:
                        # If split doesn't yield at least two parts, skip the line
                        print("Skipping invalid line:", line)
                        continue
                    name = parts[0].strip()      # Student name (trim whitespace)
                    books_str = parts[1].strip() # Books borrowed as string (trim whitespace)
                else:
                    # If no comma present, the line format is invalid
                    print("Skipping invalid line:", line)
                    continue

                # Convert the books string to integer, handling non-numeric values
                try:
                    borrowed = int(books_str)
                except ValueError:
                    # Notify user about non-numeric book counts and skip this entry
                    print("Error: Non-numeric value for", name)
                    continue

                # Use check_limit to determine status/fine for this borrower
                status = check_limit(borrowed)
                if status == "Error: Invalid number of books":
                    # Handle negative book counts explicitly
                    print("Error: Invalid number of books for", name)
                    continue
                else:
                    # Print the borrower's name and their status
                    print(name, ":", status)
    except FileNotFoundError:
        # Inform the user if the file cannot be found and return False to retry
        print("File not found. Please provide a valid file name.")
        return False

    # Return True to indicate the file was processed successfully
    return True


def calculate_average_books(filename):
    # Compute and print the average number of books borrowed (ignoring invalid lines)
    total_books = 0  # Sum of valid book counts
    count = 0        # Number of valid entries counted

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()  #Remove whitespace/newline
                if not line:
                    # Skip empty lines
                    continue

                if ',' in line:
                    parts = line.split(',')  # Split into name and books
                    if len(parts) < 2:
                        # Skip malformed lines with insufficient parts
                        continue
                    name = parts[0].strip()      # Not used here but parsed for clarity
                    books_str = parts[1].strip() # Books as string
                else:
                    # Skip lines without CSV comma
                    continue

                try:
                    books = int(books_str)  # Convert to integer
                    if books >= 0:
                        # Only include non-negative book counts
                        total_books += books
                        count += 1
                except ValueError:
                    # Ignore non-numeric book counts
                    continue

        if count > 0:
            average = total_books / count  # Compute average as float
            print("Average number of books borrowed:", round(average,2))
        else:
            # No valid numeric entries found
            print("No valid data to calculate average.")

    except FileNotFoundError:
        # Inform user if the file is missing
        print("File not found. Please provide a valid file name.")


def count_over_limit(filename):
    # Count and print the number of students who borrowed more than the allowed limit (3)
    count = 0  # Counter for students over the limit

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()  # Remove whitespace/newline
                if not line:
                    # Skip blank lines
                    continue

                if ',' in line:
                    parts = line.split(',')  # Split CSV line
                    if len(parts) < 2:
                        continue
                    name = parts[0].strip()      # Student name
                    books_str = parts[1].strip() # Books borrowed as string
                else:
                    # Skip lines that are not CSV formatted
                    continue

                try:
                    books = int(books_str)  # Convert to integer
                    if books > 3:
                        # Increment counter for anyone over the 3-book limit
                        count += 1
                except ValueError:
                    # Ignore non-numeric entries
                    continue

        # Print the total number of students who exceeded the limit
        print("Number of students over the limit:", count)

    except FileNotFoundError:
        # Notify if file cannot be opened
        print("File not found. Please provide a valid file name.")


def main():
    # Prompt the user repeatedly for a filename until process_borrowers succeeds
    while True:
        filename = input("Enter the CSV filename: ").strip()
        if process_borrowers(filename):
            # Exit loop when processing succeeds
            break
        # Ask user to try again after a failed attempt
        print("Please try again.\n")

    calculate_average_books(filename)
    count_over_limit(filename)
main()