"""
Homework16.

Description:
    write class for bank card.
    Class should reflect card lifecycle, card operations etc.
    use CVV, PIN, Name, Surname , end date, card_num as initial params
    class should have in addition to common logic some class attributes,
    as minimum one classmethod and
    as minimum  one staticmethod, two or more getters/setters
    do not forget about block "if __name__ == '__main__':"
"""

SPLIT = 45


class BankCard:
    """Bank Card class."""

    USD_RATE = 36.6

    def __init__(self, card_num, name, surname, end_date, cvv, pin, balance):
        """Initialize class instance for BankCard."""
        self.card_num = card_num
        self.name = name
        self.surname = surname
        self.end_date = end_date
        self.cvv = cvv
        self.pin = pin
        self.balance = balance

    @classmethod
    def uah_to_usd(cls, uah):
        """Return exchanged balance."""
        return uah / cls.USD_RATE

    @staticmethod
    def validate_card_num(card_num):
        """Validate card number."""
        card_num = card_num.replace(' ', '')
        return len(card_num) == 16

    @staticmethod
    def validate_card_cvv(cvv):
        """Validate card cvv."""
        return len(cvv) == 3

    @staticmethod
    def validate_card_pin(pin):
        """Validate card pin."""
        return len(pin) == 4

    # get balance method
    def get_balance(self):
        """Get card balance."""
        return self.balance

    def validate_balance(self):
        """Validate card balance."""
        if my_card.get_balance() >= price:
            return self.balance
        else:
            print('You have not enough money')

    def set_charge(self, donate):
        """Charge card balance."""
        if donate > 0:
            self.balance += donate
            print(f'Your balance was charged up to {my_card.balance} UAH '
                  f'(+{donate} UAH)')
            print(f'Current balance in USD: '
                  f'{my_card.uah_to_usd(uah=my_card.balance)}')

    def set_purchase(self, price):
        """Purchase flair price from card balance."""
        if my_card.validate_balance():
            self.balance -= price
            print('You made purchase successfully')


if __name__ == '__main__':
    print('Your card:')

    my_card = BankCard('0101 1010 1100 0011', 'Chilly', 'Cat',
                       '10/27', '322', '1234', 0)

    print('=' * SPLIT)
    print(f'Card number: {my_card.card_num}')
    print(f'Cardholder name: {my_card.name}')
    print(f'Cardholder surname: {my_card.surname}')
    print(f'card expiration date: {my_card.end_date}')
    print(f'Card CVV: {my_card.cvv}')
    print(f'Card PIN: {my_card.pin}')
    print(f'Balance: {my_card.balance} UAH')
    print('=' * SPLIT)

    my_card.validate_card_num(my_card.card_num)
    my_card.validate_card_cvv(my_card.cvv)
    my_card.validate_card_pin(my_card.pin)
    print('Card validation passed successfully')

    print('=' * SPLIT)
    donate = int(input('Charge your balance: '))
    my_card.set_charge(donate)

    print('=' * SPLIT)
    price = int(input('Enter a flair price: '))
    my_card.set_purchase(price)

    print('=' * SPLIT)
    print(f'Current balance in UAH: {my_card.balance}')
    print(f'Current balance in USD: {my_card.uah_to_usd(uah=my_card.balance)}')
