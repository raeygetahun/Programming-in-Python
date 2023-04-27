class Article:
    def __init__(self,name,date,about,number,price):
        self._name=name
        self._date=date
        self._about=about
        self._number=number
        self._price=price
        
    def get_name(self):
        return self._name
    
    def get_date(self):
        return self._date
    
    def get_about(self):
        return self._about

    def get_number(self):
        return self._number
    
        
    def set_name(self, name):
            self._name = name
            
    def set_date(self, date):
        self._date = date

    def set_about(self, about):
        self._about = about
        
    def set_number(self, number):
        self._number = number

    def set_price(self, price):
        self._price = price
        
    def __str__(self):
        return "Name: "+ self._name +\
        "\nDate: "+ self._date + "\nabout: "+ self._about+\
            "\nnumber: "+str(self._number)+"\nprice: "+str(self._price)
     