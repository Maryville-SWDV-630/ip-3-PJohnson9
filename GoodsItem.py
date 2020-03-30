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
    
    def get_Summary(self):
        if (self.Details == ''):
            return "{}, {} @ {} ea.".format(self.Description,
                                 self.Quantity, self.UnitCost)
        else:
            return "{}, {}, {} @ {} ea.".format(self.Description,
                   self.Details, self.Quantity, self.UnitCost)
 

def test():
    item = GoodsItem("Sample Good", 5, 5.75, 'Green, Size 00')
    print(item.Description)
    print(item.Quantity)
    print(item.get_Total())
    print(item.get_Summary())
    print(item.get_Tax())


if __name__=="__main__":
    test()