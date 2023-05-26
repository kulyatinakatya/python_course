import csv


def first_task(filepath: str) -> str:
    path_to_new_file = 'task2_1.csv'

    with open(filepath, 'r', newline='') as rfile:
        reader = csv.DictReader(rfile)

        with open(path_to_new_file, 'w', newline='') as wfile:
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(wfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                if len(row['Images'].split(',')) > 3:
                    writer.writerow(row)
    return path_to_new_file


file = 'stage3_test.csv'
first_task(file)
