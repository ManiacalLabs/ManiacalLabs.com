---
author: adam
date: 2015-06-02 03:44:14+00:00
draft: false
title: BiblioPixel Controlling a Jumbotron...
type: post
url: /2015/06/01/bibliopixel-controlling-a-jumbotron/
categories:
- AllPixel
- FastLED
- Projects
- SmartMatrix
---

{{< youtube q7PPyGEkRDU >}}

... sub-panel. Couldn't resist the mild click-bait there :) As you can see in the video above; no, not a full-on jumbotron, but just a single 32x32 panel designed for digital billboards. I've had one sitting in my parts drawer for nearly a year... But yesterday, the awesome [1-Pixel PacMan](http://hackaday.com/2015/06/01/1-pixel-pacman/) post on HackADay gave me enough of a push to finally pull it out and get hacking.

<!-- more -->

[These things](http://store.hackaday.com/products/smartmatrix-bundle) are seriously awesome. 1024 tiny RGB pixels packed into a roughly 8"x8" square panel. The problem, however, is that, unlike the LED strips supported by the [AllPixel](/AllPixel), these panels have basically zero logic built in. Instead of one long string of LEDs, they are actually built in a true matrix that must be manually [multiplexed](http://en.wikipedia.org/wiki/Multiplexed_display) by the controlling device. There's not even any memory on the display, so you have to _keep_ multiplexing... forever.

Fortunately, as is always the case in the world of open source, a bunch of smart people have already built cool things to help out! Enter the [SmartMatrix Teensy Shield](http://docs.pixelmatix.com/SmartMatrix/shieldref.html)! Which was also in my parts drawer for the last year :P SmartMatrix is a library for the [Teensy 3.x](http://store.hackaday.com/products/teensy-3-1) which is an awesome little ARM development board with a ton of power in a tiny package. The library uses some really fancy [DMA](http://en.wikipedia.org/wiki/Direct_memory_access) techniques to multiplex one of these panels at high frame-rates with almost negligible CPU overhead. While you _could_ wire up a Teensy directly to the display panel, the shield _greatly_ simplifies the process.

To further simplify things, the awesome guys at [FastLED](http://fastled.io) built in support for the SmartMatrix library a while back. Since the AllPixel firmware uses FastLED under the hood, there was only one thing to do... port the firmware to the Teensy 3.1 using the SmartMatrix extension so that it could work with [BiblioPixel](/bibliopixel) of course!

The port wasn't too bad as it mostly required _removing_ a ton of things like all the normal LED strip support. Technically I could have left all of that in, but since these panels are a fixed size it seemed to make more sense to produce a bespoke version of the firmware for this one application. Once that was done, it pretty much works just like the regular AllPixel except for being a fixed pixel count.

For code, instructions, and more technical details, be sure to check out the [SmartMatrix branch](https://github.com/ManiacalLabs/AllPixel/tree/SmartMatrix) of the AllPixel GitHub repo.
