# User input:
city_flight = input("which city are you flying to?  ")
num_nights = int(input("How many nights are you staying at the hotel? "))
rental_days = int(input("What is the duration in days of your holiday? "))

# Function definitions:
def hotel_cost(nights = num_nights):
    total_cost = num_nights*89
    return total_cost

def plane_cost(flight = city_flight):
    if city_flight == 'NYC':
        total_cost = 240
    elif city_flight == 'LDN':
        total_cost = 100
    elif city_flight == 'SPN':
        total_cost = 50
    else:
        total_cost = 89
    return total_cost

def car_rental(days = rental_days):
    total_cost = days*50
    return total_cost

def holiday_cost(hotel, car, plane):
    print(f'The total sum of the holiday, including: hotel costs (£{hotel}), car rental (£{car}), and plane costs (£{plane}), is £{hotel+car+plane}.')

# script:
holiday_cost(hotel_cost(), car_rental(), plane_cost())