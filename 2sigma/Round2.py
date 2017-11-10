import datetime


#When visualizing market data over a long period of time, it is often helpful to build an Open-high-low-close (OHLC) chart.
#However, to build an OHLC chart you first need to prepare some data. For each financial instrument consider each day when
#it was traded, and find the following prices the instrument had that day:

#open price: the price of the first trade of the day;
#high price: the highest trade of the day;
#low price: the lowest trade of the day;
#close price: the price of the last trade of the day.
#Given a stream of trade data ordered by time, write a program to compute the OHLC by day and instrument
#(see output section for the format details).
#If two trades happen to have equal timestamps, then their order is determined by the order of their timestamps in
#the timestamp array.

#Example

#For

timestamp = [1450625399, 1450625400, 1450625500,
            1450625550, 1451644200, 1451690100, 1451691000]
instrument = ["HPQ", "HPQ", "HPQ", "HPQ", "AAPL", "HPQ", "GOOG"]
side = ["sell", "buy", "buy", "sell", "buy", "buy", "buy"]
price = [10, 20.3, 35.5, 8.65, 20, 10, 100.35]# and
size = [10, 1, 2, 3, 5, 1, 10]#, the output should be

#dailyOHLC(timestamp, instrument, side, price, size) =
#[["2015-12-20", "HPQ", "10.00", "35.50", "8.65", "8.65"],
#["2016-01-01", "AAPL", "20.00", "20.00", "20.00", "20.00"],
# ["2016-01-01", "GOOG", "100.35", "100.35", "100.35", "100.35"],
# ["2016-01-01", "HPQ", "10.00", "10.00", "10.00", "10.00"]]




def getDay(UnixTime):
    return datetime.datetime.fromtimestamp(UnixTime).strftime('%Y-%m-%d')



def dailyOHLC(timestamp, instrument, side, price, size):
    instrDict = {}
    opList = []
    sK = []
    for t in range(len(timestamp)):
        Key = (instrument[t] ,getDay(timestamp[t]))
        if Key in instrDict.keys():
            instrDict[Key].append(price[t])
        else :
            instrDict[Key] = []
            instrDict[Key].append(price[t])
    #sorted(yourlst, key=lambda t: (abs(t[0] - t[1])), t[0]), reverse=True)

    sK = sorted(instrDict.keys(), key=lambda x: (x[1], x[0]))

    for k in sK:
        tempList = []
        tempList.append(k[1])
        tempList.append(k[0])
        Open = "%.2f" % round(instrDict[k][0],2)
        High = "%.2f" % round(max(instrDict[k]),2)
        Low = "%.2f" % round(min(instrDict[k]),2)
        endInd = len(instrDict[k]) - 1
        Close = "%.2f" % round(instrDict[k][endInd],2)


        tempList.append(Open)
        tempList.append(High)
        tempList.append(Low)
        tempList.append(Close)
        opList.append(tempList)

    return opList

print(dailyOHLC(timestamp, instrument, side, price, size))






