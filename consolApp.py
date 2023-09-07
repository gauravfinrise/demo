import pandas as pd
class Product():
    def __init__(self,productName,buyingPrice, buyingQuantity, sellingPrice, sellingQuantity):
        self.productName = productName
        self.buyingPrice = buyingPrice
        self.buyingQuantity = buyingQuantity
        self.sellingPrice = sellingPrice
        self.sellingQuantity = sellingQuantity
        self.data = pd.DataFrame
    
class ProductDetails(Product):
    def __init__(self, productName, buyingPrice, buyingQuantity, sellingPrice, sellingQuantity):
        super().__init__(productName, buyingPrice, buyingQuantity, sellingPrice, sellingQuantity)
    
    def calculateProfitAndLoss(self):
        cost = self.buyingPrice * self.buyingQuantity
        revenue = self.sellingPrice * self.sellingQuantity
        result = revenue - cost
        if(result>0):
            returnresult = f'you are in profit of {result}r'
        else:
            returnresult = f'you are in loss of {result}r'
        return returnresult
    
    def printProductDetails(self):

        profitOrLoss = self.calculateProfitAndLoss()

        # print("name: ", self.productName)
        # print("product buying price: ", self.buyingPrice)
        # print("product buying quantity: ", self.buyingQuantity)
        # print("product selling price: ", self.sellingPrice)
        # print("product selling quantity: ", self.sellingQuantity)
        # print("profit and loss: ", profitOrLoss  )

        # productData = [self.productName, self.buyingPrice, self.buyingQuantity, self.sellingPrice,self.sellingQuantity, profitOrLoss]
        productData = {
            'Product Name':self.productName,
            'Buying Price':self.buyingPrice, 
            'Buying Quantity':self.buyingQuantity, 
            'Selling Price':self.sellingPrice, 
            'Selling Quantity':self.sellingQuantity, 
            'Profit or Loss':profitOrLoss
            }

        self.data = pd.DataFrame(productData, index=[0])
        print(self.data)

        def inputFromUser():
            pass

def main():
    productName = input("Enter product name: ")
    buyingPrice = int(input("Enter products buying price: "))
    buyingQuantity = int(input("Enter products buying quantity: "))
    sellingPrice = int(input("Enter products selling price: "))
    sellingQuantity = int(input("Enter products selling quantity: "))
    


    obj = ProductDetails(productName,buyingPrice,buyingQuantity,sellingPrice,sellingQuantity)
    obj.printProductDetails()
    

if __name__ == "__main__":
    main()


    



            


