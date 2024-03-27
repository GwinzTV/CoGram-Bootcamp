
# Function definitions:
def hotel_cost(nights):
    total_cost = nights*89
    return total_cost

def plane_cost(flight):
    if flight == 'new york':
        total_cost = 240
    elif flight == 'london':
        total_cost = 100
    elif flight == 'spain':
        total_cost = 50
    else:
        total_cost = 89
    return total_cost

def car_rental(days):
    total_cost = days*50
    return total_cost

def holiday_cost(hotel, car, plane):
    print(f'The total sum of the holiday, including: hotel costs (£{hotel}), car rental (£{car}), and plane costs (£{plane}), is £{hotel+car+plane}.')

# User input:
try:
    city_flight = input("which city are you flying to?  ").lower()
    num_nights = int(input("How many nights are you staying at the hotel? "))
    rental_days = int(input("What is the duration in days of your holiday? "))

    if num_nights < 0 or rental_days < 0:
        loop = True
        while loop:
            print("\n\nNumber of nights and rental days cannot be negative.\n")
            num_nights = int(input("How many nights are you staying at the hotel? "))
            rental_days = int(input("What is the duration in days of your holiday? "))
            if num_nights > 0 or rental_days > 0:
                loop = False

    car = car_rental(rental_days)
    flight = plane_cost(city_flight)
    hotel = hotel_cost(num_nights)

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# script:
holiday_cost(hotel, car, flight)