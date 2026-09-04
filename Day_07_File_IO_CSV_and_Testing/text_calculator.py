# from calculator import square

# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 sqaured was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 sqaured was not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 sqaured was not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 sqaured was not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 sqaured was not 0")

# if __name__ == "__main__":
#     main()


# This is a test file for calculator.py, using the pytest library.
# Why: the commented-out code above was an earlier, manual way of testing
# using try/except and assert. It worked, but pytest does the same job
# more simply: each test_ function below runs on its own, and pytest
# reports which ones pass or fail automatically.

from calculator import square

# Checks that squaring positive numbers works correctly.
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

# Checks that squaring negative numbers still gives a positive result.
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

# Checks the edge case of squaring zero.
def test_zero():
    assert square(0) == 0
