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
            price = n_weekdays*self.regular_weekday_tax + n_weekends*self.regular_weekend_tax

        elif customer == 'Rewards':
            price = n_weekdays*self.reward_weekday_tax + n_weekends*self.reward_weekend_tax

        else:
            price = -1

        return price