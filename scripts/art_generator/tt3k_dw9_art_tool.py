########################################################################################################################
# This class is used to convert images and build image folders for characters.  It can also be used to convert between
# image folders.
########################################################################################################################

import png
import sys
import argparse
from path_type import PathType
from PIL import Image #this is Pillow and not PIL
from pathlib import Path



class ArtTool:
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
    NORMAL_DIR = "norm"
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
                    {'dir': HALFBODY_LARGE_DIR, 'img_key': HALFBODY_LARGE_KEY,
                     'img_large_key': HALFBODY_LARGE_LARGE_KEY},
                    {'dir': HALFBODY_SMALL_DIR, 'img_key': HALFBODY_SMALL_KEY,
                     'img_large_key': HALFBODY_SMALL_LARGE_KEY},
                    {'dir': MINI_DIR, 'img_key': MINI_LARGE_KEY, 'img_large_key': MINI_LARGE_KEY},
                    {'dir': UNITCARDS_DIR, 'img_key': UNITCARD_KEY, 'img_large_key': UNITCARD_LARGE_KEY}]

    # PNG Chuck Stuff
    TEXT_CHUNK_FLAG = b'tEXt'
    DEFAULT_X = '-25'
    DEFAULT_Y = '-75'
    DEFAULT_PIVOT_X = '0.5000'
    DEFAULT_PIVOT_Y = '0.5000'

    # Takes a folder with base 5 large version of the required images and builds a image dictionary from them
    def create_image_dict(self, source_dir):
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
        img_dict.update({self.COMPOSITE_LARGE_KEY: composite_img})

        bobbleheads_large_img = Image.open(bobbleheads_large_file)
        bobbleheads_large_img = bobbleheads_large_img.resize(self.BOBBLEHEADS_LARGE_SIZE)
        img_dict.update({self.BOBBLEHEADS_LARGE_KEY: bobbleheads_large_img})

        bobbleheads_img = Image.open(bobbleheads_large_file)
        bobbleheads_img = bobbleheads_img.resize(self.BOBBLEHEADS_SIZE)
        img_dict.update({self.BOBBLEHEADS_KEY: bobbleheads_img})

        halfbody_large_large_img = Image.open(halfbody_large_large_file)
        halfbody_large_large_img = halfbody_large_large_img.resize(self.HALFBODY_LARGE_LARGE_SIZE)
        img_dict.update({self.HALFBODY_LARGE_LARGE_KEY: halfbody_large_large_img})

        halfbody_large_img = Image.open(halfbody_large_large_file)
        halfbody_large_img = halfbody_large_img.resize(self.HALFBODY_LARGE_SIZE)
        img_dict.update({self.HALFBODY_LARGE_KEY: halfbody_large_img})

        halfbody_small_large_img = Image.open(halfbody_large_large_file)
        halfbody_small_large_img = halfbody_small_large_img.resize(self.HALFBODY_SMALL_LARGE_SIZE)
        img_dict.update({self.HALFBODY_SMALL_LARGE_KEY: halfbody_small_large_img})

        halfbody_small_img = Image.open(halfbody_large_large_file)
        halfbody_small_img = halfbody_small_img.resize(self.HALFBODY_SMALL_SIZE)
        img_dict.update({self.HALFBODY_SMALL_KEY: halfbody_small_img})

        mini_large_img = Image.open(mini_large_file)
        mini_large_img = mini_large_img.resize(self.MINI_LARGE_SIZE)
        img_dict.update({self.MINI_LARGE_KEY: mini_large_img})

        mini_img = Image.open(mini_large_file)
        mini_img = mini_img.resize(self.MINI_SIZE)
        img_dict.update({self.MINI_KEY: mini_img})

        unitcard_large_img = Image.open(unitcard_large_file)
        unitcard_large_img = unitcard_large_img.resize(self.UNITCARD_LARGE_SIZE)
        img_dict.update({self.UNITCARD_LARGE_KEY: unitcard_large_img})

        unitcard_img = Image.open(unitcard_large_file)
        unitcard_img = unitcard_img.resize(self.UNITCARD_SIZE)
        img_dict.update({self.UNITCARD_KEY: unitcard_img})

        return img_dict


    def create_image_dict_convert_mode(self):
        pass


    def convert(self):
        pass


    def build_five_image_folder(self, source_dir, target_dir, character_dir, element, gender, is_generic):
        if is_generic:
            self.build_generic_five_image_folder(source_dir, target_dir, character_dir, element, gender)
        else:
            self.build_unique_five_image_folder(source_dir, target_dir, character_dir, element, gender)


    def build_generic_five_image_folder(self, source_dir, target_dir, character_dir, element, gender):
        composite_img = "face.png"
        composite_img_path = Path(source_dir).joinpath(self.COMPOSITES_DIR).joinpath(self.FACES_DIR).joinpath(character_dir).joinpath(self.LARGE_PANEL_DIR).joinpath(self.ANGRY_DIR).joinpath(composite_img)
        bobbleheads_large_img_path = Path(target_dir).joinpath(self.STILLS_DIR).joinpath(self.BOBBLEHEADS_DIR).joinpath(self.FACES_DIR).joinpath(self.LARGE_DIR).joinpath(character_dir + ".png")
        halfbody_large_large_img_path = Path(target_dir).joinpath(self.STILLS_DIR).joinpath(self.HALFBODY_LARGE_DIR).joinpath(self.FACES_DIR).joinpath(self.LARGE_DIR).joinpath(character_dir + ".png")
        mini_large_img_path = Path(target_dir).joinpath(self.STILLS_DIR).joinpath(self.MINI_DIR).joinpath(self.FACES_DIR).joinpath(self.LARGE_DIR).joinpath(character_dir + ".png")
        unitcards_large_img_path = Path(target_dir).joinpath(self.STILLS_DIR).joinpath(self.UNITCARDS_DIR).joinpath(self.FACES_DIR).joinpath(self.LARGE_DIR).joinpath(character_dir + ".png")

        composite_img = Image.open(composite_img_path)
        bobbleheads_img = Image.open(bobbleheads_large_img_path)
        halfbody_img = Image.open(halfbody_large_large_img_path)
        mini_img = Image.open(mini_large_img_path)
        unitcards_img = Image.open(unitcards_large_img_path)

        composite = "head.png"
        bobbleheads_large = "bobbleheads_large.png"
        halfbody_large_large = "halfbody_large_large.png"
        mini_large = "mini_large.png"
        unitcard_large = "unitcard_large.png"

        composite_img.save(Path(target_dir).joinpath(composite), self.PNG)
        bobbleheads_img.save(Path(target_dir).joinpath(bobbleheads_large), self.PNG)
        halfbody_img.save(Path(target_dir).joinpath(halfbody_large_large), self.PNG)
        mini_img.save(Path(target_dir).joinpath(mini_large), self.PNG)
        unitcards_img.save(Path(target_dir).joinpath(unitcard_large), self.PNG)


    def build_unique_five_image_folder(self, source_dir, target_dir, character_dir, element, gender):
        composite_img = "head.png"
        composite_img_path = Path(source_dir).joinpath(self.COMPOSITES_DIR).joinpath(self.LARGE_PANEL_DIR).joinpath(self.ANGRY_DIR).joinpath(composite_img)
        bobbleheads_large_img_path = Path(target_dir).joinpath(self.STILLS_DIR).joinpath(self.BOBBLEHEADS_DIR).joinpath(self.LARGE_DIR).joinpath(character_dir + ".png")
        halfbody_large_large_img_path = Path(target_dir).joinpath(self.STILLS_DIR).joinpath(self.HALFBODY_LARGE_DIR).joinpath(self.LARGE_DIR).joinpath(character_dir + ".png")
        mini_large_img_path = Path(target_dir).joinpath(self.STILLS_DIR).joinpath(self.MINI_DIR).joinpath(self.LARGE_DIR).joinpath(character_dir + ".png")
        unitcards_large_img_path = Path(target_dir).joinpath(self.STILLS_DIR).joinpath(self.UNITCARDS_DIR).joinpath(self.LARGE_DIR).joinpath(character_dir + ".png")

        composite_img = Image.open(composite_img_path)
        bobbleheads_img = Image.open(bobbleheads_large_img_path)
        halfbody_img = Image.open(halfbody_large_large_img_path)
        mini_img = Image.open(mini_large_img_path)
        unitcards_img = Image.open(unitcards_large_img_path)

        composite = "head.png"
        bobbleheads_large = "bobbleheads_large.png"
        halfbody_large_large = "halfbody_large_large.png"
        mini_large = "mini_large.png"
        unitcard_large = "unitcard_large.png"

        composite_img.save(Path(target_dir).joinpath(composite), self.PNG)
        bobbleheads_img.save(Path(target_dir).joinpath(bobbleheads_large), self.PNG)
        halfbody_img.save(Path(target_dir).joinpath(halfbody_large_large), self.PNG)
        mini_img.save(Path(target_dir).joinpath(mini_large), self.PNG)
        unitcards_img.save(Path(target_dir).joinpath(unitcard_large), self.PNG)


    def build_target_folder_structure(self, source_dir, target_dir, character_dir, element, gender, is_generic):
        image_dict = self.create_image_dict(source_dir)

        if is_generic:
            self.build_generic_target_folder(target_dir, character_dir, image_dict, element, gender)
        else:
            self.build_unique_target_folder(target_dir, character_dir, image_dict)


    def build_generic_target_folder(self, target_dir, character_dir, image_dict, element, gender):
        composite_img = "face.png"
        composite_faces_dir = Path(target_dir).joinpath(self.COMPOSITES_DIR).joinpath(self.FACES_DIR).joinpath(character_dir)

        composite_large_panel_dir = composite_faces_dir.joinpath(self.LARGE_PANEL_DIR)
        composite_large_panel_dir.joinpath(self.ANGRY_DIR).mkdir(parents=True, exist_ok=True)
        composite_large_panel_dir.joinpath(self.HAPPY_DIR).mkdir(parents=True, exist_ok=True)
        composite_large_panel_dir.joinpath(self.NORMAL_DIR).mkdir(parents=True, exist_ok=True)

        composite_small_panel_dir = composite_faces_dir.joinpath(self.SMALL_PANEL_DIR)
        composite_small_panel_dir.joinpath(self.ANGRY_DIR).mkdir(parents=True, exist_ok=True)
        composite_small_panel_dir.joinpath(self.HAPPY_DIR).mkdir(parents=True, exist_ok=True)
        composite_small_panel_dir.joinpath(self.NORMAL_DIR).mkdir(parents=True, exist_ok=True)

        image_dict.get(self.COMPOSITE_LARGE_KEY).save(composite_large_panel_dir.joinpath(self.ANGRY_DIR).joinpath(composite_img))
        image_dict.get(self.COMPOSITE_LARGE_KEY).save(composite_large_panel_dir.joinpath(self.HAPPY_DIR).joinpath(composite_img))
        image_dict.get(self.COMPOSITE_LARGE_KEY).save(composite_large_panel_dir.joinpath(self.NORMAL_DIR).joinpath(composite_img))

        image_dict.get(self.COMPOSITE_LARGE_KEY).save(composite_small_panel_dir.joinpath(self.ANGRY_DIR).joinpath(composite_img))
        image_dict.get(self.COMPOSITE_LARGE_KEY).save(composite_small_panel_dir.joinpath(self.HAPPY_DIR).joinpath(composite_img))
        image_dict.get(self.COMPOSITE_LARGE_KEY).save(composite_small_panel_dir.joinpath(self.NORMAL_DIR).joinpath(composite_img))

        # TODO: redo composites to take from source values
        angry_comment = '[type:angry;x:-25;y:-75;z-order:0;pivot_x:0.5000;pivot_y:0.5000;]'
        happy_comment = '[type:happy;x:-25;y:-75;z-order:0;pivot_x:0.5000;pivot_y:0.5000;]'
        normal_comment = '[type:norm;x:-25;y:-75;z-order:0;pivot_x:0.5000;pivot_y:0.5000;]'

        self.insert_text_chunk_to_png(composite_large_panel_dir.joinpath(self.ANGRY_DIR).joinpath(composite_img), angry_comment)
        self.insert_text_chunk_to_png(composite_large_panel_dir.joinpath(self.HAPPY_DIR).joinpath(composite_img), happy_comment)
        self.insert_text_chunk_to_png(composite_large_panel_dir.joinpath(self.NORMAL_DIR).joinpath(composite_img), normal_comment)

        self.insert_text_chunk_to_png(composite_small_panel_dir.joinpath(self.ANGRY_DIR).joinpath(composite_img), angry_comment)
        self.insert_text_chunk_to_png(composite_small_panel_dir.joinpath(self.HAPPY_DIR).joinpath(composite_img), happy_comment)
        self.insert_text_chunk_to_png(composite_small_panel_dir.joinpath(self.NORMAL_DIR).joinpath(composite_img), normal_comment)

        for subdir_dict in self.SUBDIR_DICTS:
            subdir = subdir_dict.get('dir')
            img_key = subdir_dict.get('img_key')
            img_large_key = subdir_dict.get('img_large_key')

            still_dir = Path(target_dir).joinpath(self.STILLS_DIR).joinpath(subdir)
            still_large_dir = still_dir.joinpath(self.LARGE_DIR)
            still_face_dir = still_dir.joinpath(self.FACES_DIR)
            still_face_large_dir = still_face_dir.joinpath(self.LARGE_DIR)

            still_large_dir.mkdir(parents=True, exist_ok=True)
            still_face_large_dir.mkdir(parents=True, exist_ok=True)

            image_dict.get(img_large_key).save(still_face_large_dir.joinpath(character_dir + ".png"))
            image_dict.get(img_key).save(still_face_dir.joinpath(character_dir + ".png"))

            # Populate blank ancillaries
            ancillary_images = self.get_ancillary_images_list(element, gender)
            for ancillary_image in ancillary_images:
                blank_png = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
                blank_png.save(still_dir.joinpath(ancillary_image), self.PNG)
                blank_png.save(still_large_dir.joinpath(ancillary_image), self.PNG)


    def build_unique_target_folder(self, target_dir, character_dir, image_dict):
        composite_img = "head.png"
        composite_dir = Path(target_dir).joinpath(self.COMPOSITES_DIR)

        composite_large_panel_dir = composite_dir.joinpath(self.LARGE_PANEL_DIR)
        composite_large_panel_dir.joinpath(self.ANGRY_DIR).mkdir(parents=True, exist_ok=True)
        composite_large_panel_dir.joinpath(self.HAPPY_DIR).mkdir(parents=True, exist_ok=True)
        composite_large_panel_dir.joinpath(self.NORMAL_DIR).mkdir(parents=True, exist_ok=True)

        composite_small_panel_dir = composite_dir.joinpath(self.SMALL_PANEL_DIR)
        composite_small_panel_dir.joinpath(self.ANGRY_DIR).mkdir(parents=True, exist_ok=True)
        composite_small_panel_dir.joinpath(self.HAPPY_DIR).mkdir(parents=True, exist_ok=True)
        composite_small_panel_dir.joinpath(self.NORMAL_DIR).mkdir(parents=True, exist_ok=True)

        image_dict.get(self.COMPOSITE_LARGE_KEY).save(composite_large_panel_dir.joinpath(self.ANGRY_DIR).joinpath(composite_img))
        image_dict.get(self.COMPOSITE_LARGE_KEY).save(composite_large_panel_dir.joinpath(self.HAPPY_DIR).joinpath(composite_img))
        image_dict.get(self.COMPOSITE_LARGE_KEY).save(composite_large_panel_dir.joinpath(self.NORMAL_DIR).joinpath(composite_img))

        image_dict.get(self.COMPOSITE_LARGE_KEY).save(composite_small_panel_dir.joinpath(self.ANGRY_DIR).joinpath(composite_img))
        image_dict.get(self.COMPOSITE_LARGE_KEY).save(composite_small_panel_dir.joinpath(self.HAPPY_DIR).joinpath(composite_img))
        image_dict.get(self.COMPOSITE_LARGE_KEY).save(composite_small_panel_dir.joinpath(self.NORMAL_DIR).joinpath(composite_img))

        # TODO: redo composites to take from source values
        angry_comment = '[type:angry;x:-25;y:-75;z-order:0;pivot_x:0.5000;pivot_y:0.5000;]'
        happy_comment = '[type:happy;x:-25;y:-75;z-order:0;pivot_x:0.5000;pivot_y:0.5000;]'
        normal_comment = '[type:norm;x:-25;y:-75;z-order:0;pivot_x:0.5000;pivot_y:0.5000;]'

        self.insert_text_chunk_to_png(composite_large_panel_dir.joinpath(self.ANGRY_DIR).joinpath(composite_img), angry_comment)
        self.insert_text_chunk_to_png(composite_large_panel_dir.joinpath(self.HAPPY_DIR).joinpath(composite_img), happy_comment)
        self.insert_text_chunk_to_png(composite_large_panel_dir.joinpath(self.NORMAL_DIR).joinpath(composite_img), normal_comment)

        self.insert_text_chunk_to_png(composite_small_panel_dir.joinpath(self.ANGRY_DIR).joinpath(composite_img), angry_comment)
        self.insert_text_chunk_to_png(composite_small_panel_dir.joinpath(self.HAPPY_DIR).joinpath(composite_img), happy_comment)
        self.insert_text_chunk_to_png(composite_small_panel_dir.joinpath(self.NORMAL_DIR).joinpath(composite_img), normal_comment)

        for subdir_dict in SUBDIR_DICTS:
            subdir = subdir_dict.get('dir')
            img_key = subdir_dict.get('img_key')
            img_large_key = subdir_dict.get('img_large_key')

            still_dir = Path(target_dir).joinpath(self.STILLS_DIR).joinpath(subdir)
            still_large_dir = still_dir.joinpath(self.LARGE_DIR)

            still_large_dir.mkdir(parents=True, exist_ok=True)

            image_dict.get(img_large_key).save(still_dir.joinpath(character_dir + ".png"))
            image_dict.get(img_key).save(still_large_dir.joinpath(character_dir + ".png"))


    def get_ancillary_images_list(self, element, gender):
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
                                "3k_main_ancillary_armour_medium_leather_unique_earth_" + gender + ".png",
                                "ep_ancillary_armour_light_leather_partial_exceptional_earth_" + gender + ".png",
                                "ep_ancillary_armour_light_leather_partial_unique_earth_" + gender + ".png",
                                "ep_ancillary_armour_medium_leather_exceptional_earth_" + gender + ".png",
                                "ep_ancillary_armour_medium_leather_unique_earth_" + gender + ".png"
                                ]
        elif element == 'fire':
            ancillary_images = ["3k_main_ancillary_armour_heavy_iron_common_shared_" + gender + ".png",
                                "3k_main_ancillary_armour_heavy_iron_exceptional_fire_" + gender + ".png",
                                "3k_main_ancillary_armour_heavy_iron_refined_shared_" + gender + ".png",
                                "3k_main_ancillary_armour_heavy_iron_unique_fire_" + gender + ".png",
                                "3k_main_ancillary_armour_medium_iron_partial_common_shared_" + gender + ".png",
                                "3k_main_ancillary_armour_medium_iron_partial_exceptional_fire_" + gender + ".png",
                                "3k_main_ancillary_armour_medium_iron_partial_refined_shared_" + gender + ".png",
                                "3k_main_ancillary_armour_medium_iron_partial_unique_fire_" + gender + ".png",
                                "ep_ancillary_armour_heavy_iron_exceptional_fire_" + gender + ".png",
                                "ep_ancillary_armour_heavy_iron_unique_fire_" + gender + ".png",
                                "ep_ancillary_armour_medium_iron_partial_exceptional_fire_" + gender + ".png",
                                "ep_ancillary_armour_medium_iron_partial_unique_fire_" + gender + ".png"
                                ]
        elif element == 'metal':
            ancillary_images = ["3k_main_ancillary_armour_light_leather_partial_common_shared_" + gender + ".png",
                                "3k_main_ancillary_armour_light_leather_partial_exceptional_metal_" + gender + ".png",
                                "3k_main_ancillary_armour_light_leather_partial_refined_shared_" + gender + ".png",
                                "3k_main_ancillary_armour_light_leather_partial_unique_metal_" + gender + ".png",
                                "3k_main_ancillary_armour_medium_leather_common_shared_" + gender + ".png",
                                "3k_main_ancillary_armour_medium_leather_exceptional_metal_" + gender + ".png",
                                "3k_main_ancillary_armour_medium_leather_refined_shared_" + gender + ".png",
                                "3k_main_ancillary_armour_medium_leather_unique_metal_" + gender + ".png",
                                "ep_ancillary_armour_light_leather_partial_exceptional_metal_" + gender + ".png",
                                "ep_ancillary_armour_light_leather_partial_unique_metal_" + gender + ".png",
                                "ep_ancillary_armour_medium_leather_exceptional_metal_" + gender + ".png",
                                "ep_ancillary_armour_medium_leather_unique_metal_" + gender + ".png"
                                ]
        elif element == 'water':
            ancillary_images = ["3k_main_ancillary_armour_light_tunic_common_water_" + gender + ".png",
                                "3k_main_ancillary_armour_light_tunic_exceptional_water_" + gender + ".png",
                                "3k_main_ancillary_armour_light_tunic_refined_water_" + gender + ".png",
                                "3k_main_ancillary_armour_light_tunic_unique_water_" + gender + ".png",
                                "ep_ancillary_armour_light_tunic_exceptional_water_" + gender + ".png",
                                "ep_ancillary_armour_light_tunic_unique_water_" + gender + ".png"
                                ]
        elif element == 'wood':
            ancillary_images = ["3k_main_ancillary_armour_heavy_iron_common_shared_" + gender + ".png",
                                "3k_main_ancillary_armour_heavy_iron_exceptional_wood_" + gender + ".png",
                                "3k_main_ancillary_armour_heavy_iron_refined_shared_" + gender + ".png",
                                "3k_main_ancillary_armour_heavy_iron_unique_wood_" + gender + ".png",
                                "3k_main_ancillary_armour_medium_iron_partial_common_shared_" + gender + ".png",
                                "3k_main_ancillary_armour_medium_iron_partial_exceptional_wood_" + gender + ".png",
                                "3k_main_ancillary_armour_medium_iron_partial_refined_shared_" + gender + ".png",
                                "3k_main_ancillary_armour_medium_iron_partial_unique_wood_" + gender + ".png",
                                "ep_ancillary_armour_heavy_iron_exceptional_wood_" + gender + ".png",
                                "ep_ancillary_armour_heavy_iron_unique_wood_" + gender + ".png",
                                "ep_ancillary_armour_medium_iron_partial_exceptional_wood_" + gender + ".png",
                                "ep_ancillary_armour_medium_iron_partial_unique_wood_" + gender + ".png"
                                ]
        elif element == "healer":
            ancillary_images = ["3k_ytr_ancillary_armour_healer_yellow_turban_common.png",
                                "3k_ytr_ancillary_armour_healer_yellow_turban_exceptional.png",
                                "3k_ytr_ancillary_armour_healer_yellow_turban_refined.png",
                                "3k_ytr_ancillary_armour_healer_yellow_turban_unique.png"
                                ]
        elif element == "scholar":
            ancillary_images = ["3k_ytr_ancillary_armour_scholar_medium_yellow_turban_common.png",
                                "3k_ytr_ancillary_armour_scholar_medium_yellow_turban_exceptional.png",
                                "3k_ytr_ancillary_armour_scholar_medium_yellow_turban_refined.png",
                                "3k_ytr_ancillary_armour_scholar_medium_yellow_turban_unique.png"
                                ]
        elif element == "veteran":
            ancillary_images = ["3k_ytr_ancillary_armour_veteran_medium_yellow_turban_common.png",
                                "3k_ytr_ancillary_armour_veteran_medium_yellow_turban_exceptional.png",
                                "3k_ytr_ancillary_armour_veteran_medium_yellow_turban_refined.png",
                                "3k_ytr_ancillary_armour_veteran_medium_yellow_turban_unique.png"
                                ]
        else:
            raise Exception('{} is not a valid element'.format(element))
        return ancillary_images


    def generate_chunk_tuple(self, type_flag, content):
        return tuple([type_flag, content])


    def generate_text_chunk_tuple(self, str_info):
        type_flag = self.TEXT_CHUNK_FLAG
        comment_ba = bytearray(bytes("Comment", "utf-8"))
        comment_ba.extend(b'\x00')
        comment_ba.extend(bytes(str_info, "utf-8"))

        return tuple([type_flag, bytes(comment_ba)])


    def insert_text_chunk(self, target, text, index=1):
        if index < 0:
            raise Exception('The index value {} less than 0!'.format(index))

        reader = png.Reader(filename=str(target))
        chunks = reader.chunks()
        chunk_list = list(chunks)

        # add non comment chunks to new list, basically removes all existing comments
        new_chunk_list = []
        for chunk in chunk_list:
            if b'tEXt' not in chunk[0]:
                new_chunk_list.append(chunk)

        # add the new comment with postions
        chunk_item = self.generate_text_chunk_tuple(text)
        new_chunk_list.insert(index, chunk_item)

        with open(str(target), 'wb') as dst_file:
            png.write_chunks(dst_file, new_chunk_list)


    def insert_text_chunk_to_png(self, src, message):
        # src = r'E:\temp\png\register_05.png'
        self.insert_text_chunk(src, message)

