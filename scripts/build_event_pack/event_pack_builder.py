import os
import subprocess
import glob
from pathlib import Path
import shutil
import pathlib

pfm_dir='/mnt/d/Program Files/PFM/'

#this file builds event packs for tt3k_dw9
def main():
    #execute generate_spawn_def_yaml.py from its working directory
    #p = subprocess.Popen("python3 generate_spawn_def_yaml.py", cwd="../incident_generator/").wait()
    if subprocess.call(["python3", "generate_spawn_def_yaml.py"], cwd="../incident_generator/"):
        print("ERROR: generate_spawn_def_yaml.py failed")
        exit(1)

    #go through output and convert all tsv into db
    output_root = os.path.abspath("../incident_generator/output/")
    print('walk_dir (absolute) = ' + os.path.abspath(output_root))

    for filename in glob.iglob(output_root + '**/**/**.tsv', recursive=True):
        print(filename)
        filename_stem= Path(filename).stem
        if ".loc" in filename:
            out_name= os.path.join(os.path.dirname(os.path.realpath(filename)), filename_stem)

            #build loc dbs
            subprocess.call(["python3", "convert_tsv_to_db.py", "--input", filename, "--output", out_name, "--loc"], cwd="../tsv_db_converter/")
            shutil.move(filename, os.path.join(output_root, filename_stem + ".tsv"))
            #os.remove(filename)
        else:
            out_name= os.path.join(os.path.dirname(os.path.realpath(filename)), filename_stem)

            #build db
            subprocess.call(["python3", "convert_tsv_to_db.py", "--input", filename, "--output", out_name], cwd="../tsv_db_converter/")
            shutil.move(filename, os.path.join(output_root, filename_stem + ".tsv"))
            #os.remove(filename)
        print(out_name)

    #pfm information
    pfm_cwd = os.path.abspath("../incident_generator/output/")
    pfm_cli = "/mnt/d/Program Files/PFM/pfm.exe"
    event_pack_file_name = "total_war_dynasty_warriors_9_events.pack"

    #move other files into the folder
    #move the categories files
    pathlib.Path(os.path.join(pfm_cwd, "db/cdir_events_categories_tables/")).mkdir(parents=True, exist_ok=True)
    shutil.copy("include_files/tt3k_dw9_event_categories", os.path.join(pfm_cwd, "db/cdir_events_categories_tables/tt3k_dw9_event_categories"))

    #hardcode for pfm
    #this is required until we get RPFM's cli
    subprocess.call([pfm_cli, "c", event_pack_file_name], cwd=pfm_cwd)

    subprocess.call([pfm_cli, "a", event_pack_file_name, "db/cdir_events_incident_option_junctions_tables/tt3k_dw9_incident_option_junctions"], cwd=pfm_cwd)
    subprocess.call([pfm_cli, "a", event_pack_file_name, "db/cdir_events_incident_payloads_tables/tt3k_dw9_incident_payloads"], cwd=pfm_cwd)
    subprocess.call([pfm_cli, "a", event_pack_file_name, "db/incidents_tables/tt3k_dw9_incidents"], cwd=pfm_cwd)

    subprocess.call([pfm_cli, "a", event_pack_file_name, "db/cdir_events_dilemma_choice_details_tables/tt3k_dw9_dilemma_choice_details"], cwd=pfm_cwd)
    subprocess.call([pfm_cli, "a", event_pack_file_name, "db/cdir_events_dilemma_option_junctions_tables/tt3k_dw9_dilemma_option_junctions"], cwd=pfm_cwd)
    subprocess.call([pfm_cli, "a", event_pack_file_name, "db/cdir_events_dilemma_payloads_tables/tt3k_dw9_dilemma_payloads"], cwd=pfm_cwd)
    subprocess.call([pfm_cli, "a", event_pack_file_name, "db/dilemmas_tables/tt3k_dw9_dilemmas"], cwd=pfm_cwd)

    subprocess.call([pfm_cli, "a", event_pack_file_name, "text/db/tt3k_dw9_dilemma_choices.loc"], cwd=pfm_cwd)
    subprocess.call([pfm_cli, "a", event_pack_file_name, "text/db/tt3k_dw9_dilemmas.loc"], cwd=pfm_cwd)
    subprocess.call([pfm_cli, "a", event_pack_file_name, "text/db/tt3k_dw9_incidents.loc"], cwd=pfm_cwd)

    subprocess.call([pfm_cli, "a", event_pack_file_name, "script/campaign/mod/tt3k_dw9_custom_events.lua"], cwd=pfm_cwd)

    subprocess.call([pfm_cli, "a", event_pack_file_name, "db/cdir_events_categories_tables/tt3k_dw9_event_categories"], cwd=pfm_cwd)

if __name__ == '__main__':
    main()

