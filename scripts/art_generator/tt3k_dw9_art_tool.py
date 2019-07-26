import png
import sys
import argparse
from path_type import PathType
from PIL import Image
from pathlib import Path

# Image Constants
TRANSPARENT_BACKGROUND = "transparent"
CENTER = "center"
PNG = "PNG"

# Image sizes
BOBBLEHEADS_LARGE_SIZE = 134, 220
BOBBLEHEADS_SIZE = 84, 138
HALFBODY_LARGE_LARGE_SIZE = 499, 400
HALFBODY_LARGE_SIZE = 312, 250
HALFBODY_SMALL_LARGE_SIZE = 176, 134
HALFBODY_SMALL_SIZE = 110, 84
MINI_LARGE_SIZE = 48, 48
MINI_SIZE = 30, 30
UNITCARD_LARGE_SIZE = 131, 435
UNITCARD_SIZE = 82, 272

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

# Image references for the dictionary
COMPOSITE_LARGE_KEY = "composite_large_key"
BOBBLEHEADS_LARGE_KEY = "bobbleheads_large_key"
BOBBLEHEADS_KEY = "bobbleheads_key"
HALFBODY_LARGE_LARGE_KEY = "halfbody_large_large_key"
HALFBODY_LARGE_KEY = "halfbody_large_key"
HALFBODY_SMALL_LARGE_KEY = "halfbody_small_large_key"
HALFBODY_SMALL_KEY = "halfbody_small_key"
MINI_LARGE_KEY = "mini_large_key"
MINI_KEY = "mini_key"
UNITCARD_LARGE_KEY = "unitcard_large_key"
UNITCARD_KEY = "unitcard_key"

# Sub directory dictionary
SUBDIR_DICTS = [{'dir': BOBBLEHEADS_DIR, 'img_key': BOBBLEHEADS_KEY, 'img_large_key': BOBBLEHEADS_LARGE_KEY},
                {'dir': HALFBODY_LARGE_DIR, 'img_key': HALFBODY_LARGE_KEY, 'img_large_key': HALFBODY_LARGE_LARGE_KEY},
                {'dir': HALFBODY_SMALL_DIR, 'img_key': HALFBODY_SMALL_KEY, 'img_large_key': HALFBODY_SMALL_LARGE_KEY},
                {'dir': MINI_DIR, 'img_key': MINI_LARGE_KEY, 'img_large_key': MINI_LARGE_KEY},
                {'dir': UNITCARDS_DIR, 'img_key': UNITCARD_KEY, 'img_large_key': UNITCARD_LARGE_KEY}]

# PNG Chuck Stuff
TEXT_CHUNK_FLAG = b'tEXt'
DEFAULT_X = '-25'
DEFAULT_Y = '-75'
DEFAULT_PIVOT_X = '0.5000'
DEFAULT_PIVOT_Y = '0.5000'


def main():
    pass


