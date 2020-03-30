# Patrick Johnson         3/30/2020 #
# SWDV 630 3W 20/SP2         Week 3 #
#####################################
# Subclass for hourly services

from SaleItem import SaleItem

class HourlyItem(SaleItem):
    def __init__(self, Description, Quantity, UnitCost, Details = ''):
        self.Description = Description
        self.Quantity = Quantity
        self.UnitCost = UnitCost
        self.Details = Details
        
    def get_Tax(self):
        return round(self.Quantity * self.UnitCost * self.TaxRate,2)
    
    def get_Summary(self):
        if (self.Details == ''):
            return "{}, {} hr. @ {}/hr".format(self.Description,
                                 self.Quantity, self.UnitCost)
        else:
            return "{}, {}, {} hr. @ {}/hr".format(self.Description,
                   self.Details, self.Quantity, self.UnitCost)
 

def test():
    item = HourlyItem("Sample Hourly Service", 5, 5.75)
    print(item.Description)
    print(item.Quantity)
    print(item.get_Total())
    print(item.get_Summary())



if __name__=="__main__":
    test()
