import pandas
from asset_finder import AssetFinder

class NasdaqOMXCsvReader:

    NASDAQ_OMX_CSV_DIRECTORY = "../data/nasdaq-omx-csv"
    DOHLCV_COLUMNS = ["Date", "Opening price", "High price", "Low price", "Closing price", "Total volume"]
    DOHLCV_MAPPER = {"Date": "date", 
                     "Opening price": "open",
                     "High price": "high",
                     "Low price": "low",
                     "Closing price": "close",
                     "Total volume": "volume"}

    def __init__(self, assets):
        self.assets = assets
        self.assets_csv_files = AssetFinder(self.assets).find_assets_csv_files(NASDAQ_OMX_CSV_DIRECTORY)

    def _read_to_pandas_dataframe(self, csv_file):
        data = pandas.read_csv(csv_file, sep=';', header=1, decimal=',')
        # Drop last column, because it is empty
        data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)
        data = data.set_index(['Date'])
        return data 

    def _get_DOHLCV_bars(self):
        return self.raw_dataframe.columns(DOHLCV_COLUMNS)

    def get_asset_bars(self):
        assets_bars = {}
        
        for ticker, csv_file in self.assets_csv_files:
            asset_dataframe = self._read_to_pandas_dataframe(csv_file)
            asset_bars = self._get_DOHLCV_bars()
            # Rename the bars to be consistent with everything else
            asset_bars.rename(columns=DOHLCV_MAPPER)
            assets_bars[ticker] = asset_bars

        return assets_bars




            


