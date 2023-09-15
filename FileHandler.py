import json

from Datapoint import Datapoint
from Metadata import Metadata

class FileHandler:
    def __init__(self, input_path: str, output_file: str) -> None:
        self.file_path = input_path
        self.output_file = output_file
        data = self.load_data()
        self.meta_data: Metadata = Metadata(data['turbine'], data['power_unit'])
        self.data_points: [Datapoint] = list(map(lambda x: Datapoint(x['timestamp'], x["value"]), data['timeseries']))

    def get_meta_data(self) -> Metadata:
        return self.meta_data

    def get_data_points(self) -> [Datapoint]:
        return self.data_points

    def load_data(self) -> dict:
        with open(self.file_path, 'r') as f:  data = json.load(f)
        return data

    def save(self, data) -> None:
        with open(self.output_file, 'w') as f: json.dump(data, f)
