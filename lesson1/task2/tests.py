from test_helper import run_common_tests, failed, passed, get_file_output


def check_answer(studentanswer, answer):
    if studentanswer == answer:
        passed()
    else:
        failed("Did you uncomment the print statement?")

if __name__ == '__main__':
    run_common_tests()
    student_answer = get_file_output()[0]
    check_answer(student_answer, "and uncomment this one!")