# Takes a folder with base 5 large version of the required images and builds a image dictionary from them
def create_image_dict(source_dir):
    img_dict = {}

    composite = "head.png"
    bobbleheads_large = "bobbleheads_large.png"
    halfbody_large_large = "halfbody_large_large.png"
    mini_large = "mini_large.png"
    unitcard_large = "unitcard_large.png"

    composite_file = Path(source_dir).joinpath(composite)
    bobbleheads_large_file = Path(source_dir).joinpath(bobbleheads_large)
    halfbody_large_large_file = Path(source_dir).joinpath(halfbody_large_large)
    mini_large_file = Path(source_dir).joinpath(mini_large)
    unitcard_large_file = Path(source_dir).joinpath(unitcard_large)

    # create full set from starting 5 images
    composite_img = Image.open(composite_file)
    img_dict.update({COMPOSITE_LARGE_KEY, composite_img})

    bobbleheads_large_img = Image.open(bobbleheads_large_file)
    bobbleheads_large_img.resize(BOBBLEHEADS_LARGE_SIZE)
    img_dict.update({BOBBLEHEADS_LARGE_KEY, bobbleheads_large_img})

    bobbleheads_img = Image.open(bobbleheads_large_file)
    bobbleheads_img.rezie(BOBBLEHEADS_SIZE)
    img_dict.update({BOBBLEHEADS_KEY, bobbleheads_img})

    halfbody_large_large_img = Image.open(halfbody_large_large_file)
    halfbody_large_large_img.resize(HALFBODY_LARGE_LARGE_SIZE)
    img_dict.update({HALFBODY_LARGE_LARGE_KEY, halfbody_large_large_img})

    halfbody_large_img = Image.open(halfbody_large_large_file)
    halfbody_large_img.resize(HALFBODY_LARGE_SIZE)
    img_dict.update({HALFBODY_LARGE_KEY, halfbody_large_img})

    halfbody_small_large_img = Image.open(halfbody_large_large_file)
    halfbody_small_large_img.resize(HALFBODY_SMALL_LARGE_SIZE)
    img_dict.update({HALFBODY_SMALL_LARGE_KEY, halfbody_small_large_img})

    halfbody_small_img = Image(halfbody_large_large_file)
    halfbody_small_img.resize(HALFBODY_SMALL_SIZE)
    img_dict.update({HALFBODY_SMALL_KEY, halfbody_small_img})

    mini_large_img = Image(mini_large_file)
    mini_large_img.resize(MINI_LARGE_SIZE)
    img_dict.update({MINI_LARGE_KEY, mini_large_img})

    mini_img = Image(mini_large_file)
    mini_img.resize(MINI_SIZE)
    img_dict.update({MINI_KEY, mini_img})

    unitcard_large_img = Image(unitcard_large_file)
    unitcard_large_img.resize(UNITCARD_LARGE_SIZE)
    img_dict.update({UNITCARD_LARGE_KEY, unitcard_large_img})

    unitcard_img = Image(unitcard_large_file)
    unitcard_img.resize(UNITCARD_SIZE)
    img_dict.update({UNITCARD_KEY, unitcard_img})

    return img_dict


def create_image_dict_convert_mode():
    pass


def convert():
    pass


def build_target_folder_structure(target_dir, generic):
    # folder folders if they don't exist
    pass


