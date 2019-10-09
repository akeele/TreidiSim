

class BarReader:
    
    def __init__(self, raw_dataframe, start_time, end_time):
        self.raw_dataframe = raw_dataframe
        self.start_time = start_time
        self.end_time = end_time
        self.period_dataframe = self._get_dataframe_between_start_and_end(raw_dataframe)
    
    def _get_dataframe_between_start_and_end(self):
        period_dataframe = self.raw_dataframe.loc[self.start_time:self.end_time]
        return period_dataframe
    
    def get_bars(self, all_bars=False)
        #Columns are for example Opening, Close etc
        if all_bars == True:
            return self.raw_dataframe
        else:
            return self.period_dataframe
