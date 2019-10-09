import pandas


class NasdaqOMXCsvReader:

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def read_to_pandas_dataframe(self):
        data = pandas.read_csv(self.csv_file, sep=';', header=1, decimal=',')
        # Drop last column, because it is empty
        data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)
        data = data.set_index(['Date'])
        return data, data.columns



