---
author: adam
date: 2015-11-17 16:47:00+00:00
draft: false
title: Christmas Tree Light-Show with AllPixel, BiblioPixel, and PixelWeb
type: post
url: /2015/11/17/christmas-tree-light-show-with-allpixel-bibliopixel-and-pixelweb/
categories:
- AllPixel
- BiblioPixel
- Christmas
- PixelWeb
---

Ever since working on the Adafruit [APA102 Disk](/2015/05/04/review-code-adafruit-dotstar-disk/), it seemed the next logical step was to apply the same idea to a Christmas tree. So, last year after all the holidays, when everything was on sale, I picked up a 7 foot tall white artificial tree. Green would just not do... too dark for all the color :) It's still _way_ to early to put up the tree in my mind but, in the interest of beta testing, I figured I would give it a pass this year. To skip to the point and see the results, check out the video below. Or continue past for all the details of how it's done.

{{< youtube Tisn1DXV-RQ >}}

<!-- more -->

Anyone can string up some digitally controlled LEDs to a tree all willy-nilly and light them up, but making the animations work smoothly over the whole tree as a 3D object takes a little extra work. BiblioPixel has a controller called [LEDCircle](https://github.com/ManiacalLabs/bibliopixel/wiki/LEDCircle) which takes the hard work out of working with circular displays (or conical in this case, which is just a circle extruded over a point since we only care about the surface). But instead of using pixel indices or (x,y) coordinates, you can use polar coordinates: radius and angle. But we need to know how many pixels makes up each ring on the code. This required some _very_ careful layout of the pixels on the tree, counting the total number of pixels on each ring. Fortunately, unlike a real tree, the branches are evenly spaced on 14 separate levels. With this information in hand, we can define the rings on the display:

[gist https://gist.github.com/adammhaile/4a4319781503146478ba]

Note, the above is intended for use with [PixelWeb](/PixelWeb) which we highly recommend! It will create a new controller in PixelWeb called "Christmas Tree". In the genDisplayParams() method, it defines the 14 rings on the tree. The main reason when you see every single pixel defined is that layout out the LEDs was difficult to be exacting, and this allowed me to shift individual rings a few pixels in either direction to make sure the 0° mark lined up on all of them. Check out the [LEDCircle](https://github.com/ManiacalLabs/bibliopixel/wiki/LEDCircle) wiki for more information.

With the rings mapped, I needed some animations. Many were based on the above mentioned APA102 Disk review code. Check out the below gist for all the animations you see in the video above. Again, it's already setup for use with [PixelWeb](/PixelWeb); just take both files from above, save them into the same directory and then add that directory to your PixelWeb "Module Directories". Check out the [PixelWeb Wiki](https://github.com/ManiacalLabs/PixelWeb/wiki/Manifests) or the video at the end for more details on loading animations into PixelWeb.

[gist https://gist.github.com/adammhaile/246a94223c01269a38df]

{{< youtube SyL6hwqDB0Y >}}