def build_generic_target_folder(target_dir, character_dir, image_dict, element, gender):
    composite_img = "face.png"
    composite_faces_dir = Path(target_dir).joinpath(COMPOSITES_DIR).joinpath(FACES_DIR).joinpath(character_dir)

    composite_large_panel_dir = composite_faces_dir.joinpath(LARGE_PANEL_DIR)
    composite_large_panel_dir.joinpath(ANGRY_DIR).mkdir(parents=True, exist_ok=True)
    composite_large_panel_dir.joinpath(HAPPY_DIR).mkdir(parents=True, exist_ok=True)
    composite_large_panel_dir.joinpath(NORMAL_DIR).mkdir(parents=True, exist_ok=True)

    composite_small_panel_dir = composite_faces_dir.joinpath(SMALL_PANEL_DIR)
    composite_small_panel_dir.joinpath(ANGRY_DIR).mkdir(parents=True, exist_ok=True)
    composite_small_panel_dir.joinpath(HAPPY_DIR).mkdir(parents=True, exist_ok=True)
    composite_small_panel_dir.joinpath(NORMAL_DIR).mkdir(parents=True, exist_ok=True)

    image_dict.get(COMPOSITE_LARGE_KEY).save(composite_large_panel_dir.joinpath(ANGRY_DIR).joinpath(composite_img))
    image_dict.get(COMPOSITE_LARGE_KEY).save(composite_large_panel_dir.joinpath(HAPPY_DIR).joinpath(composite_img))
    image_dict.get(COMPOSITE_LARGE_KEY).save(composite_large_panel_dir.joinpath(NORMAL_DIR).joinpath(composite_img))

    image_dict.get(COMPOSITE_LARGE_KEY).save(composite_small_panel_dir.joinpath(ANGRY_DIR).joinpath(composite_img))
    image_dict.get(COMPOSITE_LARGE_KEY).save(composite_small_panel_dir.joinpath(HAPPY_DIR).joinpath(composite_img))
    image_dict.get(COMPOSITE_LARGE_KEY).save(composite_small_panel_dir.joinpath(NORMAL_DIR).joinpath(composite_img))

    # TODO: redo composites to take from source values
    angry_comment = '[type:angry;x:-25;y:-75;z-order:0;pivot_x:0.5000;pivot_y:0.5000;]'
    happy_comment = '[type:happy;x:-25;y:-75;z-order:0;pivot_x:0.5000;pivot_y:0.5000;]'
    normal_comment = '[type:norm;x:-25;y:-75;z-order:0;pivot_x:0.5000;pivot_y:0.5000;]'

    insert_text_chunk_to_png(composite_small_panel_dir.joinpath(ANGRY_DIR).joinpath(composite_img), angry_comment)
    insert_text_chunk_to_png(composite_small_panel_dir.joinpath(HAPPY_DIR).joinpath(composite_img), happy_comment)
    insert_text_chunk_to_png(composite_small_panel_dir.joinpath(NORMAL_DIR).joinpath(composite_img), normal_comment)

    insert_text_chunk_to_png(composite_small_panel_dir.joinpath(ANGRY_DIR).joinpath(composite_img), angry_comment)
    insert_text_chunk_to_png(composite_small_panel_dir.joinpath(HAPPY_DIR).joinpath(composite_img), happy_comment)
    insert_text_chunk_to_png(composite_small_panel_dir.joinpath(NORMAL_DIR).joinpath(composite_img), normal_comment)

    for subdir_dict in SUBDIR_DICTS:
        subdir = subdir_dict.get('dir')
        img_key = subdir_dict.get('img_key')
        img_large_key = subdir_dict.get('img_large_key')

        still_dir = Path(target_dir).joinpath(STILLS_DIR).joinpath(subdir)
        still_large_dir = still_dir.joinpath(LARGE_DIR)
        still_face_dir = still_dir.joinpath(FACES_DIR)
        still_face_large_dir = still_face_dir.joinpath(LARGE_DIR)

        still_large_dir.mkdir(parents=True, exist_ok=True)
        still_face_large_dir.mkdir(parents=True, exist_ok=True)

        image_dict.get(img_large_key).save(still_face_large_dir.joinpath(character_dir + ".png"))
        image_dict.get(img_key).save(still_face_dir.joinpath(character_dir + ".png"))

        # Populate blank ancillaries
        ancillary_images = get_ancillary_images_list(element, gender)
        for ancillary_image in ancillary_images:
            blank_png = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
            blank_png.save(still_dir.joinpath(ancillary_image), PNG)
            blank_png.save(still_large_dir.joinpath(ancillary_image), PNG)


