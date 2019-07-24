import os
import png
import PythonMagick
import argparse
from path_type import PathType

# Magick Constants
TRANSPARENT_BACKGROUND = "transparent"
CENTER = "center"

# Image sizes
BOBBLEHEADS_LARGE_SIZE = ""
BOBBLEHEADS_SIZE = "84x138"
HALFBODY_LARGE_LARGE_SIZE = ""
HALFBODY_LARGE_SIZE = "312x250"
HALFBODY_SMALL_LARGE_SIZE = "176x134"
HALFBODY_SMALL_SIZE = "110x84"
MINI_LARGE_SIZE = ""
MINI_SIZE = "30x30"
UNITCARD_LARGE_SIZE = ""
UNITCARD_SIZE = "82x272"


def main():
    pass


# takes a folder with base 5 large version of the required images and populates the target folder correctly
def build_and_populate():
    composite = "head.png"
    bobbleheads_large = "bobbleheads_large.png"
    halfbody_large_large = "halfbody_large_large.png"
    mini_large = "mini_large.png"
    unitcard_large = "unitcard_large.png"

    bobbleheads = "bobbleheads.png"
    halfbody_large = "halfbody_large.png"
    halfbody_small_large = "halfbody_small_large.png"
    halfbody_small = "halfbody_small.png"
    mini = "mini.png"
    unitcard = "unitcard.png"

    composite_file = os.join(args.source_dir, composite)
    bobbleheads_large_file = os.join(args.source_dir, bobbleheads_large)
    halfbody_large_large_file = os.join(args.source_dir, halfbody_large_large)
    mini_large_file = os.join(args.source_dir, mini_large)
    unitcard_large_file = os.join(args.source_dir, unitcard_large)

    bobbleheads_file = os.join(args.source_dir, bobbleheads)
    halfbody_large_file = os.join(args.source_dir, halfbody_large)
    halfbody_small_large_file = os.join(args.source_dir, halfbody_small_large)
    halfbody_small_file = os.join(args.source_dir, halfbody_small)
    mini_file = os.join(args.source_dir, mini)
    unitcard_file = os.join(args.source_dir, unitcard)

    # create full set from starting 5 images
    bobbleheads_img = PythonMagick.Image(bobbleheads)
    bobbleheads_img.rezie(BOBBLEHEADS_SIZE)
    bobbleheads_img.backgroundCOLOR(TRANSPARENT_BACKGROUND)
    bobbleheads_img.gravity(CENTER)
    bobbleheads_img.extent(BOBBLEHEADS_SIZE)


def convert():
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Processes or converts image files around to create character folders')
    parser.add_argument("--source_dir", required=True, help="source folder", type=PathType)
    parser.add_argument("--target_dir", required=True, help="target folder", type=PathType)
    parser.add_argument("--character_folder", required=True, help="name used to create the target folder", type=str)
    parser.add_argument("--character_element", required=True, help="element of the character", type=str)
    parser.add_argument("--generic", help="this is a generic character",  action='store_true')
    parser.add_argument("--convert", help="switches mod to convert mode",  action='store_true')
    parser.add_argument("--verbose", help="enable debug logging",  action='store_true')
    args = parser.parse_args()
    main()












