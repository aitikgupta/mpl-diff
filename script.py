"""
A sample script to trigger Matplotlib's PS/EPS backend
"""
import matplotlib as mpl
# mpl.use("module://mplcairo.qt")

import matplotlib.pyplot as plt
print(mpl.get_backend())
mpl.rcParams['text.usetex'] = True

STRING = "simple text"

fig, ax = plt.subplots()
ax.text(0.45, 0.5, STRING)

# The EPS file is then converted to a PNG file using the converter from
# ImageMagick: http://www.imagemagick.org/script/convert.php
plt.savefig('image.eps')
