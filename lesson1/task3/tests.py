from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    name = placeholders[0]
    age = placeholders[1]
    likes_cake = placeholders[2]

    if isinstance(name, str):
        passed()
    else:
        failed("Something is wrong with your name. Did you remember to put quotation marks around it?")

    if isinstance(age, int):
        passed()
    else:
        failed("Something is wrong with your age. ints have no quotation marks ")

if __name__ == '__main__':
    run_common_tests()
    # test_answer_placeholders()       # TODO: uncomment test call


