# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:12:41 2017

@author: parithy

This is a stock portfolio analysis modules, This takes the input of list of stock 
and purchse prices and snapshot the price differences 
"""

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style


style.use('ggplot')
ls_key = 'Adj Close'
stock = ['FIT' ,'PLUG' ,'BUFF' , 'CSCO', 'TTM','BNCN','JCP','LFGR','LNTH','RAS','INFY',
         'AMD','TICC','RUN','PXLW','GUID','PER','BLPH','SIRI','SNAP']
         
stock_price_dict = {'FIT': 7.55,
                    'PLUG':2.35,
                    'BUFF':23.92,
                    'CSCO':30.59,
                    'TTM':33.98,
                    'BNCN':32.00,
                    'JCP':9.64,
                    'LFGR':6.80,
                    'LNTH':9.05,
                    'RAS':3.34,
                    'INFY':14.82,
                    'AMD':10.738,
                    'TICC':6.72,
                    'RUN':5.941,
                    'PXLW':4.19,
                    'GUID':7.41,
                    'PER':3.25,
                    'BLPH':1.20,
                    'SIRI':5.107,
                    'SNAP':24.92}


def get_latest_price(stock):
    start = dt.datetime(2017,1,1)
    end=dt.datetime.now()
    f=web.DataReader(stock,'yahoo', start, end)
    cleandata=f.ix[ls_key]
    df=pd.DataFrame(cleandata)
    df=df.tail(1)
    return df
    
    
def get_purchase_price(stock_price_dict):
    date=pd.date_range(dt.datetime(2017,1,1) ,dt.datetime.now() )
    df2=pd.DataFrame(stock_price_dict,index=date)
    df2=df2.tail(1)
    return df2
    
def Reformat_data(Lt_price , data):
    df3 =  pd.melt(Lt_price)
    df4 = pd.melt(data)
    merged = pd.merge(df3,df4,on='variable', how='outer')
    df5=merged.set_index('variable')
    df5=df5.rename(columns={"variable":"Stock Name","value_x": "Current Price","value_y":"purchase price"})
#    print(df5)
    return df5

def plot_graph(Stock_df):
    ax=Stock_df.plot(kind='bar',color=['g','r'])
    ax.set(xlabel='Stocks', ylabel='Price')
    plt.title('Stocks Comparisons')
    plt.show()

def Stock_analysis(Stock_df):
#    Stock_df['Stock_diff'] = Stock_df[['Current Price', 'purchase price']].sub(axis=1)
    Stock_df['Stock_diff'] = Stock_df['Current Price'] - Stock_df['purchase price']
    print(Stock_df)

    Stock_df['positive'] = Stock_df['Stock_diff'] > 0
    Stock_df=Stock_df.ix[:,2:]
#    print(Stock_df)
    ax=Stock_df['Stock_diff'].plot(kind='bar',color=Stock_df.positive.map({True: 'g', False: 'r'}))
    ax.set(xlabel='Stocks', ylabel='Profit/Loss')
    plt.title('Stocks Snapshot')
    plt.show()
    

if __name__ == "__main__" :

    Lt_price=get_latest_price(stock)
    data=get_purchase_price(stock_price_dict)
    Stock_df = Reformat_data(Lt_price , data)
    plot_graph(Stock_df)
    
    Stock_df1 = Stock_analysis(Stock_df)
    
#    df2 = pd.melt(Lt_price)
#    df3 = pd.melt(data)
#    print(df2)
#    print(df3)

#    merged= pd.merge(df2,df3,on='variable', how='outer')
#    df=merged.set_index('variable')
#    df=df.rename(columns={"variable":"Stock Name","value_x": "Current Price","value_y":"purchase price"})

#    print(df)
#    ax=df.plot(kind='bar',color=['g','r'])
#    ax.set(xlabel='Stocks', ylabel='Price')
##    ax.legend_.remove()
##    ax.legend(loc='upper center', shadow=True)
#    plt.title('Stocks Comparisons')
#    plt.show()



    


    
     