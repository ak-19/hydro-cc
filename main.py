from sys import argv
from FileHandler import FileHandler
from Datapoint import Datapoint
from Metadata import Metadata
from TimeSeriesEqualizer import TimeSeriesEqualizer

def main(input_path: str, output_path: str) -> None:
    print(f'Loading from: {input_path}')
    file_handler = FileHandler(input_path, output_path)
    meta_data: Metadata = file_handler.get_meta_data()
    data_points: [Datapoint] = file_handler.get_data_points()
    timeseries = TimeSeriesEqualizer(data_points).equalize()
    file_handler.save({
        "turbine": meta_data.turbine,
        "power_unit": meta_data.power_unit,
        "timeseries": timeseries
    })


if __name__ == '__main__':
    main(argv[1], argv[2])
