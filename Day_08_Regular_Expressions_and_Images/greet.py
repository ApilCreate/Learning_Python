# sys gives us access to command-line arguments (sys.argv).
import sys

# PIL (Pillow) is a library for opening, editing, and saving images.
from PIL import Image

images=[]

# sys.argv is a list of the words typed on the command line, e.g.
# running "python greet.py greet.gif greet2.gif" gives
# sys.argv = ["greet.py", "greet.gif", "greet2.gif"].
# sys.argv[1:] slices off the script name (index 0), leaving just the
# image filenames the user passed in. Slicing with [1:] keeps a whole
# list; indexing with [1] would only grab one filename as a string,
# and looping over a string loops over its letters instead (the bug
# that was here before).
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# Build an animated GIF from the images we opened.
# - images[0] is the first frame, saved as the "base" file.
# - append_images adds the rest of the frames after it.
# - save_all=True tells Pillow to save every frame, not just the first.
# - duration=200 means each frame shows for 200 milliseconds.
# - loop=0 means the animation repeats forever.
images[0].save(
    "greeting.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)