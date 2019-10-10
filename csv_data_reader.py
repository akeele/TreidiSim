import pandas
import os
from asset_finder import AssetFinder


class NasdaqOMXCsvReader:

    NASDAQ_OMX_CSV_DIRECTORY = "data/nasdaq-omx-csv"
    DOHLCV_COLUMNS = ["Date", "Opening price", "High price", "Low price", "Closing price", "Total volume"]
    DOHLCV_MAPPER = {"Date": "date", 
                     "Opening price": "open",
                     "High price": "high",
                     "Low price": "low",
                     "Closing price": "close",
                     "Total volume": "volume"}

    def __init__(self, assets=None, all_assets=False):
        self.all_assets = all_assets
        if self.all_assets == True:                                                                                                                                 self.assets_csv_files = self._get_all_csv_files()
        else:
            self.assets = assets
            self.assets_csv_files = AssetFinder(self.assets).find_assets_csv_files(self.NASDAQ_OMX_CSV_DIRECTORY)  
    
    def _get_all_csv_files(self):
        csv_files = os.listdir(self.NASDAQ_OMX_CSV_DIRECTORY)
        tickers = [filename.split(".")[0] for filename in csv_files]
        csv_files = [os.path.join(self.NASDAQ_OMX_CSV_DIRECTORY, filename) for filename in csv_files]

        assets_csv_files = dict(zip(tickers, csv_files))
        return assets_csv_files

    def _read_to_pandas_dataframe(self, csv_file):
        data = pandas.read_csv(csv_file, sep=';', header=1, decimal=',')
        # Drop last column, because it is empty
        data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)
        return data 

    def _get_DOHLCV_bars(self, asset_dataframe):
        dohlcv_bars = asset_dataframe[self.DOHLCV_COLUMNS]
        return dohlcv_bars

    def get_assets_bars(self):
        assets_bars = {}
        for ticker, csv_file in self.assets_csv_files.items():
            asset_dataframe = self._read_to_pandas_dataframe(csv_file)
            asset_bars = self._get_DOHLCV_bars(asset_dataframe)
            
            # Rename the bars to be consistent with everything else
            asset_bars = asset_bars.rename(columns=self.DOHLCV_MAPPER)
            # Sort by ascending date
            asset_bars['date'] = pandas.to_datetime(asset_bars['date'])
            asset_bars = asset_bars.sort_values(by='date')
            assets_bars[ticker] = asset_bars

        return assets_bars




            


