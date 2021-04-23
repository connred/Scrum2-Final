import unittest
from datetime import datetime

symbol = input("Enter stock symbol: ")
chart_type = input("\nEnter 1 for Bar Chart or 2 for Line Chart: ")
print("\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly")
time_series = input("\nEnter the time series option (1, 2, 3, 4): ")
start_date = input("\nEnter start date in format of YYYY-MM-DD: ")
end_date = input("\nEnter end date in format of YYYY-MM-DD: ")

class UnitTest(unittest.TestCase):
    
    def test_symbol(self):
        self.assertTrue(symbol.isupper())
        self.assertTrue(symbol.isalpha())
        self.assertTrue(len(symbol) <= 7)
        
    def test_charttype(self):
        self.assertTrue(chart_type.isnumeric())
        self.assertTrue(chart_type == '1' or chart_type == '2')
        
    def test_timeseries(self):
        self.assertTrue(time_series.isnumeric())
        self.assertTrue(time_series == '1' or time_series == '2' or 
                       time_series == '3' or time_series == '4')
        
    def test_startdate(self):
        self.assertTrue(datetime.strptime(start_date, "%Y-%m-%d"))
        
    def test_enddate(self):
        self.assertTrue(datetime.strptime(end_date, "%Y-%m-%d"))    
        
if __name__ == '__main__':
    unittest.main()