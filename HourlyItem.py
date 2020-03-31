# Patrick Johnson         3/30/2020 #
# SWDV 630 3W 20/SP2         Week 3 #
#####################################
# Subclass for hourly services

from SaleItem import SaleItem

class HourlyItem(SaleItem):
    def __init__(self, Description, Quantity, HourlyRate, Details = ''):
        self.Description = Description
        self.Quantity = Quantity
        self.UnitCost = HourlyRate
        self.Details = Details
        
    def get_HourlyRate(self):
        return self.UnitCost
    
    def set_HourlyRate(self, value):
        self.UnitCost = value
        
    HourlyRate = property(get_HourlyRate, set_HourlyRate)
    
    def get_Summary(self):
        if (self.Details == ''):
            return "{} hr @ {}/hr".format(self.Quantity, self.HourlyRate)
        else:
            return "{}, {} hr. @ {}/hr".format(self.Details, self.Quantity, self.HourlyRate)
 

def test():
    item = HourlyItem("Sample Hourly Service", 2, 25, "Doing something")
    print(item.Details)
    print(item.HourlyRate)
    item.set_HourlyRate(22.50)
    print(item.get_HourlyRate())
    print(item.get_Summary())


if __name__=="__main__":
    test()
