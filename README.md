# Bus-Ticket-Booking-System
🚌 Bus Booking System

🎯Project Overview
This is a simple command-line Bus Booking System implemented in Python. It allows users to register buses, delete buses, view all buses, make seat reservations, view reservations, and cancel reservations. The system uses CSV files (`buses.csv` and `reservations.csv`) to store bus and reservation data persistently.

✨ Features
-	Register a new bus with ID, route description, and seat capacity
-	Delete an existing bus by ID
-	List all registered buses
-	Make seat reservations for a bus if seats are available
-	View all reservations
-	Cancel a reservation with  reservation ID

🛠️Technologies and Tools Used
-	Python 3
-	CSV file handling (‘csv’ module)
-	Basic file operations (‘os’ module)

 💻Installation and Running the Project
-	Ensure you have Python 3 installed on your system.
-	Download the project files and place them in a directory.
Run the main program:
-	Follow the on-screen menu options to use the system.

📖 Usage Instructions
-	Upon running, a menu with options 1 to 7 will appear.
-	Enter the number corresponding to the desired action.
-	For registering a bus, provide bus ID, route, and seat capacity.
-	For reservations, input customer name, bus ID, and number of seats.
-	You can view existing buses or reservations anytime.
-	To cancel a reservation or delete a bus, provide the relevant ID.
-	Exit the program via option 7.

📝Notes
-	Seat capacity must be a valid number.
-	Reservations cannot exceed available seats on a bus.
-	The system auto-generates reservation IDs sequentially.
-	Data persists in CSV files in the program directory.

📈Optional Enhancements
-	Add input validation and error handling for robustness.
-	Implement a GUI or web interface for better usability.
-	Add search/filter options for buses and reservations.
-	Support for multiple users with authentication.

🧑‍💻Developer
Vardaan Yadav

