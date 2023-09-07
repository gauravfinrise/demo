import pandas as pd
import numpy as np
import csv
from dateutil import parser
from datetime import datetime

class Demo():
    
    def readDataFrames(self):

        contract = pd.read_csv('rms_contract_20230811.csv')
        settlementDf = pd.read_csv('MARKETSTATS-20230811.csv')
        self.exchange = 'DGCX'
        contract = contract.rename(columns={'securitytype':'Instrument Type'})
        condition1 = contract['Instrument Type']=='FUTURE'
        contract.loc[condition1, 'Instrument Type'] = 'FUTURES'
        contract = contract.loc[contract['exchange']==self.exchange]

        try:
            merged_df = contract.merge(settlementDf, on='Instrument Type', how='left')
            subset_columns = ['exchange','symbol','scripcode','Instrument Type','Settlement Price']
            subset_df = merged_df[subset_columns]
            subset_df.to_csv('data.csv', index=False)

            print(subset_df)

        except Exception as e:
            print(e)
            
    def Bhavcopy(self):
        try:
            data = pd.read_csv('NSEIFSC_G_T1_Bhavcopy_FO_140823.CSV')
            contract_df = pd.read_csv('rms_contract_20230811.csv')
            contract_df=contract_df.loc[contract_df['exchange']=='NSEIFSC']
            data['securitytype']=data['CONTRACT_D'].apply(lambda x : str(x)[:6])
            data['symbol']=data['CONTRACT_D'].apply(lambda x : str(x)[6:-11])
            data['expirydate']=data['CONTRACT_D'].apply(lambda x : datetime.strptime(str(x)[-11:],'%d-%b-%Y').strftime('%d%b%Y'))
            newdata=data[['securitytype','symbol','expirydate','SETTLEMENT']]

            newdata.to_csv('data.csv', index=False)

            merged_df = contract_df.merge(newdata, on=['securitytype','expirydate','symbol'], how='left')

            print(merged_df)
            subset_columns = ['token','SETTLEMENT']
            subset_df = merged_df[subset_columns]
            subset_df.to_csv('data.csv', index=False)

        except Exception as e:
            print(e)
obj = Demo()
# obj.readDataFrames()
obj.Bhavcopy()