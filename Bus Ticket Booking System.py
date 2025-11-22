import csv
import os
def setup_files():
    """ Ensure necessary CSV files exist with headers. """
    if not os.path.isfile("buses.csv"):
        with open("buses.csv", "w", newline="") as f:
            csv.writer(f).writerow(["bus_id", "route_description", "seat_capacity"])
    if not os.path.isfile("reservations.csv"):
        with open("reservations.csv", "w", newline="") as f:
            csv.writer(f).writerow(["reservation_id", "customer_name", "bus_id", "seats_reserved"])

def register_bus(bus_id, route, seats):
    """Add a new bus record."""
    with open("buses.csv", "a", newline="") as f:
        csv.writer(f).writerow([bus_id, route, seats])
    print(f"Bus '{bus_id}' added successfully!")

def delete_bus(bus_id_to_remove):
    """Delete a bus by its ID."""
    with open("buses.csv", "r", newline="") as f:
        buses = list(csv.DictReader(f))
    new_buses = [bus for bus in buses if bus["bus_id"] != bus_id_to_remove]
    if len(buses) == len(new_buses):
        print(f"No bus found with ID '{bus_id_to_remove}'. Nothing deleted.")
        return
    with open("buses.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["bus_id", "route_description", "seat_capacity"])
        writer.writeheader()
        writer.writerows(new_buses)
    print(f"Bus '{bus_id_to_remove}' was removed.")

def list_buses():
    """List all buses."""
    with open("buses.csv", "r", newline="") as f:
        buses = list(csv.DictReader(f))
    if not buses:
        print("No buses registered yet.")
        return
    for bus in buses:
        print(f"ID: {bus['bus_id']} | Route: {bus['route_description']} | Seats: {bus['seat_capacity']}")

def make_reservation(customer_name, bus_id, seats_requested):
    """Reserve seats if available."""
    with open("buses.csv", "r", newline="") as f:
        buses = list(csv.DictReader(f))
    bus = next((b for b in buses if b["bus_id"] == bus_id), None)
    if not bus:
        print(f"Bus ID '{bus_id}' not found.")
        return
    with open("reservations.csv", "r", newline="") as f:
        reservations = csv.DictReader(f)
        reserved_seats = sum(int(r["seats_reserved"]) for r in reservations if r["bus_id"] == bus_id)
    seats_left = int(bus["seat_capacity"]) - reserved_seats
    if seats_requested > seats_left:
        print(f"Sorry, only {seats_left} seats left on this bus.")
        return
    with open("reservations.csv", "r", newline="") as f:
        count = sum(1 for _ in f) - 1
    reservation_id = count + 1
    with open("reservations.csv", "a", newline="") as f:
        csv.writer(f).writerow([reservation_id, customer_name, bus_id, seats_requested])
    print(f"Reserved {seats_requested} seat(s) on Bus '{bus_id}' for {customer_name}.")

def show_reservations():
    """Display all reservations."""
    with open("reservations.csv", "r", newline="") as f:
        reservations = list(csv.DictReader(f))
    if not reservations:
        print("No reservations found.")
        return
    for r in reservations:
        print(f"Reservation ID: {r['reservation_id']} | Customer: {r['customer_name']} | Bus ID: {r['bus_id']} | Seats: {r['seats_reserved']}")

def cancel_reservation(reservation_id):
    """Cancel a reservation by its ID."""
    with open("reservations.csv", "r", newline="") as f:
        reservations = list(csv.DictReader(f))
    new_reservations = [r for r in reservations if r["reservation_id"] != str(reservation_id)]
    if len(new_reservations) == len(reservations):
        print(f"No reservation found with ID {reservation_id}.")
        return
    with open("reservations.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["reservation_id", "customer_name", "bus_id", "seats_reserved"])
        writer.writeheader()
        writer.writerows(new_reservations)
    print(f"Reservation {reservation_id} cancelled.")

def main():
    setup_files()
    menu = (""" Bus Booking System
    1.Register Bus
    2.Delete Bus
    3.View Buses
    4.Make Reservation
    5.View Reservations
    6.Cancel Reservation
    7.Exit"""
    )
    while True:
        print(menu)
        choice = input("Enter your choice:").strip()
        if choice == "1":
            bus_id = input("Enter Bus ID: ").strip()
            route = input("Enter Route Description: ").strip()
            seats = input("Enter Seat Capacity: ").strip()
            if seats.isdigit():
                register_bus(bus_id, route, int(seats))
            else:
                print("Please enter a valid number of seats.")
        elif choice == "2":
            bus_id = input("Bus ID to delete: ").strip()
            delete_bus(bus_id)
        elif choice == "3":
            list_buses()
        elif choice == "4":
            customer = input("Enter Customer Name: ").strip()
            bus_id = input("Bus ID for reservation: ").strip()
            seats = input("Number of Seats: ").strip()
            if seats.isdigit():
                make_reservation(customer, bus_id, int(seats))
            else:
                print("Invalid seat number.")
        elif choice == "5":
            show_reservations()
        elif choice == "6":
            res_id = input("Reservation ID to cancel: ").strip()
            if res_id.isdigit():
                cancel_reservation(int(res_id))
            else:
                print("Please enter a valid reservation ID.")
        elif choice == "7":
            print("Thanks for using the Booking System. Goodbye!")
            break
        else:
            print("Invalid option. Please choose from the menu.")

if __name__== "__main__":
    main()
    
    