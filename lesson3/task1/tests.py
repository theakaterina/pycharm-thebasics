from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    addition = placeholders[0]
    subtraction = placeholders[1]
    multiplication = placeholders[2]
    division = placeholders[3]
    answers = get_file_output()
    if answers == ['(10, 10, 10, 10)']:
        passed()
    else:
        failed("One of your answers isn't equal to 10!")
    if '+' in addition:
        passed()
    else:
        failed("Check your addition. Did you use + ?")
    if '-' in subtraction:
        passed()
    else:
        failed("Check your subtraction. Did you use - ? ")
    if '*' in multiplication:
        passed()
    else:
        failed("Check your multiplication. Did you use * ?")
    if '/' in division:
        passed()
    else:
        failed("Check your division. Did you use / ?")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()