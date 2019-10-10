import pandas


class NasdaqOMXCsvReader:

    DOHLCV_columns = ["Date", "Opening price", "High price", "Low price", "Closing price", "Total volume"]
    DOHLCV_mapper = {"Date": "date", 
                     "Opening price": "open",
                     "High price": "high",
                     "Low price": "low",
                     "Closing price": "close",
                     "Total volume": "volume"}

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.raw_dataframe = self._read_to_pandas_dataframe()
        self.bars = self._get_DOHLCV_bars()
        self.bars.rename(columns=DOHLCV_mapper)

    def _read_to_pandas_dataframe(self):
        data = pandas.read_csv(self.csv_file, sep=';', header=1, decimal=',')
        # Drop last column, because it is empty
        data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)
        data = data.set_index(['Date'])
        return data 

    def _get_DOHLCV_bars(self):
        return self.raw_dataframe.columns(DOHLCV_columns)

