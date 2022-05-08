def compare_hotels(hotel1, hotel2, customer, nweek, nweekend):
    price1 = hotel1.get_price(customer, nweek, nweekend)
    price2 = hotel2.get_price(customer, nweek, nweekend)

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
    customer, days = line.split(':')
    ndays = days.count(',') + 1
    
    nweekend = days.count('sat')
    nweekend += days.count('sun')

    nweek = ndays - nweekend

    hotels = []

    hotels.append(Hotel('Lakewood', 110, 90, 80, 80, 3))
    hotels.append(Hotel('Bridgewood', 160, 60, 110, 50, 4))
    hotels.append(Hotel('Ridgewood', 220, 150, 100, 40, 5))

    best_hotel = hotels[0]

    for h in hotels:
        best_hotel = compare_hotels(best_hotel, h, customer, nweek, nweekend)

    print(best_hotel.name, best_hotel.get_price(customer, nweek, nweekend), best_hotel.stars)
    
    cheapest_hotel = best_hotel.name

    return cheapest_hotel

class Hotel():

    def __init__(self,
                name,
                regular_weekday_tax,
                regular_weekend_tax,
                reward_weekday_tax,
                reward_weekend_tax,
                stars,
                ):

        self.name = name
        self.regular_weekday_tax = regular_weekday_tax
        self.regular_weekend_tax = regular_weekend_tax
        self.reward_weekday_tax = reward_weekday_tax
        self.reward_weekend_tax = reward_weekend_tax
        self.stars = stars

    def get_price(self, customer, n_weekdays, n_weekends):
        
        if customer == 'Regular':
            price = n_weekdays * self.regular_weekday_tax + n_weekends * self.regular_weekend_tax

        elif customer == 'Rewards':
            price = n_weekdays * self.reward_weekday_tax + n_weekends * self.reward_weekend_tax

        else:
            price = -1

        return price
