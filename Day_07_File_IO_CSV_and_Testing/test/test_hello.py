# Another test file for hello.py, placed inside its own "test" folder.
# Why: pytest can discover tests placed in subfolders too, which is
# a common way to keep tests organized as a project grows.

from hello import hello

# Checks the default greeting when no name is passed in.
def test_default():
    assert hello() == "hello, world"

# Checks the greeting when a specific name is passed in.
def test_argument():
    assert hello("Apil") == "hello, Apil"