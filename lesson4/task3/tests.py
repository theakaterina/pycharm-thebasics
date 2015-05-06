from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    answer1 = placeholders[0]
    answer2 = placeholders[1]
    answer3 = placeholders[2]
    answer4 = placeholders[3]
    answer5 = placeholders[4]
    if answer1 == "\"yellow\"":
        passed()
    else:
        failed("There is something wrong with answer1")
    if answer2 == "\"indigo\"":
        passed()
    else:
        failed("There is something wrong with answer2")
    if answer3 == "7":
        passed()
    else:
        failed("There is something wrong with answer3")
    if answer4 == "[\"red\", \"orange\", \"yellow\"]":
        passed()
    else:
        failed("There is something wrong with answer4")
    if answer5 == "colours[::3]" or answer5 == "colours[0::3]" or answer5 == "colours[0:7:3]":
        passed()
    else:
        failed("There is something wrong with answer5")

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


