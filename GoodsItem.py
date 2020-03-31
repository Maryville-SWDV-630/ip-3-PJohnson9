# Patrick Johnson         3/30/2020 #
# SWDV 630 3W 20/SP2         Week 3 #
#####################################
# Subclass for physical goods

from SaleItem import SaleItem

class GoodsItem(SaleItem):
    def __init__(self, Description, Quantity, UnitCost, Details = '', TaxRate = 0.06):
        self.Description = Description
        self.Quantity = Quantity
        self.UnitCost = UnitCost
        self.Details = Details
        self.TaxRate = TaxRate
        
    def get_Tax(self):
        return round(self.Quantity * self.UnitCost * self.TaxRate,2)
    
    Tax = property(get_Tax)
    
    def get_Summary(self):
        if (self.Details == ''):
            return "{} @ {:.2f} ea.".format(self.Quantity, self.UnitCost)
        else:
            return "{}, {} @ {:.2f} ea.".format(self.Details, self.Quantity, self.UnitCost)
        
def test():
    item = GoodsItem("Sample Good", 5, 5.75, 'Green, Size 00')
    print(item.TaxRate)
    print(item.Tax)
    print(item.get_Total())
    print(item.get_Summary())
    

if __name__=="__main__":
    test()