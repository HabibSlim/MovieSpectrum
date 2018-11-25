<h1 align="center">
    MovieSpectrum
</h1>
<p align="center">
<sup>
<b>MovieSpectrum is a simple program that you can use to extract the color spectrum of a film or a video.</b>
</sup>
</p>

# How to use it?
Define the script parameters in params.py.
You will have to adjust IMAGE_WIDTH, IMAGE_HEIGHT for the output picture, and SAMPLE_NUMBER to define the number of frames to be used to build the spectrum.

# Averaging methods
You can also play with average methods, square average seems to give the best results.
However, do NOT try to use K-Mean clustering unless you are working with a very small SAMPLE_NUMBER, it will take way too much time for not that good of a result.

Just call spectrum.py in a terminal and supply a video path, like this :

    spectrum.py Porco\ Rosso.avi

A window will popup and the spectrum will start building. When you are finished, just press Q to exit.

# Dependencies
* <a href="https://github.com/numpy/numpy">Numpy</a>
* <a href="https://github.com/opencv/opencv">OpenCV</a>

# Some examples
Here are some cool examples built using the script.

Princess Mononoke

<h1 align="center">
    <img src="examples/mononoke.png">
</h1>

Porco Rosso

<h1 align="center">
    <img src="examples/porco_rosso.png">
</h1>

Have fun !