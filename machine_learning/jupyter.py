#===============
# View pdf 
#===============
from wand.image import Image as WImage
path = '/path/to/file.pdf'
img = WImage(filename=path, resolution=300)
img

# time code execution - single line
%timeit some_fancy_one_liner

# time code execution - entire cell
%%timeit`
some_super
multi_line
code

#