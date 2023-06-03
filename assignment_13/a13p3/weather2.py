import csv
import urllib.request

url = f"https://grader.eecs.jacobs-university.de/courses/350112/python/csv/exp200803.csv"
local_file = f"wdata2.csv"
urllib.request.urlretrieve(url, local_file)


input_file = "wdata2.csv"
output_file = "wdata2_filtered.csv"

filtered_data = []

with open(input_file, "r") as file:
    reader = csv.reader(file)
    header = next(reader)  

    filtered_data = [row for row in reader if row[0].startswith("11.03.")]
    filtered_data = [[f"{row[0].split('.')[2]}-{row[0].split('.')[1]}-{row[0].split('.')[0]} {row[1]}", row[2], row[3], row[6], row[7]] for row in filtered_data]

with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Date Time", "Temperature", "Humidity", "Wind", "Direction"])
    writer.writerows(filtered_data)
