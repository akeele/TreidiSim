import os

class AssetFinder:

    def __init__(self, assets):
        self.assets = assets

    def find_assets_csv_files(self, csv_directory):
        assets_csv_files = {}
        
        csv_files = os.listdir(csv_directory)
        csv_tickers = [filename.split(".")[0] for filename in csv_files]
        #csv_files = [os.path.join(csv_directory, filename) for filename in csv_files]
        
        for asset in self.assets:
            if asset.ticker in csv_tickers:
                filename = asset.ticker + ".csv"
                assets_csv_files[asset.ticker] = os.path.join(csv_directory, filename)

        return assets_csv_files
