#===============
# View pdf 
#===============
from wand.image import Image as WImage
path = '/path/to/file.pdf'
img = WImage(filename=path, resolution=300)
img

# time code execution - single line
%%time`
super_advanced_single_line_code

#