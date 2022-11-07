import os
import sys

script_path = os.path.realpath(__file__)
new_abs_path = os.path.join(script_path, 'fol_near_script')
if not os.path.exists(new_abs_path):
  os.mkdir(new_abs_path)