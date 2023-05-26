import csv


def third_task(filepath: str) -> str:
    path_to_new_file = 'task2_3.csv'

    with open(filepath, 'r', newline='') as rfile:
        reader = csv.DictReader(rfile)

        with open(path_to_new_file, 'w', newline='') as wfile:
            fieldnames = list(reader.fieldnames)
            fieldnames.remove('Images')
            fieldnames.remove('Description')

            writer = csv.DictWriter(wfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                del row['Images']
                del row['Description']
                writer.writerow(row)
    return path_to_new_file


file = 'stage3_test.csv'
third_task(file)
