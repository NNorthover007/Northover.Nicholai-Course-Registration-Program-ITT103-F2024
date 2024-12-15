Nicholai Northover
December 13,2024
ITT103

PURPOSE OF THE PROGRAM

The purpose of the program is to simplify & navigate the course registrations and payment system with management of student registrations, course enrollments, and payments for educational institutions. 
So by automating these tasks with a menu option, the program reduces errors, enhances transparency, and optimize workflow. 
The system demonstrates the practicality of object-oriented programming principles , modular design, and robust exception handling.

HOW TO RUN IT

Install PyCharm Community Edition 2024.2.3 on your PC.
Save the provided code in a Python file named Northover.Nicholai-Course_Registration-ITT103-F2024.py.
Open/locate a terminal/project file in PyCharm or command prompt and navigate to the directory containing the file.
Run the program with the following command (ALT+4)OR THE RUN tab: Northover.Nicholai-Course_Registration-ITT103-F2024.py
Use the drop down/menu-driven interface to interact with the system.

ASSUMPTIONS AND LIMITATIONS

Assumptions; The program assumes that administrators provide valid inputs for emails, names, and fees.
Partial payments so the students must pay at least 40% of their outstanding balance for payments to be accepted.
It is assumed that course IDs and student IDs are unique strings or numbers entered by the administrator.

Limitations; The program is unable validate email by distinguishing format outside of basic string entry
Date persistence where's no database or dataset or file storage exist so once the program exits the data will be lost.
Concurrencies where the system does not simultaneously handle administrators making changes and this requires a rerun if any modifications is made in the code.
