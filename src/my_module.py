from .hotel import Hotel

hotels = []
hotels.append(Hotel('Lakewood', 110, 90, 80, 80, 3))
hotels.append(Hotel('Bridgewood', 160, 60, 110, 50, 4))
hotels.append(Hotel('Ridgewood', 220, 150, 100, 40, 5))

def compare_hotels(hotel1, hotel2, customer, n_weekdays, n_weekends):
    '''
    Compare two hotels and returns the best for some customer based on the number 
    of days required.

    Parameters:
        hotel1 (Hotel):The first hotel to be compared.
        hotel2 (Hotel):The second hotel to be compared.
        customer (str):The type of customer (regular or rewards).
        n_weekdays (int):Number of weekdays.
        n_weekends (int):Number of weekends.

    Returns:
        (Hotel):The cheapest hotel according price and stars.
    '''
    price1 = hotel1.get_price(customer, n_weekdays, n_weekends)
    price2 = hotel2.get_price(customer, n_weekdays, n_weekends)

    if price1 < price2:
        return hotel1
    
    elif price2 < price1:
        return hotel2
    
    else:
        if hotel1.stars > hotel2.stars:
            return hotel1
        else:
            return hotel2


def get_cheapest_hotel(line):
    '''
    Get the cheapest hotel name.

    Parameters:
        line (str):<type_of_client>: <date1>, <date2>, <date3>, ....

    Returns:
        (str):The cheapest hotel name according price and stars.
    '''
    customer, days = line.split(':')
    n_days = days.count(',') + 1
    
    n_weekends = days.count('sat')
    n_weekends += days.count('sun')

    n_weekdays = n_days - n_weekends

    cheapest_hotel = hotels[0]

    for h in hotels:
        cheapest_hotel = compare_hotels(cheapest_hotel, h, customer, n_weekdays, n_weekends)

    return cheapest_hotel.name
