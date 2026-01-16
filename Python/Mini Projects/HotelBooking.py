from datetime import datetime

# ------------------ Data Structures ------------------

class Booking:
    def __init__(self, guest_name, room_type, check_in, check_out):
        self.guest_name = guest_name
        self.room_type = room_type
        self.check_in = check_in
        self.check_out = check_out
        self.next = None

class HotelSystem:
    def __init__(self):
        # Each day has a list of 5 booleans (True = available) for each room type
        self.room_availability = {
            "Single": [[True] * 5 for _ in range(30)],
            "Double": [[True] * 5 for _ in range(30)],
            "Suite": [[True] * 5 for _ in range(30)]
        }
        self.bookings_head = None
        self.guest_bookings = {}

    def date_to_index(self, date_str):
        base_date = datetime.today()
        target_date = datetime.strptime(date_str, "%Y-%m-%d")
        return (target_date - base_date).days

    def is_available(self, room_type, check_in, check_out):
        start = self.date_to_index(check_in)
        end = self.date_to_index(check_out)
        if start < 0 or end >= len(self.room_availability[room_type]):
            return False
        # Check if at least one room is available for all days in range
        for i in range(start, end):
            if not any(self.room_availability[room_type][i]):
                return False
        return True

    def book_room(self, guest_name, room_type, check_in, check_out):
        if not self.is_available(room_type, check_in, check_out):
            print("❌ Room not available for selected dates.")
            return

        start = self.date_to_index(check_in)
        end = self.date_to_index(check_out)
        # Find the first available room index for all days
        for room_idx in range(5):
            if all(self.room_availability[room_type][i][room_idx] for i in range(start, end)):
                for i in range(start, end):
                    self.room_availability[room_type][i][room_idx] = False
                booking = Booking(guest_name, room_type, check_in, check_out)
                booking.next = self.bookings_head
                self.bookings_head = booking
                self.guest_bookings.setdefault(guest_name, []).append(booking)
                print(f"✅ Booking confirmed for {guest_name} in {room_type} (Room {room_idx+1}) from {check_in} to {check_out}")
                return
        print("❌ Room not available for selected dates.")

    def show_bookings(self):
        print("\n Current Bookings:")
        current = self.bookings_head
        while current:
            print(f"{current.guest_name} → {current.room_type} ({current.check_in} to {current.check_out})")
            current = current.next

    def search_guest(self, guest_name):
        print(f"\n🔍 Bookings for {guest_name}:")
        for b in self.guest_bookings.get(guest_name, []):
            print(f"{b.room_type} from {b.check_in} to {b.check_out}")

# ------------------ Menu Driven Interface ------------------

def run_hotel_system():
    hotel = HotelSystem()

    while True:
        print("\n****** Hotel Booking System Menu ******")
        print("      1. Book a Room")
        print("      2. View All Bookings")
        print("      3. Search Guest Booking")
        print("      4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            guest_name = input("Enter guest name: ")
            ch = int(input("Enter room type: \n1: Single\n2: Double\n3: Suite "))
            if ch == 1:
                room_type = "Single"
            elif ch == 2:
                room_type = "Double"
            elif ch == 3:
                room_type = "Suite"
            check_in = input("Enter check-in date (YYYY-MM-DD): ")
            check_out = input("Enter check-out date (YYYY-MM-DD): ")
            hotel.book_room(guest_name, room_type, check_in, check_out)

        elif choice == "2":
            hotel.show_bookings()

        elif choice == "3":
            guest_name = input("Enter guest name to search: ")
            hotel.search_guest(guest_name)
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

run_hotel_system()
