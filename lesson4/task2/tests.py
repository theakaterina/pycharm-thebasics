from test_helper import run_common_tests, check_answer


if __name__ == '__main__':
    run_common_tests()
    doubles = ['[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]']
    check_answer(doubles, "You didn't return a list of doubles")