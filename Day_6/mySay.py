# sys gives us access to command-line arguments (sys.argv)
import sys

# Reusing the hello and goodbye functions defined in sayings.py
from sayings import hello
from sayings import goodbye

# sys.argv[0] is the script name, sys.argv[1] would be the name typed after it
# so only greet if the user typed exactly one extra argument
if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])