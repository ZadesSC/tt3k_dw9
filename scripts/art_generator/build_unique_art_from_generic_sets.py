#!/usr/bin/env python3

########################################################################################################################
# This script is used to build unique portrait sets from generics provided by CA
########################################################################################################################

import png
import sys
import argparse
from path_type import PathType
from PIL import Image
from pathlib import Path

# Subdirectory names
COMPOSITES_DIR = "composites"
STILLS_DIR = "stills"
BOBBLEHEADS_DIR = "bobbleheads"
HALFBODY_LARGE_DIR = "halfbody_large"
HALFBODY_SMALL_DIR = "halfbody_small"
MINI_DIR = "mini"
UNITCARDS_DIR = "unitcards"
LARGE_PANEL_DIR = "large_panel"
SMALL_PANEL_DIR = "small_panel"
FACES_DIR = "faces"
ANGRY_DIR = "angry"
HAPPY_DIR = "happy"
NORMAL_DIR = "normal"
LARGE_DIR = "large"

# Sub directory dictionary
SUBDIR_DICTS = [{'dir': BOBBLEHEADS_DIR, 'img_key': BOBBLEHEADS_KEY, 'img_large_key': BOBBLEHEADS_LARGE_KEY},
                {'dir': HALFBODY_LARGE_DIR, 'img_key': HALFBODY_LARGE_KEY, 'img_large_key': HALFBODY_LARGE_LARGE_KEY},
                {'dir': HALFBODY_SMALL_DIR, 'img_key': HALFBODY_SMALL_KEY, 'img_large_key': HALFBODY_SMALL_LARGE_KEY},
                {'dir': MINI_DIR, 'img_key': MINI_LARGE_KEY, 'img_large_key': MINI_LARGE_KEY},
                {'dir': UNITCARDS_DIR, 'img_key': UNITCARD_KEY, 'img_large_key': UNITCARD_LARGE_KEY}]


def main():
    pass


def build_element_set(element_gender_dir):
    composite_dir = element_gender_dir.joinpath(COMPOSITES_DIR)
    stills_dir = element_gender_dir.joinpath(STILLS_DIR)

    for subdir_dict in SUBDIR_DICTS:
        subdir = stills_dir.joinpath(subdir_dict.get('dir'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process generic elemental folder and build custom generic/unique folders')
    parser.add_argument("--source_dir", required=True, help="source folder, must be the data/UI/characters/ folder and must have the elemental folders", type=str)
    parser.add_argument("--target_dir", required=True, help="will output similar to what is in the data/UI/characters/ folder", type=str)
    args = parser.parse_args()
    main()
