# This script generates an entire characters/ folder

from tt3k_dw9_art_tool import ArtTool
import argparse
import yaml
import pprint
from path_type import PathType
from pathlib import Path


class ArtSetGenerator:

    CONFIG_DIR = "config"
    PORTRAIT_SET_CONFIG = "portrait_set_config.yaml"

    def read_portrait_set_config(self):
        portrait_set_config_path = Path(self.CONFIG_DIR).joinpath(self.PORTRAIT_SET_CONFIG)

        with open(portrait_set_config_path,  'r') as portrait_set_config_file:
            portrait_set_config_data = yaml.safe_load(portrait_set_config_file)

        return portrait_set_config_data


    def read_portrait_set(self, portrait_set_file_name):
        portrait_set_path = Path(self.CONFIG_DIR).joinpath(portrait_set_file_name)

        with open(portrait_set_path,  'r') as portrait_set_file:
            portrait_set_data = yaml.safe_load(portrait_set_file)

        return portrait_set_data


    def build_portrait_set(self, build_target, target_dir):
        config_data = self.read_portrait_set_config()

        # logic
        # get load order, pull load order yaml files
        # loop through arts in config data
        # check if load order name exists, if it does, run the art tool on the ps_data
        load_order = config_data.get("art_set_build_priority").get(build_target).get("priority")

        #create art tool object
        art_tool = ArtTool()

        #loop through load order and load each portrait set yaml
        #for now just only load the first one
        ps_data = {}
        for load_order_set in load_order:
            portrait_set = self.read_portrait_set(config_data.get("art_sets").get(load_order_set).get("file_name"))
            ps_data.update({load_order_set: portrait_set})

        # loop through arts
        arts = config_data.get("arts")
        for art, data in arts.items():
            # check to see which art set to load based on priority
            selected_art_set = ""
            for load_order_set in load_order:
                if load_order_set in data.get("art_sets"):
                    selected_art_set = load_order_set

            # skip this art if there are no matching sets from the priority list
            if selected_art_set == "":
                continue

            # get art and create it
            art_data = ps_data.get(selected_art_set)
            character_art_data = art_data.get("arts").get(art)
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(character_art_data)

            #run art tool here
            char_source_dir = Path(config_data.get("source_dir")).joinpath(config_data.get("art_sets").get(selected_art_set).get("dir")).joinpath(character_art_data.get("src_dir"))
            char_target_dir = Path(target_dir).joinpath(character_art_data.get("char_dir_name"))
            char_card = character_art_data.get("char_file_name")
            char_element = character_art_data.get("element")
            char_gender = character_art_data.get("gender")
            char_type = character_art_data.get("type")
            if char_type == "generic":
                char_is_generic = True
            elif char_type == "ca_unique" or char_type == "unique":
                char_is_generic = False
            else:
                raise Exception("Error when processing character {}. {} is not a valid value for character type.".format(char_source_dir, char_type))

            print(char_source_dir)
            print(char_target_dir)
            print(char_card)
            print(char_element)
            print(char_gender)
            print(char_is_generic)
            #art_tool.build_target_folder_structure(source_dir, target_dir, character_folder, character_element, character_gender, is_generic)

def main():
    build_target = args.build_target
    target_dir = args.target_dir

    art_set_generator = ArtSetGenerator()
    art_set_generator.build_portrait_set(build_target, target_dir)
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Builds entire portrait set for the TT3K_DW9 mod')
    parser.add_argument("--build_target", required=True, help="source folder", type=str)
    parser.add_argument("--target_dir", required=True, help="target folder", type=str)
    args = parser.parse_args()
    main()
