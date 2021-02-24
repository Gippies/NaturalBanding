from statistics import median, mean

import jenkspy


def josh_natural_banding(test_input_list, num_of_bands):
    diff_list = []
    test_input_list = sorted(test_input_list)

    for i in range(len(test_input_list)):
        if i + 1 < len(test_input_list):
            diff_list.append((i, test_input_list[i + 1] - test_input_list[i]))

    diff_list = sorted(diff_list, key=lambda x: x[1], reverse=True)

    diff_diff = diff_list[0][1] - diff_list[len(diff_list) - 1][1]
    if diff_diff >= mean(test_input_list) or diff_diff >= median(test_input_list):
        print("Using Josh Algorithm...")
        diff_list = diff_list[:num_of_bands - 1]
        high_diff_index_list = [x for x, _ in diff_list]

        results_list = []
        for index in high_diff_index_list:
            results_list.append(test_input_list[index])

        results_list = sorted(results_list)
        return results_list
    else:
        print("Using Fisher-Jenks Algorithm...")
        return jenkspy.jenks_breaks(test_input_list, num_of_bands)


def main():
    test_list = [5100, 5000, 4900, 4750, 2000, 1800, 1500, 1200, 500, 499, 10, 0]
    print(josh_natural_banding(test_list, 4))

    print()
    test_list_2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    print(josh_natural_banding(test_list_2, 4))

    print()
    test_list_3 = [0, 1000000, 2000000, 3000000]
    print(josh_natural_banding(test_list_3, 2))


if __name__ == "__main__":
    main()
