# mpl-diff
#### A sample repository which aims to compare the difference between TeX exporting mechanism for PS/EPS backends in core [matplotlib](https://github.com/matplotlib/matplotlib) vs [mplcairo](https://github.com/matplotlib/mplcairo/).
### The interactive diff can be seen via [this link](https://github.com/aitikgupta/mpl-diff/pull/1/files?short_path=4ee84a8#diff-4ee84a82b5e4c9e6651b13fd27dcf615e427ec584929f2cef7167aa99151a77a).

The images are exported by Matplotlib in EPS format (see [script.py](https://github.com/aitikgupta/mpl-diff/blob/main/script.py)), which are then converted to PNGs for GitHub to render the above result with [ImageMagick](http://www.imagemagick.org/script/convert.php):
```console
convert -density 150 -geometry 100% image.eps image.png
```
Author: [Aitik Gupta](https://aitikgupta.github.io/)
