from datetime import datetime

class credit_card:
    def __init__(self, exp_month, exp_year, first_name, last_name, card_number):
        self.__exp_month = exp_month
        self.__exp_year = exp_year
        self.__first_name = first_name
        self.__last_name = last_name
        self.__card_number = card_number

    def format_expiry_date(self):
        month = str(self.__exp_month).zfill(2)
        year = str(self.__exp_year)[-2:]
        formatted_date = month + '/' + year
        print(formatted_date)
        return formatted_date
    
    def format_full_name(self):
        return self.__first_name + ' ' + self.__last_name
    
    def format_card_number(self):
        s = self.__card_number[:4] + ' ' + self.__card_number[4:8] + ' ' + self.__card_number[8:12] + ' ' + self.__card_number[12:]
        return s
    
    def is_valid(self):
        if self.__exp_year < datetime.now().year or (self.__exp_year == datetime.now().year and self.__exp_month < datetime.now().month):
            return False
        else:
            return True
        
    def __str__(self):
        s = f'Card Number: {self.format_card_number()}' + '\n' + f'Expiry Date: {self.format_expiry_date()}' + '\n' + f'Account Holder: {self.format_full_name()}' + '\n' + f'Is valid: {self.is_valid()}'

        return s



cc1 = credit_card(10, 2014, "Bob", "Jones", "1234567890123456")
cc2 = credit_card(10, 2034, "Bob", "Jones", "1234567890123456")

print(cc1.__str__())
print(cc2.__str__())

# print(cc1.format_card_number())
# print(cc1.format_expiry_date())