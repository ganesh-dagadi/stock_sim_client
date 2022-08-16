from dotenv import load_dotenv
import sys
import os

def setup():
    base_path = os.path.expanduser('~')
    mod_dir = base_path + '\gdmm\modules'
    sys.path.append(mod_dir)
    load_dotenv()