from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    exponentiation = placeholders[0]
    modulo = placeholders[1]
    answers = get_file_output()
    if answers == ['8 8']:
        passed()
    else:
        failed("One of your answers isn't equal to 10!")
    if '**' in exponentiation:
        passed()
    else:
        failed("Check exponentiation. Did you use ** ?")
    if '%' in modulo:
        passed()
    else:
        failed("Check modulo. Did you use % ? ")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


