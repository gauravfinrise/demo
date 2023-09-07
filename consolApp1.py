import pandas as pd

    
class ProductDetails():

    def __init__(self):
        self.data = pd.DataFrame()

    def calculateProfitAndLoss(self):
        profit_or_loss = []
        # for i in range(len(self.data)):
        #     cost = self.data['Buying_Price'] * self.data['Buying_Quantity']
        #     revenue = self.data['Selling_Price'] * self.data['Selling_Quantity']
        #     result = revenue - cost
        #     if(result>0):
        #         profit_or_loss.append (f'you are in profit of {result}r') 
        #     else:
        #         profit_or_loss.append(f'you are in loss of {result}r')

        #     print("=================================================")
        #     print(profit_or_loss)

        
        cost = self.data['Buying_Price'][0] * self.data['Buying_Quantity'][0]
        revenue = self.data['Selling_Price'][0] * self.data['Selling_Quantity'][0]
        result = revenue - cost
        if(result>0):
            profit_or_loss.append (f'you are in profit of {result}r') 
        else:
            profit_or_loss.append(f'you are in loss of {result}r')

        # print("=================================================")
        # print(profit_or_loss)
        return profit_or_loss
    
    def printProductDetails(self):

        profitOrLoss = self.calculateProfitAndLoss()
        # productData = {
        #     'Product_Name':self.data['Product_Name'],
        #     'Buying_Price':self.data['Buying_Price'], 
        #     'Buying_Quantity':self.data['Buying_Quantity'], 
        #     'Selling_Price':self.data['Selling_Price'], 
        #     'Selling_Quantity':self.data['Selling_Quantity'], 
        #     'Profit_or_Loss':profitOrLoss
        #     }

        # self.data = pd.DataFrame(productData, index=[0])
        self.data['Profit_or_Loss']=profitOrLoss
        print(self.data)

    def inputFromUser(self):
        product_data = {}
        product_data['Product_Name'] = input("Enter product name: ")
        product_data['Buying_Price'] = int(input("Enter products buying price: "))
        product_data['Buying_Quantity'] = int(input("Enter products buying quantity: "))
        product_data['Selling_Price'] = int(input("Enter products selling price: "))
        product_data['Selling_Quantity'] = int(input("Enter products selling quantity: "))
        
        self.data = self.data._append(product_data, ignore_index=True)
        # print(self.data)
          

def main():

    obj = ProductDetails()
    obj.inputFromUser()
    obj.calculateProfitAndLoss()
    obj.printProductDetails()

    

if __name__ == "__main__":
    main()
