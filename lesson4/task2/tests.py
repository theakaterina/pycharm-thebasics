# TODO replace x

from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == ("[x * 2 for x in L]" or "[x + x for x in L]"):
        passed()
    elif placeholder == ("[x*2 for x in L]" or "[x+x for x in L]"):
        passed()
    else:
        failed("Format should be [expression to double number for number in L]")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


