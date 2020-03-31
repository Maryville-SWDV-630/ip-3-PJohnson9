# Patrick Johnson         3/30/2020 #
# SWDV 630 3W 20/SP2         Week 3 #
#####################################
# Subclass for flat fee services

from SaleItem import SaleItem

class FlatFeeItem(SaleItem):
    def __init__(self, Description, Quantity, UnitCost, Details = ''):
        self.Description = Description
        self.Quantity = Quantity
        self.UnitCost = UnitCost
        self.Details = Details
        self._DiscountPercent = 0
            
    def set_DiscountPercent(self, value):
        self._DiscountPercent = value
        
    def get_DiscountPercent(self):
        return self._DiscountPercent
    
    def set_UnitCost(self, value):
        self._UnitCost = value
    
    def get_UnitCost(self):
        return self._UnitCost * (100 - self.DiscountPercent)/100
    
    DiscountPercent = property(get_DiscountPercent, set_DiscountPercent)
    UnitCost = property(get_UnitCost, set_UnitCost)
    
    def get_Summary(self):
        if (self.Details == ''):
            return "{} @ {:.2f} ea.".format(self.Quantity, self.UnitCost)
        else:
            return "{}, {} @ {:.2f} ea.".format(self.Details, self.Quantity, self.UnitCost)
 

def test():
    item = FlatFeeItem("Flat Rate Service", 2, 75)
    print(item.get_UnitCost())
    item.DiscountPercent = 20.0
    print(item.DiscountPercent)
    print(item.UnitCost)
    print(item.get_Summary())
    
if __name__=="__main__":
    test()