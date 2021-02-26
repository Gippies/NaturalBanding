import sys

import jenkspy


def natural_banding():
    fn = sys.argv[1]
    num_of_breaks = int(sys.argv[2])

    input_list = []
    with open(fn, 'r') as f:
        for line in f:
            input_list.append(float(line))
    print(jenkspy.jenks_breaks(input_list, num_of_breaks))


if __name__ == "__main__":
    natural_banding()
