import urllib.request

month = int(input(""))

url = f"https://grader.eecs.jacobs-university.de/courses/350112/python/csv/exp2008{month:02d}.csv"
local_file = f"wdata1.csv"

urllib.request.urlretrieve(url, local_file)
