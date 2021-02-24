import sys


def csv_extractor():
    fn = sys.argv[1]
    column_number = sys.argv[2]

    with open(fn, 'r') as f:
        new_fn = f.readline().split(',')[int(column_number) - 1]
        with open(new_fn + '_' + fn, 'w') as new_f:
            for line in f:
                new_f.write(line.split(',')[int(column_number) - 1] + '\n')


if __name__ == '__main__':
    csv_extractor()
