from dotenv import load_dotenv
import sys
import os

def setup():
    CURR_DIR = os.path.dirname(os.path.realpath(__file__))
    base_path = chr(92).join(CURR_DIR.split(chr(92), 3)[:3])
    mod_dir = base_path + '\gdmm\modules'
    sys.path.append(mod_dir)
    load_dotenv()