def build_unique_target_folder(target_dir, character_dir, image_dict):
    composite_img = "head.png"
    composite_dir = Path(target_dir).joinpath(COMPOSITES_DIR)

    composite_large_panel_dir = composite_dir.joinpath(LARGE_PANEL_DIR)
    composite_large_panel_dir.joinpath(ANGRY_DIR).mkdir(parents=True, exist_ok=True)
    composite_large_panel_dir.joinpath(HAPPY_DIR).mkdir(parents=True, exist_ok=True)
    composite_large_panel_dir.joinpath(NORMAL_DIR).mkdir(parents=True, exist_ok=True)

    composite_small_panel_dir = composite_dir.joinpath(SMALL_PANEL_DIR)
    composite_small_panel_dir.joinpath(ANGRY_DIR).mkdir(parents=True, exist_ok=True)
    composite_small_panel_dir.joinpath(HAPPY_DIR).mkdir(parents=True, exist_ok=True)
    composite_small_panel_dir.joinpath(NORMAL_DIR).mkdir(parents=True, exist_ok=True)

    image_dict.get(COMPOSITE_LARGE_KEY).save(composite_large_panel_dir.joinpath(ANGRY_DIR).joinpath(composite_img))
    image_dict.get(COMPOSITE_LARGE_KEY).save(composite_large_panel_dir.joinpath(HAPPY_DIR).joinpath(composite_img))
    image_dict.get(COMPOSITE_LARGE_KEY).save(composite_large_panel_dir.joinpath(NORMAL_DIR).joinpath(composite_img))

    image_dict.get(COMPOSITE_LARGE_KEY).save(composite_small_panel_dir.joinpath(ANGRY_DIR).joinpath(composite_img))
    image_dict.get(COMPOSITE_LARGE_KEY).save(composite_small_panel_dir.joinpath(HAPPY_DIR).joinpath(composite_img))
    image_dict.get(COMPOSITE_LARGE_KEY).save(composite_small_panel_dir.joinpath(NORMAL_DIR).joinpath(composite_img))

    # TODO: redo composites to take from source values
    angry_comment = '[type:angry;x:-25;y:-75;z-order:0;pivot_x:0.5000;pivot_y:0.5000;]'
    happy_comment = '[type:happy;x:-25;y:-75;z-order:0;pivot_x:0.5000;pivot_y:0.5000;]'
    normal_comment = '[type:norm;x:-25;y:-75;z-order:0;pivot_x:0.5000;pivot_y:0.5000;]'

    insert_text_chunk_to_png(composite_small_panel_dir.joinpath(ANGRY_DIR).joinpath(composite_img), angry_comment)
    insert_text_chunk_to_png(composite_small_panel_dir.joinpath(HAPPY_DIR).joinpath(composite_img), happy_comment)
    insert_text_chunk_to_png(composite_small_panel_dir.joinpath(NORMAL_DIR).joinpath(composite_img), normal_comment)

    insert_text_chunk_to_png(composite_small_panel_dir.joinpath(ANGRY_DIR).joinpath(composite_img), angry_comment)
    insert_text_chunk_to_png(composite_small_panel_dir.joinpath(HAPPY_DIR).joinpath(composite_img), happy_comment)
    insert_text_chunk_to_png(composite_small_panel_dir.joinpath(NORMAL_DIR).joinpath(composite_img), normal_comment)

    for subdir_dict in SUBDIR_DICTS:
        subdir = subdir_dict.get('dir')
        img_key = subdir_dict.get('img_key')
        img_large_key = subdir_dict.get('img_large_key')

        still_dir = Path(target_dir).joinpath(STILLS_DIR).joinpath(subdir)
        still_large_dir = still_dir.joinpath(LARGE_DIR)

        still_large_dir.mkdir(parents=True, exist_ok=True)

        image_dict.get(img_large_key).save(still_dir.joinpath(character_dir + ".png"))
        image_dict.get(img_key).save(still_large_dir.joinpath(character_dir + ".png"))


