from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "\"Hello World!\"":
        passed()
    elif placeholder == "'\Hello World!\'":
        passed()
    elif placeholder == "Hello World!":
        failed("Have you put quotation marks around the words?")
    else:
        failed("Make sure the capitalization and punctuation is exactly the same as the example")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


