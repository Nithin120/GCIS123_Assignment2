# GCIS123_Assignment2_Library_Book_Borrowing_System

## Description
This is a **Library Book Borrowing System** developed in Python. The program reads a CSV file containing student names and the number of books they borrowed. It:

- Checks borrowing limits and calculates fines in AED.
- Processes each student’s record and prints their borrowing status.
- Calculates the average number of books borrowed by all students.
- Counts how many students borrowed more than the allowed limit.
- Handles invalid or missing data gracefully, skipping problematic lines.

## Contributors

| Name           | Student ID      | Contribution                                  |
|----------------|----------------|-----------------------------------------------|
| Karim Nsouli   |       | Implemented `check_limit()` and `process_borrowers()` |
| Varsha Jayakrishnan    |           | Implemented `calculate_average_books()`      |
| Nithin Julius Ceaser Ananthi     | 426000109           | Implemented `count_over_limit()` and `main()` |
| All Members    | -              | Tested and debugged the program together     |

## How to Use
1. Make sure you have Python installed on your computer.  
2. Prepare a CSV file with student data in this format:

| Name    | NumberOfBooks |
|---------|---------------|
| Alice   | 2             |
| Bob     | 5             |
| Charlie | abc           |


3. Run the Python program.  
4. When prompted, enter the CSV file name (e.g., `borrowers.csv`).  
5. The program will display:
   - Borrowing status for each student
   - Average number of books borrowed
   - Number of students over the limit
   - Skipped lines or invalid data messages

## File Structure
- `library_borrowing_system.py` – Main Python program  
- `borrowers.csv` – Example CSV file containing student data (you can create your own)  

## Notes
- Empty lines, missing data, or non-numeric book counts are **skipped with a message**.  
- Fines:
  - Up to 3 books → within limit
  - 4–6 books → $5
  - More than 6 books → $10
