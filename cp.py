# get file as first argument
# copy file to directory

import sys
import os
output_dir = "/Users/kwonmingi/Documents/video_survey/video"
input_file = sys.argv[1]
input_file = os.path.join("/Users/kwonmingi/Downloads/Adobe_internship/poject_page/supple", input_file)
output_file = os.path.join(output_dir, os.path.basename(input_file))

print("Copying file %s to %s" % (input_file, output_file))

import shutil
shutil.copy(input_file, output_file)
