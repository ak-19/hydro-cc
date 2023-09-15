from sys import argv
from FileHandler import FileHandler
from TimeSeriesEqualizer import TimeSeriesEqualizer


def main(input_path, output_path):
    print(f'Loading from: {input_path}')
    file_handler = FileHandler(input_path, output_path)
    meta_data, data_points = file_handler.extract_data()
    timeseries = TimeSeriesEqualizer(data_points).equalize()
    file_handler.save({
        "turbine": meta_data.turbine,
        "power_unit": meta_data.power_unit,
        "timeseries": timeseries
    })


if __name__ == '__main__':
    main(argv[1], argv[2])
