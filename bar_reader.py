

class BarReader:
    
    def __init__(self, raw_dataframe, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.dataframe_period = self._get_dataframe_between_start_and_end(raw_dataframe)
    
    def _get_dataframe_between_start_and_end(self, raw_dataframe):
        dataframe_period = raw_dataframe.loc[self.start_time:self.end_time]
        return dataframe_period
    
    def get_bars(self, columns)
        #Columns are for example Opening, Close etc
        return self.dataframe_period.columns(columns)
