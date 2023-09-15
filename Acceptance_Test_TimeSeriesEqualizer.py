from unittest import TestCase as TC, main
from TimeSeriesEqualizer import TimeSeriesEqualizer
from FileHandler import FileHandler
from Datapoint import Datapoint


class TestTimeSeriesEqualizer(TC):

    # use case 1
    def test_case_1(self):
        data_points: [Datapoint] = FileHandler('test-data/input-1', '').get_data_points()
        timeseries = TimeSeriesEqualizer(data_points).equalize()
        expected_timeseries = []
        self.assertEqual(timeseries, expected_timeseries, 'Test case 1 failed')

    # use case 2
    def test_case_2(self):
        data_points: [Datapoint] = FileHandler('test-data/input-2', '').get_data_points()
        timeseries = TimeSeriesEqualizer(data_points).equalize()
        expected_timeseries = [{"timestamp": 1581609600000, "value": 0.2}, { "timestamp": 1581611400000, "value": 3.0}, {"timestamp": 1581613200000, "value": 9.0}]
        self.assertEqual(timeseries, expected_timeseries, 'Test case 2 failed')

    # use case 3
    def test_case_3(self):
        data_points: [Datapoint] = FileHandler('test-data/input-3', '').get_data_points()
        timeseries = TimeSeriesEqualizer(data_points).equalize()
        expected_timeseries = [{"timestamp": 1581609600000, "value": 8.0}, {"timestamp": 1581611400000, "value": 32.0}]
        self.assertEqual(timeseries, expected_timeseries, 'Test case 3 failed')

    # use case 4
    def test_case_4(self):
        data_points: [Datapoint] = FileHandler('test-data/GranularityOperations_Input', '').get_data_points()
        timeseries = TimeSeriesEqualizer(data_points).equalize()
        expected_timeseries = [{"timestamp": 1586901600000, "value": 7.34}, {"timestamp": 1586923200000, "value": 20.043}, {"timestamp": 1586939400000, "value": 24.031999999999996}, {"timestamp": 1586957400000, "value": 24.770266666666664}, {"timestamp": 1586959200000, "value": 32.000001}, {"timestamp": 1586962800000, "value": 31.318883999999997}, {"timestamp": 1586966400000, "value": 30.2}, {"timestamp": 1586977200000, "value": 0.001}, {
            "timestamp": 1586993400000, "value": 0.0006}, {"timestamp": 1586995200000, "value": -0.00013333333333333334}, {"timestamp": 1586998800000, "value": 2.0}, {"timestamp": 1587002400000, "value": 2.5}, {"timestamp": 1587006000000, "value": 3.3}, {"timestamp": 1587009600000, "value": 4.4}, {"timestamp": 1587013200000, "value": 5.5}, {"timestamp": 1587016800000, "value": 6.6}, {"timestamp": 1587020400000, "value": 7.7}, {"timestamp": 1587056400000, "value": 0.0}]
        self.assertEqual(timeseries, expected_timeseries, 'Test case 4 failed')


if __name__ == '__main__':
    main()
