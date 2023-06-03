import urllib.request

url = "https://grader.eecs.jacobs-university.de/courses/350112/python/csv/exp200811.csv"
output_file = "wdata4.csv"

urllib.request.urlretrieve(url, output_file)

with open(output_file, "r+") as file:
    lines = file.readlines()
    lines[1] = "Modified the file with this text\n"
    file.seek(0)
    file.writelines(lines)

