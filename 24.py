class Money:
    def __init__(self, money):
        self.__money = 0
        self.set_money(money)

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
       return self.__money

    def add_money(self, mn):
        if self.__check_money(mn):
            self.__money += mn.get_money()

    @classmethod
    def __check_money(self, money):
        return isinstance(money, int) and money >= 0
