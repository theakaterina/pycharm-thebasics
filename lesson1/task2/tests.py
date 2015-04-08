from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def check_answer(student_answer, answer):
    if student_answer == answer:
        passed()
    else:
        failed("Did you uncomment the print statement?")

if __name__ == '__main__':
    run_common_tests()
    # test_answer_placeholders()       # TODO: uncomment test call
    student_answer = get_file_output()[0]
    check_answer(student_answer, "and uncomment this one!")

