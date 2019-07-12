import os
import subprocess
import glob
from pathlib import Path

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
            out_name= os.path.join(os.path.dirname(os.path.realpath(filename)), filename_stem + ".loc")

            #build loc dbs
            subprocess.call(["python3", "convert_tsv_to_db.py", "--input", filename, "--output", out_name, "--loc"], cwd="../tsv_db_converter/")
            os.remove(filename)
        else:
            out_name= os.path.join(os.path.dirname(os.path.realpath(filename)), filename_stem)

            #build db
            subprocess.call(["python3", "convert_tsv_to_db.py", "--input", filename, "--output", out_name], cwd="../tsv_db_converter/")
            os.remove(filename)
        print(out_name)




if __name__ == '__main__':
    main()

