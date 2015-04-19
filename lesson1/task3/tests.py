from test_helper import run_common_tests, failed, passed, get_file_output


def correct_answer(answer):
    if answer == ["233168"]:
        passed()
    else:
        failed("Some of your indents are not correct. Check again!")

if __name__ == '__main__':
    run_common_tests()
    correct_answer(get_file_output())




