---
author: adam
date: 2015-01-23 12:57:53+00:00
draft: false
title: Adafruit Matrix Hat Support for BiblioPixel
type: post
url: /2015/01/23/adafruit-matrix-hat-support-for-bibliopixel/
categories:
- BiblioPixel
- Code
- Cool Stuff
- Projects
---

So, last week, [Adafruit](http://adafruit.com) launched [this little beauty](http://www.adafruit.com/product/2345). Having just acquired a handful of Pi B+ and A+ boards and already having a 32x32 matrix that I'd been meaning to use, this was a complete insta-buy™. And, of course, I had to make it work with [BiblioPixel](https://github.com/ManiacalLabs/bibliopixel)! Well, it showed up last night and the coding commenced!

Fortunately, Adafruit already had a [library](https://github.com/adafruit/rpi-rgb-led-matrix) ready to go with a handy python wrapper, since the main code is all C. Unfortunately, the python wrapper was really basic and only provided setting individual pixels. I tried this method first, but 1024 pixels all set one at a time in python was just not nearly fast enough. So...

I next had to figure out how to modify the [C python extension](https://github.com/adafruit/rpi-rgb-led-matrix/blob/master/rgbmatrix.cc)... something I've never done. As good a time as any to learn! After a bit of documentation reading, I was able to knock out a new function, [SetBuffer()](https://github.com/adafruit/rpi-rgb-led-matrix/blob/master/rgbmatrix.cc#L108), that takes the BiblioPixel data buffer and dumps it to the display's framebuffer. Internally it's still using SetPixel, but it's doing so at the C level and therefore much faster. All this and the BiblioPixel driver is insanely simple, not counting comments only 6 lines:

{{< highlight python >}}
from rgbmatrix import Adafruit_RGBmatrix
from bibliopixel.drivers.driver_base import *

class DriverAdaMatrix(DriverBase):

    # rows: height of the matrix, same as led-matrix example
    # chain: number of LEDMatrix panels, same as led-matrix example
    def __init__(self, rows = 32, chain = 1):
        super(DriverAdaMatrix, self).__init__(rows*32*chain)
        self._matrix = Adafruit_RGBmatrix(rows, chain)

    #Push new data to strand
    def update(self, data):
        self._matrix.SetBuffer(data)
{{< / highlight >}}

Since this driver is so dependent upon the Adafruit library, the Pi, and compiling C code on the Pi, I opted to not include it directly in the main BiblioPixel source. But, through the wonders of open source, it's already merged into and is [available](https://github.com/adafruit/rpi-rgb-led-matrix/blob/master/ada-matrix.py) directly in their library!

Enjoy and happy making!
