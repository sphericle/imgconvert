from PIL import Image
import re

import os

base_path = 'input/'

i = 0

for filename in os.listdir(base_path):
    file_path = os.path.join(base_path, filename)
    if os.path.isfile(file_path):
        no_ext = filename.split('.')[0]
        
        print('Converted ' + no_ext)
        
        if filename != 'info.txt':
            try:
                i += 1
                im = Image.open(file_path).convert('RGB')
                im.save(f'output/converted {no_ext} {i}.png', "png")
            except:
                print('File not found')