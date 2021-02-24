from collections import OrderedDict

import jenkspy


def jenks_test(test_input_list, num_of_bands):
    return jenkspy.jenks_breaks(test_input_list, num_of_bands)


def josh_test(test_input_list, num_of_bands):
    diff_dict = OrderedDict()
    test_input_list = sorted(test_input_list)

    for i in range(len(test_input_list)):
        if i + 1 < len(test_input_list):
            diff_dict[i] = test_input_list[i + 1] - test_input_list[i]

    diff_list = sorted(diff_dict.items(), key=lambda x: x[1], reverse=True)
    diff_list = diff_list[:num_of_bands - 1]

    high_diff_index_list = [x for x, _ in diff_list]

    results_list = []
    for index in high_diff_index_list:
        results_list.append(test_input_list[index])

    results_list = sorted(results_list)
    return results_list


def main():
    test_list = [5100, 5000, 4900, 4750, 2000, 1800, 1500, 1200, 500, 499, 10, 0]
    print(jenks_test(test_list, 4))
    print(josh_test(test_list, 4))


if __name__ == "__main__":
    main()
