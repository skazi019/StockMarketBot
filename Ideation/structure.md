# Structure of the Code

---

### Short description
> create a stock market bot that will fetch data from free apis(for now)
> on some time frame(1m, 5m, 10m, 1h etc) for some paticular scrip.
> Then apply some algorithm on this data to make decision whether to go long
> or short on the scrip. Then buy/sell based on the algorithm. Also, manage
> portfolio to check whether the stocks I have are ready to be sold for
> profit.

<br/>

### Classes and attributes
 - Algorithms
   - all the algorithms available
   - algorithms to identify stocks/options/futures to buy/short
   - methods to enter/exit the trade using algorithm
   - different classes for different algorithms
 - Portfolio
   - Funds available (PAPER TRADE)
   - stocks/options/futures owned
     - algorithm used
     - bought at time
   - P/L