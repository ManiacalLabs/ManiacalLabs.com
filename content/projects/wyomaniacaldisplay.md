---
author: adam
date: 2016-03-05 17:06:07+00:00
draft: false
title: WyoManiacalDisplay
type: page
thumb: /images/wmd.png
description: 3k Pixels / 400 Watts
url: /wyomaniacaldisplay/
aliases:
  - /WyoManiacalDisplay/
---


After we unveiled [Colossus](/Colossus) back in September, our good friends at [WyoLum](http://WyoLum.com) challenged us to make something awesome with their [TiM LED panels](http://www.seeedstudio.com/depot/TiM-p-1516.html) and have it ready for the [NoVA Maker Faire](http://makerfairenova.com/) in Reston, VA on Marth 13th.

Many, many late nights  of coding, soldering, 3D printing, and fabricating later and it's finally ready to show off!

{{< youtube 9yjcHflWVkI >}}

Here's the specs:


  * 24 WyoLum TiM WS2812 Panels (in a 6 x 4 grid)
  * 64 x 48 Total Resolution - 3072 Pixels!
  * 3 Teensy 3.2's running modified [AllPixel](/AllPixel) firmware
  * Custom adapter PCBs with 74HCT245 buffer
  * 104A @ 5V Max power draw
  * Up to 60fps
  * Controlled by [BiblioPixel](/bibliopixel)
  * 175 3D printed components totaling 15 separate designs
  * [Acrylite 7C056](https://www.acrylite-shop.com/US/us/extruded-f0p5v3qaql1/acrylite-extruded-ff-grey-7c056-gt-ckhtgnt8efh~p.html) 8% transmission black acrylic front cover
  * Frame constructed from 3/4" MDF
  * 46" x 36" x 6" Total Dimensions


The display is actually divided into three separate sub-displays, each with 8 TiM panels, a 40A@5V power supply, and a Teensy 3.2 controller. These three sections are capable of acting independently, but are coordinated via BiblioPixel's [multiple driver support](https://github.com/ManiacalLabs/bibliopixel/wiki/Multiple-Driver-Support).

In order to achieve the highest possible framerate, we had to ditch the usual method of treating the display as one long strand of pixels. If we did it that way, it would take around 100ms just to update all the pixels once (WS2812 LEDs use a slow 800khz data rate) and that would mean a max frame-rate of 10fps. No good. This is where the Teensy and FastLED comes in. With some brilliant code from the FastLED guys, the Teensy can control WS2812 LEDs on up to 16 parallel channels simultaneously using DMA (Direct Memory Access). This allows almost no CPU load to push data to 1024 pixels (16 channels of 64 pixels each) in under 4ms. This is what the adapter PCB is for... it breaks out the 16 outputs from the Teensy, through the 74HCT245 buffer (which brings it from 3.3V to 5V logic), and through some impedance matching resistors.  This is done three times over (once for each sub-display) threaded in parallel (a feature built into BiblioPixel) allowing for a total update time of under 6ms (there's a little overhead for the USB). MUCH better than 100ms! This allows a theoretical frame-rate of over 150fps, but in practice it takes longer to generate the frame than it does to push it, so 60fps is more reasonable to expect.

We will soon be posting all of the 3D designs we used, the adapter PCBs, as well as the new animation code for things like displaying videos and audio spectrum as seen in the demo above, once we've had a chance to clean things up a little. As usual, the core software is [BiblioPixel](/bibliopixel) and [PixelWeb](/PixelWeb) which are completely open source.

That's all for now. Check out the gallery below, or see it in person at [NoVA Maker Faire](http://makerfairenova.com/) in Reston, VA on Marth 13th!

{{< gallery dir="/wp-content/galleries/2016-02-29-wyomaniacal-display-nova-maker-faire/0/" />}}

