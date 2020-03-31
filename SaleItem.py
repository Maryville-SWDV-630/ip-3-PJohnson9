# Patrick Johnson         3/30/2020 #
# SWDV 630 3W 20/SP2         Week 3 #
#####################################
# Code a generic superclass and at least three subclasses of that superclass,
# each class needs to have at least 2 attributes and 2 methods.
# You need to provide a test method that shows your classes in operation.
#
# SaleItem base class for invoice items

class SaleItem:
    def __init__(self, Description, Quantity, UnitCost):
        self.Description = Description
        self.Quantity = Quantity
        self.UnitCost = UnitCost
        self.Tax = 0
    
    def get_Total(self):
        return round(self.Quantity * self.UnitCost,2)
        
    def get_Summary(self):
        return "{} @ {} ea.".format(self.Quantity, self.UnitCost)
    
    Total = property(get_Total, None, None, "LineItem Total Without Tax")
    Summary = property(get_Summary)


def test():
    item = SaleItem("Sample Item", 4, 13.75)
    print(item.Description)
    print(item.Quantity)
    print(item.get_Total())
    print(item.get_Summary())

if __name__=="__main__":
    test()
    