def get_ancillary_images_list(element, gender):
    if gender != "male" and gender != "female":
        raise Exception('{} is not a valid gender'.format(gender))

    if element == 'earth':
        ancillary_images = ["3k_main_ancillary_armour_light_armour_earth_metal_and_water_common" + gender + ".png",
                            "3k_main_ancillary_armour_light_leather_partial_common_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_light_leather_partial_exceptional_earth_" + gender + ".png",
                            "3k_main_ancillary_armour_light_leather_partial_refined_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_light_leather_partial_unique_earth_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_leather_common_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_leather_exceptional_earth_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_leather_refined_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_leather_unique_earth_" + gender + ".png"
                            ]
    elif element == 'fire':
        ancillary_images = ["3k_main_ancillary_armour_heavy_iron_common_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_heavy_iron_exceptional_fire_" + gender + ".png",
                            "3k_main_ancillary_armour_heavy_iron_refined_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_heavy_iron_unique_fire_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_iron_partial_common_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_iron_partial_exceptional_fire_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_iron_partial_refined_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_iron_partial_unique_fire_" + gender + ".png"
                            ]
    elif element == 'metal':
        ancillary_images = ["3k_main_ancillary_armour_light_leather_partial_common_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_light_leather_partial_exceptional_metal_" + gender + ".png",
                            "3k_main_ancillary_armour_light_leather_partial_refined_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_light_leather_partial_unique_metal_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_leather_common_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_leather_exceptional_metal_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_leather_refined_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_leather_unique_metal_" + gender + ".png"
                            ]
    elif element == 'water':
        ancillary_images = ["3k_main_ancillary_armour_light_tunic_common_water_" + gender + ".png",
                            "3k_main_ancillary_armour_light_tunic_exceptional_water_" + gender + ".png",
                            "3k_main_ancillary_armour_light_tunic_refined_water_" + gender + ".png",
                            "3k_main_ancillary_armour_light_tunic_unique_water_" + gender + ".png"
                            ]
    elif element == 'wood':
        ancillary_images = ["3k_main_ancillary_armour_heavy_iron_common_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_heavy_iron_exceptional_wood_" + gender + ".png",
                            "3k_main_ancillary_armour_heavy_iron_refined_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_heavy_iron_unique_wood_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_iron_partial_common_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_iron_partial_exceptional_wood_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_iron_partial_refined_shared_" + gender + ".png",
                            "3k_main_ancillary_armour_medium_iron_partial_unique_wood_" + gender + ".png"
                            ]
    elif element == "healer":
        pass
    elif element == "veteran":
        pass
    elif element == "colonel":
        pass
    else:
        raise Exception('{} is not a valid element'.format(element))
    return ancillary_images


def generate_chunk_tuple(type_flag, content):
    return tuple([type_flag, content])


def generate_text_chunk_tuple(str_info):
    type_flag = TEXT_CHUNK_FLAG
    comment_ba = bytearray(bytes("Comment").encode("utf-8"))
    comment_ba.append(b'\x00')
    comment_ba.extend(bytes(str_info).encode("utf-8"))

    return tuple([type_flag, bytes(comment_ba)])


def insert_text_chunk(target, text, index=1):
    if index < 0:
        raise Exception('The index value {} less than 0!'.format(index))

    reader = png.Reader(filename=target)
    chunks = reader.chunks()
    chunk_list = list(chunks)

    # add non comment chunks to new list, basically removes all existing comments
    new_chunk_list = []
    for chunk in chunk_list:
        if 'tEXt' not in chunk[0]:
            new_chunk_list.append(chunk)

    # add the new comment with postions
    chunk_item = generate_text_chunk_tuple(text)
    new_chunk_list.insert(index, chunk_item)

    with open(target, 'wb') as dst_file:
        png.write_chunks(dst_file, new_chunk_list)


def insert_text_chunk_to_png(src, message):
    # src = r'E:\temp\png\register_05.png'
    insert_text_chunk(src, message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Processes or converts image files around to create character folders')
    parser.add_argument("--source_dir", required=True, help="source folder", type=PathType)
    parser.add_argument("--target_dir", required=True, help="target folder", type=PathType)
    parser.add_argument("--character_folder", required=True, help="name used to create the target folder", type=str)
    parser.add_argument("--character_element", required=True, help="element of the target character", type=str)
    parser.add_argument("--character_gender", required=True, help="gender of the target character", type=str)
    parser.add_argument("--composite_x", required=False, help="x offset of the composite image", type=str)
    parser.add_argument("--composite_y", required=False, help="y offset of the composite image", type=str)
    parser.add_argument("--generic", help="this is a generic character",  action='store_true')
    parser.add_argument("--convert", help="switches to convert mode",  action='store_true')
    parser.add_argument("--vanilla_unique", help="enable debug logging",  action='store_true')
    parser.add_argument("--verbose", help="enable debug logging",  action='store_true')
    args = parser.parse_args()
    main()












