import re
import csv
import urllib.request

url = f"https://grader.eecs.jacobs-university.de/courses/350112/python/csv/exp200807.csv"
local_file = f"wdata.csv"
urllib.request.urlretrieve(url, local_file)

input_file = "wdata.csv"
output_file = "wdata3.csv"

pattern = r"(15\.07\.\d{2}),(\d{2}:\d{2}),(.+),(.+),(.+),(.+),(.+),(.+)"
replacement = r"15.07.22,\2,\3,\4,\5,\6,\7,\8"

with open(input_file, "r") as file:
    data = file.read()

modified_data = re.sub(pattern, replacement, data)

with open(output_file, "w", newline="") as file:
    file.write(modified_data)
