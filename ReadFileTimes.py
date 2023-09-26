from sys import argv
import json 
from TimeHelper import TimeHelper as TH

def main(file_path: str) -> None:
    with open(file_path, 'r') as f:  data = json.load(f)
    for ts in data["timeseries"]:
        timestamp = ts["timestamp"]
        TH.pretty_print_timestamp(timestamp)

if __name__ == '__main__': main(argv[1])