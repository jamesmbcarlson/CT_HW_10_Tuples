# James Carlson 
# Coding Temple - SE FT-144
# Backend Module 3 Lesson 2 Assignment: Tuples

print("\n====== 1. Tuple Mastery in Python ======\n")

# takes list of tuples, returns string
def get_itineraries(list_tuples):
    itinerary_string = ""
    for i in range(len(list_tuples)):
        itinerary_string += f"Itinerary {i+1}: {list_tuples[i][0]} - From {list_tuples[i][1]} to {list_tuples[i][2]}\n"
    return itinerary_string

itineraries = [
    ("Alice", "New York", "London"), 
    ("Bob", "Tokyo", "San Francisco"),
    ("James", "Denver", "Boston"),
    ("Megan", "Denver", "Boston")
]

print(get_itineraries(itineraries))



print("\n====== 2. Python Data Structure Challenges in Real-World Scenarios ======\n")

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# takes book tuple with title an author, prints result
def add_book(book):
    if book in library:
        print(f"{book[0]} by {book[1]} is already in the library.")
    else:
        library.append(book)
        print(f"{book[0]} by {book[1]} has been added to the library!")

# test cases
add_book(("Mistborn: The Final Empire", "Brandon Sanderson"))
add_book(("1984", "George Orwell"))
print("\nLibrary:", library, "\n")



print("\n====== 3. Python Loops and Tuples in Analytical Applications ======\n")
print("    === 3.1 Stock Market Data Analysis ===\n")

stock_data = [
    ("AAPL", "2021-01-04", 127.00),
    ("AAPL", "2021-01-05", 128.57),
    ("AAPL", "2021-01-06", 124.24),
    ("AAPL", "2021-01-07", 128.48),
    ("AAPL", "2021-01-08", 129.59),
    ("MSFT", "2021-01-04", 211.61),
    ("MSFT", "2021-01-05", 211.81),
    ("MSFT", "2021-01-06", 206.32),
    ("MSFT", "2021-01-07", 212.19),
    ("MSFT", "2021-01-08", 213.48)
]

# takes stock symbol and prints average if stock in data set
def print_average_closing_price(stock):

    total_price = 0
    stock_listed = 0

    # search through stock data and increment stock count and add to total
    for s in stock_data:
        if s[0] == stock:
            stock_listed += 1
            total_price += s[2]

    # if stock appeared in data, print out average closing price
    if stock_listed > 0:
        print(f"Average Closing Price for {stock}: {round(total_price / stock_listed, 2)}")
    else:
        print(f"{stock} not found in data set.")

# test cases
print_average_closing_price("AAPL")
print_average_closing_price("MSFT")
print_average_closing_price("GOOG")



print("\n    === 3.2 Event Attendance Tracker ===\n")

attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    ("James Carlson, Game Developer Extraordinaire", "Game Developers Conference"),
    ("Hugh Mann", "AI Summit"),
    ("Alex Swiggum", "Python Conference"),
    ("Gabe Newell", "Game Developers Conference"),
    ("Ben Brode", "Game Developers Conference"),
    ("Tim Schafer", "Game Developers Conference")
]

# takes event name and prints attendees and number of attendees
def list_attendees(event):
    print(f"Attendees for this year's {event}:")
    attendance = 0

    for person, conference in attendees:
        if conference == event:
            print(" " + person)
            attendance += 1
    
    if attendance > 0:
        print(f"{attendance} people in attendance! Pretty good!")
    else:
        print("None! No one's attending. Maybe they'll cancel...")
    print()

# test cases
list_attendees("Python Conference")
list_attendees("AI Summit")
list_attendees("Game Developers Conference")
list_attendees("Trash Expo")