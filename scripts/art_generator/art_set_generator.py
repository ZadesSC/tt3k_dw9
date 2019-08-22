# This script generates an entire characters/ folder

import tt3k_dw9_art_tool
import argparse
import yaml
from path_type import PathType
from pathlib import Path

CONFIG_DIR = "config"
PORTRAIT_SET_CONFIG = "portrait_set_config.yaml"


def main():
    build_target = args.build_target
    target_dir = args.target_dir
    pass


def read_portrait_set_config():
    portrait_set_config_path = Path(CONFIG_DIR).joinpath(PORTRAIT_SET_CONFIG)

    with open(portrait_set_config_path,  'r') as portrait_set_config_file:
        portrait_set_config_data = yaml.safe_load(portrait_set_config_file)

    return portrait_set_config_data

def read_portrait_set(portrait_set_file_name):
    portrait_set_path = Path(CONFIG_DIR).joinpath(portrait_set_file_name)

    with open(portrait_set_path,  'r') as portrait_set_file:
        portrait_set_data = yaml.safe_load(portrait_set_file)

    return portrait_set_data

def build_portrait_set(build_target, target_dir):
    config_data = read_portrait_set_config()
    portrait_set_file_name = config_data.get("art_sets").get(build_target).get("dir")
    ps_data = read_portrait_set(portrait_set_file_name)


    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Builds entire portrait set for the TT3K_DW9 mod')
    parser.add_argument("--build_target", required=True, help="source folder", type=str)
    parser.add_argument("--target_dir", required=True, help="target folder", type=str)
    args = parser.parse_args()
    main()
