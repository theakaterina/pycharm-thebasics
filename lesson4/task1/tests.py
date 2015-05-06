# Doesn't really test what I want

from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if '[' in placeholder:
        passed()
    else:
        failed("Use square brackets please!")

    if placeholder.count(',') >= 3:
        passed()
    else:
        failed("Please have at least four items in your list")

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


