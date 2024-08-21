class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill, flatmate2):
        """
        :param bill:
        :param flatmate2:
        :return:
        """
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = round((bill.amount * weight), 2)
        return to_pay
