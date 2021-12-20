import numpy as np
from numpy.core.fromnumeric import repeat
import pandas as pd
pd.set_option('mode.chained_assignment', None)

def simpleMovingAverage(scrip_df, ma):
        """
            This is a function to backtest the Simple Moving Average trading strategy.
            Condition 1: Buy when close price goes above the moving average
            Condition 2: Sell when close price goes below the moving average

            Input: A dataframe with date as index and Close prices of one scrip; moving average
            taken as input from the user

            Output: Based on the conditions above we output
            Number of Trades taken, Total Profit/Loss, Mean Return, and Profit Factor for the scrip
            in question
        """

        sma_col = str(ma)+'_SMA' # making the SMA col 
        scrip_df.dropna(inplace=True) # Wyeth had null values

        scrip_df[sma_col] = scrip_df['close'].rolling(window = ma, min_periods = ma).mean()
        scrip_df['Signal'] = 0.0
        scrip_df['Signal'] = np.where(scrip_df['close'] > scrip_df[sma_col], 1.0, 0.0) # applying the strategy rules
        scrip_df['Position'] = scrip_df['Signal'].diff() # Creating a column to identify when did we buy and sell
        
        scrip_df = scrip_df[(scrip_df['Position'] == 1) | (scrip_df['Position'] == -1)] # 1 : Buy ; -1 : Sell
        scrip_df['Position'] = scrip_df['Position'].apply(lambda x: 'Buy' if x == 1 else 'Sell')
        scrip_df['Returns'] = scrip_df['close'].diff()
        
        for index,row in scrip_df.iterrows():
            if row['Position'] == 'Buy':
                scrip_df.loc[index, 'Returns'] = 0
        
        num_of_trades = len(scrip_df[scrip_df['Position'] == 'Sell'])
        total_pl = sum(scrip_df['Returns'])
        mean_return = scrip_df[scrip_df['Position'] == 'Sell']['Returns'].mean()
        profit_factor = (sum(scrip_df[scrip_df['Returns'] > 0]['Returns']) / abs(sum(scrip_df[scrip_df['Returns'] < 0]['Returns'])))

        return [num_of_trades, total_pl, mean_return, profit_factor]

if __name__ == '__main__':

    print("Please enter the moving average value:")
    ma = int(input())

    main_data = pd.read_csv("./close_price.csv")
    main_data.set_index('TRADING_DATE', inplace=True)
    
    all_scrip_data = []

    # Iterating through all the scrips that are represented as columns
    for col in main_data.columns:
        ind_scrip_df = main_data[[col]]
        ind_scrip_df.columns = ['close']
        scrip_data = simpleMovingAverage(ind_scrip_df, ma)
        scrip_data.insert(0, col)
        all_scrip_data.append(scrip_data)

    all_scrip_df = pd.DataFrame(all_scrip_data, columns=['Scrip', 'Number of Trades', 'Total P/L', 'Mean Return', 'Profit Factor'])
    print(all_scrip_df)
    print(''.join(np.repeat('=', 40)))
    print("Portfolio Level:")
    print(f"Total number of trades: {sum(all_scrip_df['Number of Trades'])}")
    print(f"Total P/L: {sum(all_scrip_df['Total P/L'])}")
    print(f"Mean Return: {all_scrip_df['Mean Return'].mean()}")
    print(f"Profit factor: {(sum(all_scrip_df[all_scrip_df['Total P/L'] > 0]['Total P/L']) / abs(sum(all_scrip_df[all_scrip_df['Total P/L'] < 0]['Total P/L'])))}")
    print(''.join(np.repeat('=', 40)))
    