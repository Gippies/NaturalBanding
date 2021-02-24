import jenkspy


def jenks_test(test_input_list, num_of_bands):
    return jenkspy.jenks_breaks(test_input_list, num_of_bands)


def josh_test(test_input_list, num_of_bands):
    diff_list = []
    test_input_list = sorted(test_input_list)

    for i in range(len(test_input_list)):
        if i + 1 < len(test_input_list):
            diff_list.append((i, test_input_list[i + 1] - test_input_list[i]))

    return diff_list


def main():
    test_list = [5100, 5000, 4900, 4750, 2000, 1800, 1500, 1200, 500, 499, 10, 0]
    print(jenks_test(test_list, 4))
    print(josh_test(test_list, 4))


if __name__ == "__main__":
    main()
