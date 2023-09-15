import json

from Datapoint import Datapoint
from Metadata import Metadata

class FileHandler:
    def __init__(self, input_path, output_file) -> None:
        self.file_path = input_path
        self.output_file = output_file

    def extract_data(self) -> (Metadata, [Datapoint]):
        data = self.load_data()
        meta_data: Metadata = Metadata(data['turbine'], data['power_unit'])
        data_points: [Datapoint] = list(map(lambda x: Datapoint(x['timestamp'], x["value"]), data['timeseries']))
        return meta_data, data_points

    def load_data(self) -> dict:
        with open(self.file_path, 'r') as f:  data = json.load(f)
        return data

    def save(self, data):
        with open(self.output_file, 'w') as f: json.dump(data, f)
