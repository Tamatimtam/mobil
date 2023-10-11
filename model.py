class Model:
    def __init__(self, name, price, premium_color_price=0, two_tone_color_price=0):
        self.name = name
        self.price = price
        self.premium_color_price = premium_color_price
        self.two_tone_color_price = two_tone_color_price

    def display(self):
        price_str = f"Rp. {self.price}"
        if self.premium_color_price:
            price_str += f" + {self.premium_color_price} (Premium Color)"
        if self.two_tone_color_price:
            price_str += f" + {self.two_tone_color_price} (Two-Tone Color)"
        print(f"- {self.name}: {price_str}")

    def update_model_name(self, new_name):
        self.name = new_name

    def update_model_price(self, new_price):
        self.price = new_price