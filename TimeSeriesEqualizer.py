from collections import defaultdict

from Datapoint import Datapoint
from TimeHelper import TimeHelper as TH

class TimeSeriesEqualizer:
    def __init__(self, data_points: [Datapoint]):
        self.load_data_points(data_points)

    def load_data_points(self, data_points: [Datapoint]):
        self.data_points = data_points
        self.data_points.sort()        

    def get_range_buckets(self) -> dict:
        buckets = defaultdict(list)
        for dp in self.data_points:
            bucket_start_time = TH.closest_half_hour(dp.timestamp)
            buckets[bucket_start_time].append(dp)
            if dp.value is None: break
            # debug trace states
            TH.pretty_print(bucket_start_time, dp)
        return buckets
    
    def calculate_interval_value(self, previous_data_point: Datapoint, curr_point: Datapoint) -> float:
        minutes = (curr_point.timestamp - previous_data_point.timestamp) / 1000 / 60
        return minutes / 30 * previous_data_point.value
    
    def datapoint_with_none_value(self, intervals: [Datapoint]) -> bool:
        return any(i.value is None for i in intervals)
    
    def first_bucket_first_and_non_starting_point(self, minutes: int, index: int) -> bool:
        return minutes > 0 and index == 0
    
    def last_interval_one_datapoint(self, B, i, intervals):
        return len(intervals) == 1 and i == B - 1  

    def invalid_interval(self, intervals: [Datapoint], minutes: int, i: int, buckets_len: int) -> bool:
        return  self.datapoint_with_none_value(intervals) \
                or self.first_bucket_first_and_non_starting_point(minutes, i) \
                or self.last_interval_one_datapoint(buckets_len, i, intervals)

    def granulate_buckets(self, buckets: dict) -> [dict]:
        bucket_times, result = sorted(buckets), []

        for i, bucket_start_time in enumerate(bucket_times):
            intervals = buckets[bucket_start_time]
            
            minutes = TH.minute_gap(intervals[0].timestamp, bucket_start_time) 
            
            if self.invalid_interval(intervals, minutes, i, len(bucket_times)): continue

            curr = {'timestamp': bucket_start_time, 'value': 0}

            if minutes > 0: curr['value'] += minutes / 30 * buckets[bucket_times[i-1]][-1].value

            for i, curr_point in enumerate(intervals): curr['value'] += self.calculate_interval_value(intervals[max(0, i-1)], curr_point)

            curr['value'] += (30 - TH.minute_gap(intervals[-1].timestamp, bucket_start_time)) / 30 * intervals[-1].value
                                    
            result.append(curr)
        return result
    
    def duplicate_check(self):
        seen = set()
        for data_point in self.data_points:
            if data_point.timestamp in seen: raise Exception('Duplicate datapoint found')
            seen.add(data_point.timestamp)

    def equalize(self) -> dict:
        self.duplicate_check()
        return self.granulate_buckets(self.get_range_buckets())
