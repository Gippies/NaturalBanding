import sys
from statistics import median, mean

import jenkspy


def josh_natural_banding(test_input_list, num_of_bands):
    diff_list = []
    test_input_list = sorted(test_input_list)

    for i in range(len(test_input_list)):
        if i + 1 < len(test_input_list):
            diff_list.append((i, test_input_list[i + 1] - test_input_list[i]))

    sorted_diff_list = sorted(diff_list, key=lambda x: x[1], reverse=True)

    diff_diff = sorted_diff_list[0][1] - sorted_diff_list[len(sorted_diff_list) - 1][1]
    diff_only_list = [x for _, x in diff_list]
    if diff_diff >= mean(diff_only_list) or diff_diff >= median(diff_only_list):
        print("Using Josh Algorithm...")
        sorted_diff_list = sorted_diff_list[:num_of_bands - 1]
        high_diff_index_list = [x for x, _ in sorted_diff_list]

        results_list = []
        for index in high_diff_index_list:
            results_list.append(test_input_list[index])

        results_list = sorted(results_list)
        return results_list
    else:
        print("Using Fisher-Jenks Algorithm...")
        return jenkspy.jenks_breaks(test_input_list, num_of_bands)


def main():
    input_list = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            input_list.append(float(line))
    print(josh_natural_banding(input_list, int(sys.argv[2])))
    print(jenkspy.jenks_breaks(input_list, int(sys.argv[2])))


if __name__ == "__main__":
    main()
