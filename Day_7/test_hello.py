# This is a test file for hello.py, using the pytest library.
# Why: instead of manually running the program and checking the output
# by eye, pytest lets us write checks (assertions) that run automatically
# and tell us instantly if something breaks.

from hello import hello


# Checks that calling hello() with no name still gives the default greeting.
def test_default():
    assert hello() == "hello, world"

# Checks that hello() works correctly for several different names.
# Why: looping over a list lets us test multiple cases without
# repeating the same assert line over and over.
def test_argument():
    for name in ["Apil", "Soni", "Neupane"]:
        assert hello(name) == f"hello, {name}"

