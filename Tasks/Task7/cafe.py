
class Cafe:
    # == initializing the class == #
    def __init__(self):
        self.menu = ['Coffee',
                     'Pastries', 
                     'Sandwiches',
                     'Salads']
        self.stock = {'Coffee': 4,
                      'Pastries': 7,
                      'Sandwiches': 2,
                      'Salads': 10}
        self.price = {
            'Coffee': 7.4,
            'Pastries': 4.8,
            'Sandwiches': 9.5,
            'Salads': 6.5}

    # == calculating the total stock == #
    def total_stock(self):
        menu = self.menu
        stock = self.stock
        price = self.price
        total = 0
        # == iterates through all stock and sums their total value == #
        for item in menu:
            total += stock[item]*price[item]

        print(f'The total stock in the cafe is worth: £{total}')


joshua_cafe = Cafe()
joshua_cafe.total_stock()