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
            
    def set_DiscountPercent(self, value):
        self._DiscountPercent = value)
        
    def get_DiscountPercent(self):
        return self._DiscountPercent
    
    DiscountPercent = property(get_DiscountPercent, set_DiscountPercent)
    
    def get_Summary(self):
        if (self.Details == ''):
            return "{} @ {} ea.".format(self.Quantity, self.UnitCost)
        else:
            return "{}, {} @ {} ea.".format(self.Details, self.Quantity, self.UnitCost)
 

def test():
    item = FlatFeeItem("Flat Rate Service", 2, 75)
    print(item.Description)
    print(item.Quantity)
    print(item.get_Total())
    print(item.get_Summary())
    
if __name__=="__main__":
    test()