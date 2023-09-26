from datetime import datetime

class TimeHelper:
    @staticmethod
    def closest_half_hour(timestamp: int) -> int:
        year = datetime.fromtimestamp(timestamp / 1000).year
        month = datetime.fromtimestamp(timestamp / 1000).month
        day = datetime.fromtimestamp(timestamp / 1000).day
        hours = datetime.fromtimestamp(timestamp / 1000).hour
        minutes = 0 if datetime.fromtimestamp(timestamp / 1000).minute < 30 else 30
        return int(datetime(year, month, day, hours, minutes, 0).timestamp() * 1000)
    
    @staticmethod
    def pretty_print(start_datapoint, curr_datapoint):
        prettty_time = datetime.fromtimestamp(curr_datapoint.timestamp / 1000).strftime('%d/%m/%y %H:%M:%S')
        prettty_half_starttime = datetime.fromtimestamp(start_datapoint / 1000).strftime('%d/%m/%y %H:%M:%S')
        print(prettty_time, ' belongs to ', prettty_half_starttime, ' carries value of',curr_datapoint.value)  

    @staticmethod
    def pretty_print_timestamp(timestamp):
        prettty_time = datetime.fromtimestamp(timestamp / 1000).strftime('%d/%m/%y %H:%M:%S')
        print(prettty_time)

    @staticmethod
    def minute_gap(second_timestamp: int, first_timestamp: int) -> int:
        return (second_timestamp - first_timestamp) / 1000 / 60