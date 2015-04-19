from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output
from math import pi


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    radius = placeholders[0]
    formula = placeholders[1]
    if radius == "5":
        passed()
    else:
        failed("The radius of the circle should be 5")
    if "pi" in formula:
        passed()
    else:
        failed()


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()
    answer = pi * 25
    if get_file_output() == [str(answer)]:
        passed()
    else:
        failed("Something is wrong with your formula")


