def show_movies():
    print("🎬 Available Movies")
    print("1. Avengers - 10:30 AM")
    print("2. Interstellar - 1:00 PM")
    print("3. Batman - 6:00 PM")

def book_ticket(movie_name, tickets):
    print(f"Movie   : {movie_name}")
    print(f"Tickets : {tickets}")

def calculate_bill(ticket_price, quantity):
    total = ticket_price * quantity
    print(f"Ticket Price : ₹{ticket_price}")
    print(f"Total Bill   : ₹{total}")
    return total

def payment(method, amount):
    print(f"Payment Method : {method}")
    print(f"Paid Amount    : ₹{amount}")

def thank_you(name):
    print(f"Thank you {name}! Enjoy your movie 🍿")

# Program Flow
show_movies()
book_ticket("Avengers", 2)
total = calculate_bill(250, 2)
payment("UPI", total)
thank_you("Kiran")