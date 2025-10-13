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
# calculates fines in AED, and generates a summary report.

def check_limit(borrowed):
    if borrowed < 0:
        return "Error: Invalid number of books"
    elif borrowed <= 3:
        return "Within limit"
    elif borrowed <= 6:
        return "Over limit: Fine AED 5"
    else:
        return "Over limit: Fine AED 10"


def process_borrowers(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()  # Remove spaces and new line
                if not line:
                    continue  # Skip empty lines

                # Split into name and books
                if ',' in line:
                    parts = line.split(',')
                    if len(parts) < 2:
                        print("Skipping invalid line:", line)
                        continue
                    name = parts[0].strip()
                    books_str = parts[1].strip()
                else:
                    print("Skipping invalid line:", line)
                    continue

                # Convert books to integer
                try:
                    borrowed = int(books_str)
                except ValueError:
                    print("Skipping student due to invalid number of books:", name)
                    continue

                # Check limit and print status
                status = check_limit(borrowed)
                if status == "Error: Invalid number of books":
                    print("Error: Invalid number of books for", name)
                else:
                    print(name, ":", status)

    except FileNotFoundError:
        print("File not found. Please provide a valid file name.")
        return False

    return True


def calculate_average_books(filename):
    total_books = 0
    count = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                if ',' in line:
                    parts = line.split(',')
                    if len(parts) < 2:
                        print("Skipping invalid line:", line)
                        continue
                    name = parts[0].strip()
                    books_str = parts[1].strip()
                else:
                    print("Skipping invalid line:", line)
                    continue

                try:
                    books = int(books_str)
                    if books >= 0:
                        total_books += books
                        count += 1
                except ValueError:
                    print("Skipping student due to invalid number of books:", name)
                    continue

        if count > 0:
            average = total_books / count
            print("Average number of books borrowed:",average)
        else:
            print("No valid data to calculate average.")

    except FileNotFoundError:
        print("File not found. Please provide a valid file name.")


def count_over_limit(filename):
    count = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                if ',' in line:
                    parts = line.split(',')
                    if len(parts) < 2:
                        continue
                    name = parts[0].strip()
                    books_str = parts[1].strip()
                else:
                    continue

                try:
                    books = int(books_str)
                    if books > 3:
                        count += 1
                except ValueError:
                    continue

        print("Number of students over the limit:", count)

    except FileNotFoundError:
        print("File not found. Please provide a valid file name.")


def main():
    while True:
        filename = input("Enter the CSV filename (e.g., borrowers.csv): ").strip()
        if process_borrowers(filename):
            break
        print("Please try again.\n")

    calculate_average_books(filename)
    count_over_limit(filename)
main()
