from collections import defaultdict
from datetime import datetime
from Datapoint import Datapoint

class TimeSeriesEqualizer:
    def __init__(self, data_points: [Datapoint]):
        self.load_data_points(data_points)

    def load_data_points(self, data_points: [Datapoint]):
        self.data_points = data_points
        self.data_points.sort()        

    def closest_half_hour(self, timestamp: int) -> int:
        year = datetime.fromtimestamp(timestamp / 1000).year
        month = datetime.fromtimestamp(timestamp / 1000).month
        day = datetime.fromtimestamp(timestamp / 1000).day
        hours = datetime.fromtimestamp(timestamp / 1000).hour
        minutes = 0 if datetime.fromtimestamp(
            timestamp / 1000).minute < 30 else 30
        return int(datetime(year, month, day, hours, minutes, 0).timestamp() * 1000)

    def pretty_print(self, bucket_start_time, dp):
        prettty_time = datetime.fromtimestamp(
            dp.timestamp / 1000).strftime('%d/%m/%y %H:%M:%S')
        prettty_half_starttime = datetime.fromtimestamp(
            bucket_start_time / 1000).strftime('%d/%m/%y %H:%M:%S')
        print(prettty_time, ' belongs to ', prettty_half_starttime, ' carries value of',dp.value)

    def get_range_buckets(self) -> dict:
        buckets = defaultdict(list)

        for dp in self.data_points:
            if dp.timestamp is None or dp.value is None:
                break
            bucket_start_time = self.closest_half_hour(dp.timestamp)
            buckets[bucket_start_time].append(dp)
            # debug trace states
            # self.pretty_print(bucket_start_time, dp)

        return buckets
    
    def calculate_interval_value(self, previous_data_point: Datapoint, curr_point: Datapoint) -> float:
        minutes = (curr_point.timestamp - previous_data_point.timestamp) / 1000 / 60
        return minutes / 30 * previous_data_point.value

    def granulate_buckets(self, buckets: dict) -> [dict]:
        bucket_times, B, result = sorted(buckets), len(buckets), []

        for i in range(B):
            bucket_start_time = bucket_times[i]
            intervals = buckets[bucket_start_time]
            if len(intervals) < 2 and i == 0: continue

            minutes = (intervals[0].timestamp - bucket_start_time) / 1000 / 60
            if minutes > 0 and i == 0: continue

            curr = {'timestamp': bucket_start_time, 'value': 0}
            if minutes > 0:
                curr['value'] += minutes / 30 * buckets[bucket_times[i-1]][-1].value
            for i, curr_point in enumerate(intervals):
                curr['value'] += self.calculate_interval_value(intervals[max(0, i-1)], curr_point)
            curr['value'] += (30 - (intervals[-1].timestamp-bucket_start_time) / 1000 / 60) / 30 * intervals[-1].value
            result.append(curr)
        return result
    
    def duplicate_check(self):
        seen = set()
        for data_point in self.data_points:
            if data_point.timestamp in seen:
                raise Exception('Duplicate datapoint found')
            seen.add(data_point.timestamp)

    def equalize(self) -> dict:
        self.duplicate_check()
        return self.granulate_buckets(self.get_range_buckets())
