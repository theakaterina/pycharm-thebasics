from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    print placeholders
    name = placeholders[0]
    age = placeholders[1]
    likes_cake = placeholders[2]

    if isinstance(name, str):
        passed()
    else:
        failed("Something is wrong with your name. Did you remember to put quotation marks around it?")

    if '.' in age:
        failed("Ints are whole numbers, putting a decimal point in makes it a float.")
    else:
        try:
            int(age)
            passed()
        except ValueError:
            failed("Something is wrong with your age. Ints should not have quotation marks around them")

    if likes_cake == "True":
        passed()
    elif likes_cake == "False":
        passed()
    else:
        failed("Something is wrong with likes_cake. "
               "True and False should have capital letters and be written without quotation marks")

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()