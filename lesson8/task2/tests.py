from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    integers = placeholders[0]
    floats = placeholders[1]
    if '.' in integers:
        failed()
    if '.' in floats:
        passed()
    else:
        failed()


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()

