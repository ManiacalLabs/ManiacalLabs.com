---
author: adam
date: 2015-05-04 14:44:24+00:00
draft: false
title: 'Review & Code: Adafruit DotStar Disk'
type: post
url: /2015/05/04/review-code-adafruit-dotstar-disk/
---

About a week ago, Adafruit released [this beauty](http://www.adafruit.com/products/2477):

{{< figure src="/wp-content/uploads/2015/05/APA102Disk.png" caption="APA102Disk" >}}

Needless to say, I bought one immediately.

<!-- more -->



### Hardware



It's a really interesting display that uses 255 APA102 (DotStar) LEDs in 10 concentric circles on a 240mm circular 1.6mm PCB. I couldn't be happier about it using the awesome APA102 chipset, which is tremendously versatile, super fast, and easy to communicate with from a wide variety of devices. Including the [AllPixel](/AllPixel), of course :) All told, it makes for one sexy display.

Note that Adafruit doesn't actually manufacturer this display. If they had, instead of a Chinese company with a [malfunctioning website](http://www.soya-led.com/), I imagine that my few gripes with the display would not be an issue.

Basically, I have a problem with the power setup. The APA102 datasheet claims a max draw of 40mA per LED at full white which would mean 255x0.04A = 10.2A max draw. In general, the power traces on the display are decent at about 4mm wide which should be enough to carry the current. But the connectors are _not_ up to the task. It comes with standard 4-pin JST SM that, sadly, only use 22 gauge wire. According to the usual wire gauge current rating tables, that wire should only be able to handle, at most, 7A! (Edit: For the record, yes, there are two connectors on the disk, but the output connector is NOT connected to the VCC trace, only ground.) That's just bad design. First chance I get, I will be replacing those cables with some lower gauge wires to make sure it has no problem drawing the max rated power. They really could learn a few things from the [RGB-123](http://rgb-123.com/) offerings which can always handle the maximum possible power.

My last, and smallest, gripe with the display is that it's outer ring has only 48 pixels. My first though for it was, of course, to make a clock, but that is a little weird to do when there's no way to get 60 full seconds or minutes on the display. I have a basic clock concept working, but it has to tick every 1.25 seconds. Not a huge deal, I'd just love to see a bigger display with a 60 pixel outer ring :)



### Software



Even though it is an awesome display, it's no use unless you can control it in a way that won't cause hair loss in the process. [BiblioPixel](/bibliopixel) already has the LEDStrip and LEDMatrix classes for controlling strips and matrices, respectively. LEDMatrix is right out because there's no way a standard (x,y) coordinate system would make sense. The cop-out way would be to use LEDStrip and then program all the animations in a very hard-coded, manual way such that it looks like everything is being done in a circular fashion. This is what I originally did, by implementing the [Bloom](https://github.com/ManiacalLabs/bibliopixel/blob/master/matrix_animations.py#L40) animation, but with LEDStrip instead. This was done by mapping out what LED indices were in each ring, and then filling each ring, based on those indices, with a slowing changing gradient. But as I was writing this code, I looked at the mapping I generated and had an epiphany:

```
rings = [
    [254,254],  #0 - Center point
    [248,253],  #1
    [236,247],  #2
    [216,235],  #3
    [192,215],  #4
    [164,191],  #5
    [132,163],  #6
    [92,131],   #7
    [48,91],    #8
    [0,47],     #9 - Outer-most ring
]
```

If I knew the start and end indices of the pixels in each ring and assumed that all rings have the pixels evenly arranged in the ring, I could easily calculate the degrees between each pixel for that ring with a simple formula: `ringDegrees = 360.0/(endIndex - startIndex + 1)`

Now that I had the "distance" (in degrees) between each pixel for that ring, I could infer what pixel on a given ring was closest to a given angle: `startIndex + int(math.floor(angle/ringDegrees))`

What this does is map [polar coordinates](http://en.wikipedia.org/wiki/Polar_coordinate_system), angle and radius (ring index in this case), to a actual pixel index :) With a display like the one from Adafruit, this means that many angles will actually resolve to the same pixel for a given ring, but there's really no way around this. It's more and more the case as the ring gets smaller and contains fewer pixels. For example, the outer ring on the Adafruit display has 48 pixels which means 7.5° between each pixel, but the smallest ring (ignoring the single pixel center) has only 6 pixels, meaning a whopping 60° per pixel! Nothing to really be done about this, it's just the nature of circles. Despite this, I've found it's still _much_ easier to write animations for the display using polar coordinates. It just makes more sense, once you wrap your brain around it. It's limited compared to a matrix in some ways, but can do a lot more that a matrix cannot. Smooth circles are _never_ easy on a low resolution matrix.

I'm still trying to figure out the best way to do things like display text, but I'm sure that will come in time. In the mean time, I've wrapped all of this up into a couple of [BiblioPixel](/bibliopixel) classes that should make writing animations for the display a lot easier. First is [LEDCircle](https://github.com/ManiacalLabs/bibliopixel/wiki/LEDCircle) which, like [LEDMatrix](https://github.com/ManiacalLabs/bibliopixel/wiki/LEDMatrix), automatically handles mapping the 2D pixel arrangement to the 1D pixel indices (since all displays like this are logically a strip, just arranged differently). Second is [BaseCircleAnim](https://github.com/ManiacalLabs/bibliopixel/wiki/Animations#class-basecircleanim) which, like the other base animation classes, takes out all of the hard work of creating and running your animation code. All you have to do differently is use angle and radius (ring index) instead of pixel index or (x,y) coordinates. If you are interested more in how those classes work, certainly check out the links above to their Wiki pages. These new classes are being released with the brand new [BiblioPixel v1.2](/2015/05/04/bibliopixel-v1-2-is-here/). For now, I think it's going to be much easier to just show you how they can be used.

[gist https://gist.github.com/adammhaile/457aa849f8690eb1f769]

Run the above code and you will get this awesomeness:

{{< youtube bhW_CixG99o >}}

I'll certainly be writing more circle animations soon, and will be sure to post all of them on our [BiblioPixelAnimations](https://github.com/ManiacalLabs/bibliopixelAnimations) repository. In order to use LEDCircle and BaseCircleAnim, you will need the latest BiblioPixel, v1.2, which we are releasing today! And if you haven't seen it already, be sure to check out the [AllPixel](/AllPixel) which will have you pushing pixels to this, or nearly any, display in minutes!

While I love using BiblioPixel (and the AllPixel) for all my LED and animation work, don't think I'd leave out those that want to use this display with micro-controllers, like the Arduino, directly! The AllPixel is built upon the astounding [FastLED](http://fastled.io) library. So, of course, I had to make all this crazy polar coordinate mapping work with FastLED directly :) Check out the code below, which should hopefully give everyone a head start on programming their awesome new Adafruit DotStar disk! Happy Making!

[gist https://gist.github.com/adammhaile/a769f3ff87ff61f22ace]