def main():
    source_dir = args.source_dir
    target_dir = args.target_dir
    character_folder = args.character_folder
    character_element = args.character_element
    character_gender = args.character_gender
    is_generic = args.is_generic
    is_invert = args.is_invert

    art_tool = ArtTool()

    if is_invert:
        art_tool.build_five_image_folder(source_dir, target_dir, character_folder, character_element, character_gender, is_generic)
    else:
        art_tool.build_target_folder_structure(source_dir, target_dir, character_folder, character_element, character_gender, is_generic)
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Processes or converts image files around to create character folders')
    parser.add_argument("--source_dir", required=True, help="source folder", type=str)
    parser.add_argument("--target_dir", required=True, help="target folder", type=str)
    parser.add_argument("--character_folder", required=True, help="name used to create the target folder", type=str)
    parser.add_argument("--character_element", required=True, help="element of the target character", type=str)
    parser.add_argument("--character_gender", required=True, help="gender of the target character", type=str)
    parser.add_argument("--composite_x", required=False, help="x offset of the composite image", type=str)
    parser.add_argument("--composite_y", required=False, help="y offset of the composite image", type=str)
    parser.add_argument("--is_generic", help="this is a generic character",  action='store_true')
    parser.add_argument("--is_invert", help="switches to dumping a character folder into the 5 image folder",  action='store_true')
    parser.add_argument("--is_convert", help="switches to convert mode",  action='store_true')
    parser.add_argument("--is_vanilla_unique", help="enable debug logging",  action='store_true')
    parser.add_argument("--verbose", help="enable debug logging",  action='store_true')
    args = parser.parse_args()
    main()












