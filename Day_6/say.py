import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
else:
    cowsay.cow("Enter your real name!!!")