import pygal
import lxml
import requests
import json
import datetime

api_key = "65210ZZ38CVFIWM4"
#api docs https://www.alphavantage.co/documentation/
def getData(time_series, symbol, api_key):
    #Daily Time Series API Func
    #https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
    #TIME_SERIES = TIME_SERIES_DAILY
    #symbol = symbol 
    #apikey = api_key

    #Intraday Time Series API Func
    #https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
    #time_series = TIME_SERIES_INTRADAY
    #symbol = symbol
    #apikey = api_key
    #interval = interaval? api required interval 

    #Weekly Time Series API Func
    #https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo
    #time_series = TIME_SERIES_WEEKLY
    #symbol = symbol 
    #apikey = api_key 

    #Monthly Time Series API Func
    #https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=demo
    #time_series = TIME_SERIES_MONTHLY
    #symbol = symbol
    #apikey = api_key
    #create string
    
    ##STRING ADDITION NOT WORKING, probably doing it wrong 
    apistring = "https://www.alphavantage.co/query?function="
    if (time_series == 1):
        time_series = "TIME_SERIES_INTRADAY"
    elif (time_series == 2):
        time_series = "TIME_SERIES_DAILY"
    elif (time_series == 3):
        time_series = "TIME_SERIES_WEEKLY"
    elif (time_series == 4):
        time_series = "TIME_SERIES_MONTHLY"
    apistring = (apistring + (time_series + "&symbol=" + symbol))
    if (time_series == "TIME_SERIES_INTRADAY"):
        apistring += "&interval=30min"
    apistring = apistring + ("&apikey=" + api_key)
    
    
    print(apistring)
    data = requests.get(apistring).json()
    return data



#main    
do_program = True
while (do_program):
    print("Stock Data Visualizer\n======================")

    symbol = input("\nEnter the stock symbol are looking for: ")
    #check and see if symbol exist > error handling
    #probably just hit the api with a constant time_series value and input the requested symbol
    #see if we get a good respone

    print("\nChart Types\n==================\n1. Bar\n2. Line")
    chart_type = input("Enter the chart type you want (1 , 2):")
    #make sure it's 1 or 2, while loop > error handling
   
        

    print("\nSelect the Time Series of chart you want to Generate\n=================================================================")
    print("\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly")
    time_series = int(input("Enter the time series option (1, 2, 3, 4): "))
    if (time_series == 1):
        time = "Time Series (30min)"
    elif (time_series == 2):
        time = "Time Series (Daily)"
    elif (time_series == 3):
        time = "Weekly Time Series"
    elif (time_series == 4):
        time = "Monthly Time Series"
    # error check option picked > error handling


    start_date = input("Enter the start Date (YYYY-MM-DD):")  
    # error handling > check valid date in YYYY-MM-DD
    end_date = input("Enter the end Date (YYYY-MM-DD):")
    # error hadling > check valid date in YYYY-MM-DD and that it is after the start date
    apidata = getData(time_series,symbol,api_key)
    
    # variables for data transfer to lists.
    x = 0
    newdata = {}
    datedata = []
    opendata = []
    highdata =[]
    lowdata = []
    closeddata = []
    
    # for loop to transfer data from apidata dictionary to newdata dictionary and then transfer
    #   individual data to different lists.
    for key, value in apidata[time].items():
        datedata = list(apidata[time].keys())
        x+=1
        holder = {x : value}
        newdata.update(holder)
        opendata.append(newdata[x]['1. open'])
        highdata.append(newdata[x]['2. high'])
        lowdata.append(newdata[x]['3. low'])
        closeddata.append(newdata[x]['4. close'])
   
    # method to convert data in list to float for chart data.
    def convert(data):
        for i in range(0, len(data)):
            data[i] = float(data[i])
        return data
    

    # if statement to choose a line or bar chart and display onto default browser.
    if (chart_type == '1'):
        bar_chart = pygal.Bar(x_label_rotation = 70)
        bar_chart.title = ('Stock Data for ' + symbol + ": " + start_date + ' to ' + end_date)
        datedata.reverse()
        bar_chart.x_labels = datedata
        opendata.reverse()
        bar_chart.add('Open', convert(opendata)) 
        highdata.reverse()
        bar_chart.add('High',  convert(highdata))
        lowdata.reverse()
        bar_chart.add('Low',   convert(lowdata))
        closeddata.reverse()
        bar_chart.add('Close', convert(closeddata))
        bar_chart.render_in_browser() 
        pass
    if (chart_type == '2'):
        line_chart = pygal.Line(x_label_rotation = 70)
        line_chart.title = ('Stock Data for ' + symbol + ": " + start_date + ' to ' + end_date)
        datedata.reverse()
        line_chart.x_labels = datedata
        opendata.reverse()
        line_chart.add('Open', convert(opendata)) 
        highdata.reverse()
        line_chart.add('High',  convert(highdata))
        lowdata.reverse()
        line_chart.add('Low',   convert(lowdata))
        closeddata.reverse()
        line_chart.add('Close', convert(closeddata))
        line_chart.render_in_browser() 
        pass



    #after everything is pretty much toss it all in a while loop so user can re run a visualizaiton
    an = str(input("Do you want to check another stock?"))
    if (an == 'y' or an == 'Y'):
        continue
    else: 
        do_program = False