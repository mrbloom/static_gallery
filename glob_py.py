
from glob import glob

imgs = glob(*.jpg)
imgs.reverse()

with open("images.txt","w") as f:
    for img in imgs:
        f.write('<div data-thumb="images/slides/thumbs/tn_' + img + '" data-src="images/slides/' + img + '"></div>\n')
