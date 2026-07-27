SEAT_PRICE = 150

seats = ["Available"] * 10
booked_count = 0
total_revenue = 0


def view_seats():
    print("\n========== SEAT STATUS ==========")
    for i in range(10):
        print(f"Seat {i + 1} : {seats[i]}")
    print("=================================")


def book_ticket():
    global booked_count
    global total_revenue

    view_seats()

    seat = int(input("\nEnter seat number (1-10): "))

    if seat < 1 or seat > 10:
        print("Invalid seat number.")
        return

    if seats[seat - 1] == "Booked":
        print("Seat already booked.")
    else:
        name = input("Enter customer name: ")

        seats[seat - 1] = "Booked"

        booked_count += 1
        total_revenue += SEAT_PRICE

        print("\nTicket Booked Successfully!")
        print("----------------------------")
        print("Customer :", name)
        print("Seat No  :", seat)
        print("Price    : ₹", SEAT_PRICE)


def cancel_ticket():
    global booked_count
    global total_revenue

    view_seats()

    seat = int(input("\nEnter seat number to cancel: "))

    if seat < 1 or seat > 10:
        print("Invalid seat number.")
        return

    if seats[seat - 1] == "Available":
        print("Seat is already available.")
    else:
        seats[seat - 1] = "Available"

        booked_count -= 1
        total_revenue -= SEAT_PRICE

        print("Ticket cancelled successfully.")


def booking_summary():
    available = 10 - booked_count

    print("\n========== BOOKING SUMMARY ==========")
    print("Total Seats      :", 10)
    print("Booked Seats     :", booked_count)
    print("Available Seats  :", available)
    print("Total Revenue    : ₹", total_revenue)
    print("=====================================")


while True:

    print("\n========== MOVIE TICKET BOOKING ==========")
    print("1. View Seats")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Booking Summary")
    print("5. Exit")
    print("==========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_seats()

    elif choice == "2":
        book_ticket()

    elif choice == "3":
        cancel_ticket()

    elif choice == "4":
        booking_summary()

    elif choice == "5":
        print("\nThank you for using Movie Ticket Booking System!")
        break

    else:
        print("Invalid choice. Please try again.")
