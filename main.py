import jenkspy


def jenks_test(test_input):
    return jenkspy.jenks_breaks(test_input, 4)


def josh_test(test_input):
    pass


def main():
    test_list = [5100, 5000, 4900, 4750, 2000, 1800, 1500, 1200, 500, 499, 10, 0]
    print(jenks_test(test_list))


if __name__ == "__main__":
    main()
