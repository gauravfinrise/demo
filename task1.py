import pandas as pd
import numpy as np
import csv
from dateutil import parser

class Demo():

    # def __init__(self):
        

    def readSettlementFile(self):
       
        settlementDf = pd.read_csv('MARKETSTATS-20230811.csv')
        # print(settlementDf)
        self.instrumentType = settlementDf.loc[0,'Instrument Type']
        # self.exchange = 'DGCX'
        self.settlementPrice = settlementDf.loc[0,'Previous settlement Price']
        print(self.exchange, self.instrumentType, self.settlementPrice)
    
    def readDataFrames(self):
        
        contract = pd.read_csv('rms_contract_20230811.csv')
        settlementDf = pd.read_csv('MARKETSTATS-20230811.csv')
        self.exchange = 'DGCX'
        condition1 = contract['exchange']==self.exchange
        condition2 = contract['securitytype'].isin(settlementDf['Instrument Type'])
        contract.loc[condition1, 'securitytype'] = 'FUTURES'

        contract = contract.loc[contract['exchange']==self.exchange]
        # print(contract)

        contract = contract[contract['securitytype'].isin(settlementDf['Instrument Type'])]
        

        # contract['Settlement Price'] = np.where(condition2, settlementDf.loc[condition2, 'Settlement Price'], contract['Settlement Price'])

        # contract['Settlement Price'] = settlementDf.loc[condition2, settlementDf['Settlement Price']]



        # contract['Settlement Price'] = settlementDf['Settlement Price'].where(condition1)

        # merged_df = contract.merge(settlementDf, on=settlementDf['Instrument Type'], how='inner')

        print(contract)
        # final_result = merged_df[merged_df['Value_df2'] == 'B']


        # # print(contract)
        # condition1 = contract['exchange']==self.exchange
        # condition2 = contract['securitytype']==self.instrumentType
        # contract.loc[condition1, 'securitytype'] = 'FUTURES'
        
        # contract = contract.loc[contract['exchange']==self.exchange]
        # contract = contract.loc[contract['securitytype']==self.instrumentType]
        # contract['Previous settlement Price'] = self.settlementPrice
        
        # # print(contract)
        # # print(contract.loc['Expiry date'])

        contract.to_csv('data.csv', index=False)
        


obj = Demo()
# obj.readSettlementFile()
obj.readDataFrames()