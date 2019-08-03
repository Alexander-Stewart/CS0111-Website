from datetime import date
from dataclasses import dataclass

@dataclass(frozen=True)
class Flight:
    num: int
    frm: str
    to: str

# sample of a hashtable from dates to a hashtables from flights to passenger lists
sample = {date(2018, 12, 1): {Flight(150, "BOS", "NYC"): ["Heila", "Eli"],
                              Flight(72, "BOS", "DEN"): ["Julia"]},
          date(2018, 12, 2): {Flight(150, "BOS", "NYC"): ["Leo", "Rohan"],
                              Flight(72, "BOS", "DEN"): ["Valeria"]},
          }

# how to look up data in this nested hashtable
# should print ["Valeria"]
print(sample[date(2018, 12, 2)][Flight(72, "BOS", "DEN")])
print()

# ---------------------------------------------

"""
In hindsight, putting the entire Flight class as the key seems tedious. Since flight
numbers will be unique, let's redo this where there is a separate hashtable from flight
numbers to all of the flight info, and then just use the flightnum as the key in the
sample table.  Here's the revised setup:
"""

# you can see this visually in the powerpoint
sample2 = {date(2018, 12, 1): {150: ["Heila", "Eli"],
                               72: ["Julia"]},
           date(2018, 12, 2): {150: ["Leo", "Rohan"],
                               72: ["Valeria"]},
           }

flight_details = {150: Flight(150, "BOS", "NYC"),
                  72: Flight(72, "BOS", "DEN")}

"""
But we had a concern -- what if we wanted one hashtable that started with flights
and another that started with dates (since we might want to look up on either one). 
Could we have both organizations and only have to maintain one passenger list 
per date/flight combination?

Yes, we just have to set up both hashtables to use the same list locations
in memory.

We're more likely to do that by adding passengers incrementally to flights.
Let's set up the code to do that.
"""

# first, create the empty hashtables
date_to_flights = {}
flight_to_dates = {}

# next, we want to create the keys in these hashtables, but with empty passenger lists.
# The following setup function does that. It takes a month and max day in that month
# to use in the keys, and sets up the hashtable structure:

def setup(month: int, maxday: int, flightnums: list):
    """set up the hashtables with the date/flightnum key combos, but with empty passenger lists"""

    # first, make sure every flight number is a key in the flight_to_dates hashtable
    for flnum in flightnums:
        flight_to_dates[flnum] = {}

    # next, iterate through all of the days in the month. For each day, we will create a date
    #   and set up the date as a key in the date_to_flights hashtable (akin to what we did
    #   for the flight_to_dates table just above.

    for day in range(maxday): # range generates a list of all nums from 0 through maxday - 1.
        d = date(2018, month, day+1) # +1 since range starts at 0 while dates start at 1
        date_to_flights[d] = {}

        # next, we put an empty passenger list in each hashtable for each date/flight combo.
        # We will again iterate over the flightnums (the nested for loops get us every combo
        #   of flight numbers and dates)
        # For each combo, we will create a new passenger list and put the same list (the
        #   same memory location) into each outer hashtable for the same date/flight combo
        for flnum in flightnums:
            passengers: list = []
            date_to_flights[d][flnum] = passengers
            flight_to_dates[flnum][d] = passengers


# set up three flights over a 3-day period
setup(12, 3, [175, 42, 16])

print("Both hashtables after initial setup -- passenger lists empty")
print(date_to_flights)
print()
print(flight_to_dates)

# How will we add passengers? We will write a function (buy_ticket) that registers a
# person on a flight for a given date

def buy_ticket(name: str, flnum: int, d: date):
    """registers given name as passenger on flight for date in both hashtables"""
    flight_to_dates[flnum][d].append(name)

# Buy a ticket and see where Amy shows up
buy_ticket("Amy", 42, date(2018, 12, 2))

print()
print("Both hashtables after Amy buys a ticket")
print(date_to_flights)
print()
print(flight_to_dates)

"""
Study questions:

1. Why did buy_ticket only need to add Amy to one hashtable?

2. In setup, it looks like every flight/date combo is assigned to the empty list
   named passengers. So doesn't that mean all flights/dates are sharing the same list?
   But Amy was only added to the hashtables for the same combo. How are different
   combos getting different lists?
   
3. Why do we need the for loop at line 65 to set up the flightnums as keys? Where
   would the code break if we commented out that line?

"""
