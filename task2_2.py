import csv


def second_task(filepath):
    path_to_new_file = 'task2_2.csv'

    with open(filepath, 'r', newline='') as rfile:
        reader = csv.reader(rfile)
        headers = next(reader, None)

        with open(path_to_new_file, 'w', newline='') as wfile:
            writer = csv.writer(wfile)
            if headers:
                writer.writerow(headers)
            for row in reader:
                if 50000 > float(row[4]) > 10000:
                    writer.writerow(row)

second_task('stage3_test.csv')